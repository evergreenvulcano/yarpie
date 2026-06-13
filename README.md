# Yarpie

Yarpie is a static web repository for `yarpie.verbotenmedia.se`.

The repo is not the editorial machine and not the protected source layer. It is the public web body where approved or bounded outcomes can become pages, status blocks, navigation, 404 language, and other reviewable web surfaces.

## Repo Modules

- Root HTML pages form the current public portal surface.
- `index.html` - portal start page.
- `yarpie.html` - Yarpie / Orrengonjo Jarpie.
- `det-djupsamiska-naringslivet.html` - public system explanation.
- `sapmi-empire-intelligence.html` - English Lompolo-cybernetic front facade for the Sapmi Empire.
- `storbastutinget.html` - Storbastuting as storyworld heart, chronology, talordning, and public web edge.
- `kallvattenradet.html` - RUN A regional event surface for Kallvattenrådet / Kevne Kaiser.
- `framtidsplaner-2040.html` - succession and long-term preparation.
- `radio.html` - Ruinradio and signal window.
- `besoksfonster.html` - controlled contact / visit path.
- `fjarde-generationen.html` - Mermaid-rendered succession map.
- `sameklyvning-2026.html` - fulltext archive page for krönikav0, `_varldsvav`, and `_varldshiss_codex`.
- Additional stub rooms: radioskugga, korna, kosmiska kvadraten, scrolls, riskmotorn, world-events, ordlista.
- `assets/` contains shared styling, scripts, and local images.
- `modules/webbsamen/` defines the first Webbsamen repo module: how Codex may turn approved outcomes into reviewable web patches without exposing the editorial core.
- `modules/webbsamen/orders/` stores repo-specific content orders; Drive remains the writing surface.

## Working Principle

Webbsamen works through Codex. Changes should stay small enough to review, should preserve source boundaries, and should show blocked or held material as web discipline rather than as leaked content.

The repo can add or revise public routes when Storbastuting chronology and product gate leave a buildable consequence. It should not invent missing editorial material to make a page feel finished.

Each new Webbsamen surface should be able to point back to a ting, decision, stop, yrkande, andeförskjutning, or slussed value. The web builds handtag, not the core itself.

Webbsamen may audit the repo for content product-level improvement potential. A content audit may identify manifest stiffness, thin sections, missing passage, unclear navigation, weak retention, dead status surfaces, or pages that may need future editorial body. An audit must not create content orders automatically. It may only mark potential need; a request to `kontent_skribent` can be opened later after human confirmation or after a concrete Webbsamen build task proves that text is required.

## Local Preview

Open `index.html` directly in a browser, or serve the folder with:

```bash
python -m http.server 8141 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8141/
```

## GitHub Pages

This repo is prepared for static GitHub Pages publishing from `main` and `/ (root)`.

Custom domain:

```text
yarpie.verbotenmedia.se
```

See [PAGES_SETUP.md](PAGES_SETUP.md) for the GitHub Pages and Cloudflare settings.

## Boundaries

- Do not expose LOMPOLO-CORE as the public website.
- Do not publish protected sources, sensitive genealogy, or real personal data.
- Do not treat Mermaid succession nodes as verified people.
- Do not treat Strålsamen, Spräck, or Flempo as the entire portal voice.
- Do not make KSA/Korna into ordinary corporate governance.
- Do not import draft facade terms literally when they conflict with project specifics; normalize through Webbsamen before publication.
- Do not treat a product candidate as public release.
- Do not turn internal holds or blocked sources into ordinary content.
- Do not let repo convenience replace editorial judgment.

## External Notes

The prototype links to:

- https://VMNODEN.SE/
- https://JAMDA.APP/
- https://acarta.app/
