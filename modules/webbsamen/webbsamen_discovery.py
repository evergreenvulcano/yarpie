#!/usr/bin/env python3
"""Repo-local discovery utility for Yarpie's public web surface.

The utility reports reviewable signals only. It does not write content, open
orders, publish pages, or inspect protected source layers.
"""

from __future__ import annotations

import argparse
import html.parser
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote, urlparse


CATEGORIES = {
    "broken",
    "orphan",
    "thin_surface",
    "navigation_gap",
    "status_unclear",
    "content_need",
    "style_risk",
    "public_bound_candidate",
    "do_not_touch",
}

WEB_EXTENSIONS = {".html", ".md"}
SKIP_DIRS = {".git", "assets"}
DO_NOT_TOUCH_PARTS = {"orders", "protocols", "registers"}
PUBLIC_STATUS_TERMS = (
    "public",
    "publik",
    "status",
    "under värme",
    "kandidat",
    "candidate",
    "review",
    "spärr",
    "hold",
    "blocked",
    "stängd",
)
CONTENT_NEED_TERMS = (
    "under värme",
    "behöver content",
    "behöver text",
    "missing passage",
    "kontent_skribent",
    "TODO",
    "FIXME",
)
STYLE_RISK_TERMS = (
    "manifest",
    "manifestet",
    "protocol",
    "protokoll",
    "system",
    "apparat",
    "repomanifest",
)
LOCAL_NERVE_TERMS = (
    "besök",
    "rum",
    "sida",
    "händelse",
    "mottagare",
    "kontakt",
    "öppna",
    "visa",
)


@dataclass
class Link:
    target: str
    line: int


@dataclass
class Page:
    path: Path
    rel: str
    text: str
    lines: list[str]
    title: str | None
    description: str | None
    ids: set[str]
    links: list[Link]
    nav_links: list[str]


@dataclass
class Finding:
    category: str
    file: str
    line: str
    diagnosis: str
    why_it_matters: str
    minimum_safe_action: str
    risk: str
    needs_human_mandate: bool

    def __post_init__(self) -> None:
        if self.category not in CATEGORIES:
            raise ValueError(f"Unknown category: {self.category}")


class HTMLSurfaceParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title: str | None = None
        self.description: str | None = None
        self.ids: set[str] = set()
        self.links: list[Link] = []
        self.nav_links: list[str] = []
        self._in_title = False
        self._in_nav = False
        self._title_chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if "id" in data and data["id"]:
            self.ids.add(data["id"] or "")
        if "name" in data and data["name"]:
            self.ids.add(data["name"] or "")
        if tag == "title":
            self._in_title = True
            self._title_chunks = []
        if tag == "nav":
            self._in_nav = True
        if tag == "meta" and data.get("name") == "description":
            self.description = data.get("content")
        if tag in {"a", "link"} and data.get("href"):
            self.links.append(Link(data["href"] or "", self.getpos()[0]))
            if self._in_nav and tag == "a":
                self.nav_links.append(data["href"] or "")
        if tag in {"img", "script"} and data.get("src"):
            self.links.append(Link(data["src"] or "", self.getpos()[0]))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self._in_title = False
            self.title = " ".join("".join(self._title_chunks).split())
        if tag == "nav":
            self._in_nav = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_chunks.append(data)


def line_for_match(lines: list[str], pattern: str) -> str:
    lowered = pattern.lower()
    for index, line in enumerate(lines, start=1):
        if lowered in line.lower():
            return str(index)
    return "-"


def first_term_line(lines: list[str], terms: Iterable[str]) -> str:
    for term in terms:
        line = line_for_match(lines, term)
        if line != "-":
            return line
    return "-"


def strip_markdown_links(text: str) -> list[Link]:
    links: list[Link] = []
    pattern = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
    for line_number, line in enumerate(text.splitlines(), start=1):
        for match in pattern.finditer(line):
            links.append(Link(match.group(1), line_number))
    return links


def collect_pages(root: Path) -> dict[str, Page]:
    pages: dict[str, Page] = {}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in WEB_EXTENSIONS:
            continue
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        if path.suffix.lower() == ".html":
            parser = HTMLSurfaceParser()
            parser.feed(text)
            page = Page(path, rel, text, lines, parser.title, parser.description, parser.ids, parser.links, parser.nav_links)
        else:
            first_heading = next((line.strip("# ").strip() for line in lines if line.startswith("#")), None)
            page = Page(path, rel, text, lines, first_heading, None, set(), strip_markdown_links(text), [])
        pages[rel] = page
    return pages


def is_external(target: str) -> bool:
    parsed = urlparse(target)
    return parsed.scheme in {"http", "https", "mailto", "tel"} or target.startswith(("javascript:", "data:"))


def resolve_link(source: Page, root: Path, target: str) -> tuple[Path | None, str | None]:
    if not target or is_external(target):
        return None, None
    clean_target = target.split("?", 1)[0]
    path_part, _, anchor = clean_target.partition("#")
    if not path_part:
        return source.path, anchor or None
    path_part = unquote(path_part)
    if path_part.startswith("/"):
        candidate = root / path_part.lstrip("/")
    else:
        candidate = source.path.parent / path_part
    if candidate.is_dir():
        candidate = candidate / "index.html"
    return candidate.resolve(), anchor or None


def add_finding(findings: list[Finding], *args: object) -> None:
    findings.append(Finding(*args))  # type: ignore[arg-type]


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\wåäöÅÄÖ-]+\b", text))


def classify_pages(root: Path, pages: dict[str, Page]) -> list[Finding]:
    findings: list[Finding] = []
    html_pages = {rel: page for rel, page in pages.items() if page.path.suffix.lower() == ".html"}
    all_known = {page.path.resolve(): page for page in pages.values()}
    referenced: set[str] = set()
    nav_referenced: set[str] = set()
    title_to_pages: dict[str, list[Page]] = {}

    for page in html_pages.values():
        if page.title:
            title_to_pages.setdefault(page.title.lower(), []).append(page)
        for link in page.links:
            resolved, anchor = resolve_link(page, root, link.target)
            if resolved is None:
                continue
            rel_target = resolved.relative_to(root).as_posix() if root in resolved.parents or resolved == root else None
            if rel_target:
                referenced.add(rel_target)
                if link.target in page.nav_links:
                    nav_referenced.add(rel_target)
            if not resolved.exists():
                add_finding(
                    findings,
                    "broken",
                    page.rel,
                    str(link.line),
                    f"Intern länk pekar mot saknad fil: {link.target}",
                    "Trasiga interna länkar bryter portalens handtag och gör statusytor svåra att reviewa.",
                    "Korrigera länken, skapa bara sidan om den redan har mandat, eller markera den som väntande i befintlig navigation.",
                    "medel",
                    True,
                )
            elif anchor and resolved in all_known and resolved.suffix.lower() == ".html":
                target_page = all_known[resolved]
                if anchor not in target_page.ids:
                    add_finding(
                        findings,
                        "broken",
                        page.rel,
                        str(link.line),
                        f"Intern ankarlänk saknar mål-id: {link.target}",
                        "Ankare som inte landar gör navigationen opålitlig även när filen finns.",
                        "Lägg till befintligt id som mål eller ändra ankaret till en existerande sektion.",
                        "låg",
                        False,
                    )

    for rel, page in html_pages.items():
        if rel == "index.html":
            continue
        if rel not in referenced and rel != "404.html":
            add_finding(
                findings,
                "orphan",
                rel,
                "-",
                "HTML-sidan hittas inte från någon intern HTML-länk.",
                "Publika sidor utan väg från portalen blir parkerade ytor snarare än reviewbara entry surfaces.",
                "Länka från index/navigation om sidan är publik, eller markera status/hold om den bara ska ligga kvar.",
                "medel",
                True,
            )
        elif rel not in nav_referenced and rel != "404.html":
            add_finding(
                findings,
                "navigation_gap",
                rel,
                "-",
                "Sidan är länkad men saknar tydlig plats i återkommande navigation.",
                "En sida kan vara nåbar men ändå sakna relation till portalens huvudvägar.",
                "Lägg till navigation bara om ytan är en huvudroute; annars lägg en lokal återväg eller tydlig placering.",
                "låg",
                True,
            )

        wc = word_count(re.sub(r"<[^>]+>", " ", page.text))
        has_status = any(term in page.text.lower() for term in PUBLIC_STATUS_TERMS)
        if wc < 120:
            add_finding(
                findings,
                "thin_surface",
                rel,
                "1",
                f"Sidan är mycket tunn ({wc} ord).",
                "Tunna entry surfaces kan kännas som döda dörrar om status och nästa steg inte är tydliga.",
                "Lägg till status, återväg eller beställningssignal; skriv inte ny brödtext utan mandat.",
                "låg",
                True,
            )
        if not page.title or not page.description:
            missing = "title" if not page.title else "meta description"
            add_finding(
                findings,
                "status_unclear",
                rel,
                "1",
                f"Sidan saknar {missing}.",
                "Metadata hjälper webbytan att förklara vad sidan är utan att öppna källmaterial.",
                "Lägg till minimal titel/beskrivning som beskriver status och placering.",
                "låg",
                False,
            )
        if not has_status and rel not in {"404.html"}:
            add_finding(
                findings,
                "status_unclear",
                rel,
                "1",
                "Sidan verkar publik men saknar tydlig statusmarkör.",
                "När status saknas är det svårt att skilja release, kandidat, hold och fönster.",
                "Lägg en kort befintlig statusmarkör, eller låt människan bekräfta sidans publiceringsläge.",
                "medel",
                True,
            )

        lower_text = page.text.lower()
        if any(term.lower() in lower_text for term in CONTENT_NEED_TERMS) and wc < 260:
            add_finding(
                findings,
                "content_need",
                rel,
                first_term_line(page.lines, CONTENT_NEED_TERMS),
                "Sidan signalerar väntande material men har ännu svag lokal kropp.",
                "Det kan minska manifestliknande stelhet, men Webbsamen ska inte skriva texten själv.",
                "Formulera som beställningssignal till mänskligt mandat eller kontent_skribent, inte som färdig text.",
                "medel",
                True,
            )

        style_hits = sum(lower_text.count(term) for term in STYLE_RISK_TERMS)
        nerve_hits = sum(lower_text.count(term) for term in LOCAL_NERVE_TERMS)
        if wc > 180 and style_hits >= 8 and style_hits > nerve_hits:
            add_finding(
                findings,
                "style_risk",
                rel,
                "1",
                "Sidan har hög täthet av manifest-/systemord jämfört med lokala webbsignaler.",
                "Produktnivån kan stelna till manifest i stället för att fungera som levande entry surface.",
                "Beställ lokal ingress, exempel eller övergångstext efter mandat; ändra inte rösten automatiskt.",
                "medel",
                True,
            )

    for title, group in title_to_pages.items():
        if len(group) > 1:
            files = ", ".join(page.rel for page in group)
            for page in group:
                add_finding(
                    findings,
                    "navigation_gap",
                    page.rel,
                    "1",
                    f"Delad sidtitel med annan HTML-yta: {files}",
                    "Upprepade entry surfaces kan göra det oklart vilken sida som är huvudväg.",
                    "Ge sidorna mer precis titel eller markera en som arkiv/profil/status.",
                    "låg",
                    False,
                )

    for rel, page in pages.items():
        parts = set(Path(rel).parts)
        if parts & DO_NOT_TOUCH_PARTS:
            add_finding(
                findings,
                "do_not_touch",
                rel,
                "-",
                "Filen ligger i order/protokoll/register-yta och ska inte behandlas som fri webbcontent.",
                "Discoveryn får se att filen finns, men ska inte extrahera eller omvandla den till publik sida.",
                "Rör inte innehållet; använd endast filens existens som status- eller provenienssignal.",
                "hög",
                True,
            )
        elif rel.startswith("modules/") and rel.endswith(".md") and "README" not in rel and "repomanifest" not in rel:
            add_finding(
                findings,
                "public_bound_candidate",
                rel,
                "-",
                "Modulfilen kan påverka webbytan men är inte själv en publik route.",
                "Sådana filer kan locka till publicering trots att de ofta är protokoll, order eller register.",
                "Behåll som intern repo-signal tills människa pekar ut en konkret webbyta.",
                "medel",
                True,
            )

    return sorted(findings, key=lambda f: (f.category, f.file, f.line, f.diagnosis))


def format_markdown(findings: Iterable[Finding]) -> str:
    rows = []
    for item in findings:
        mandate = "ja" if item.needs_human_mandate else "nej"
        rows.append(
            "\n".join(
                [
                    f"- `{item.category}` | `{item.file}` | line: {item.line} | risk: {item.risk} | human: {mandate}",
                    f"  Diagnos: {item.diagnosis}",
                    f"  Varför: {item.why_it_matters}",
                    f"  Minsta säkra åtgärd: {item.minimum_safe_action}",
                ]
            )
        )
    return "\n".join(rows) if rows else "Inga discovery-fynd."


def main() -> int:
    default_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(description="Scan Yarpie's public web surface for reviewable Webbsamen findings.")
    parser.add_argument("--root", type=Path, default=default_root, help="Repo root to scan. Defaults to Yarpie repo root.")
    parser.add_argument("--format", choices=("md", "json"), default="md", help="Output format.")
    parser.add_argument("--limit", type=int, default=80, help="Maximum findings to print.")
    args = parser.parse_args()

    root = args.root.resolve()
    pages = collect_pages(root)
    findings = classify_pages(root, pages)[: args.limit]

    if args.format == "json":
        print(json.dumps([asdict(finding) for finding in findings], ensure_ascii=False, indent=2))
    else:
        print(format_markdown(findings))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
