# Webbsamen Repomanifest

Status: pilot module
Active public surface: `webbsamen.html`
Repo mode: static HTML, CSS, assets, reviewable patches
Last executed: 2026-06-13 against Drive passage patch, Storbastuting-krönikan, and `_redaktionell_contentlogik/_register/STATUS_LEDGER_v0.md`

## Purpose

This manifest makes `explainerv0.md` actionable inside the Yarpie repo.

It defines what Webbsamen may build, what must remain only a visible stop, and what must not enter the public web surface.

## Primary Anchor

Webbsamen now builds from the Storbastuting chronology first, then from the redaktionella contentlogik as sluss.

The repo must treat:

```text
Sameräknaren
  as vilka

Storbastuting-krönikan
  as när, vad, beslut, anda

_redaktionell_contentlogik
  as how ting value is slussed, held, blocked, or made buildable

Webbsamen
  as the digital handtag-builder

Yarpie
  as public body: door, window, status, 404, format, protocol edge
```

The Storbastuting chronology is an index and backbone, not publishable source copy. A web surface may refer to the public consequence of a ting, decision, hold, stop, or andeförskjutning; it must not turn the core into a tour.

## Allowed Repo Consequences

- Create or extend static HTML pages when product gate has left a buildable consequence.
- Tie each new public surface back to a ting, decision, stop, yrkande, andeförskjutning, or slussed value.
- Add navigation links when a page becomes a real public route.
- Add public status blocks for waiting, held, blocked, or review states.
- Add recurring layout patterns for approved public formats.
- Improve 404 and closed-edge copy when a blocked state needs to be visible.
- Keep module documentation current when scope changes.
- Create repo-specific content orders when a page is buildable but text-poor; do not write free content to hide the gap.

## Stop Rules

- Do not open protected sources.
- Do not publish product candidates as if they are released material.
- Do not make the core into a website.
- Do not treat the Storbastuting-krönikan as public source copy.
- Do not write free lore to fill missing editorial output.
- Do not replace editorial judgment with repo convenience.
- Do not treat a content order as publication.

## Content Orders

Repo order path:

```text
modules/webbsamen/orders/
```

Drive execution path:

```text
LOMPOLO-CORE/_redaktionell_contentlogik/03_artifacts/kontent_skribent/
```

Webbsamen may order krönikerande brödtext, eventkort, signalnotis, mottagarkort, protokollkant, 404-copy, mikrocopy, övergångstext, läsnästa-copy, or human-review-fråga. Krönikörsamen is a role inside `kontent_skribent`, not a new repo module.

## Current Web Map

| Outcome | Repo treatment | Public treatment |
| --- | --- | --- |
| `veckans_same` | Talskuld/talordning echo after product gate. | Public, readable format where "previous" is not rank. |
| `kontent_kronikor` | Yarpie window, chronicle list, or single chronicle page after ting/sluss. | Public web window, not raw source. |
| `press_release/regional_initiatives` | Event-like public notice after ting, rådslag, or torgmöte. | Public event surface with clear status, not ordinary press template. |
| `hold_internal` | Status line, closed-edge copy, or internal-hold indicator. | Tingets right to keep something in the bastu; visible discipline, not content. |
| `blocked_protected_source` | 404 language, blocked-edge notice, or proof-of-integrity marker. | Avståendets etik: proof that a boundary exists, not a source excerpt. |

## Executed Passage: 2026-06-13

Source layer: Drive filesystem, `_redaktionell_contentlogik`.

Storbastuting anchor: `_infrastruktur/STORBASTUTING_KRONIKAN.md` is now read as the chronology index above this passage. The passage package remains useful, but secondary.

| Run | Source status | Webbsamen decision | Repo consequence |
| --- | --- | --- | --- |
| A | `official_candidate_not_published` in `press_release/regional_initiatives` | Show as eventable public status after ting, not release. | `kallvattenradet.html`, status row on `webbsamen.html`. |
| B | `blocked_protected_source` / `needs_human_provenance_decision` | Show the stop as avståendets etik without source detail. | Stop edge on `webbsamen.html` and 404 discipline. |
| C | `official_candidate_not_published` in `veckans_same` | Prepare talskuld/talordning format after light human review. | Running format on `veckans-same.html`, order for next issue. |
| H | `official_candidate_not_published` in `kontent_kronikor` | Install Yarpie-window logic: public breadth against closed depths. | Active Webbsamen status surface on `webbsamen.html`. |
| J | `hold_internal` | Keep as internal hold; only the edge is visible. | Closed-edge status on `webbsamen.html`. |

No candidate draft text is published by this run. The web page shows status, format, and boundary only.

## Specialpass: Veckans Same 2026-06-13

Source layer: Drive filesystem, `04_product/veckans_same`.

Ting anchor: the page is now read as a talskuld/talordning echo from Storbastuting logic: low/long unheard does not mean low value.

Decision: build a focused Veckans Same page with previous recipients as value additions, while preserving the source status `official_candidate_not_published`.

Repo consequences:

- `veckans-same.html`
- `protocols/2026-06-13_veckans_same_specialpass.md`
- `registers/veckans_same_recipients_v0.md`

## Ting-till-Webb Pass: 2026-06-13

Drive protocol:

```text
_redaktionell_contentlogik/03_artifacts/_websamens_window/WEBBSAMEN_TING_TILL_WEBB_PROTOCOL_2026-06-13.md
```

Repo consequences:

- revise `webbsamen.html` so Storbastuting is the motor and Webbsamen is the digital handtag-builder,
- revise `storbastutinget.html` so the public page frames tinget as heart/motor without opening the core,
- revise `veckans-same.html` so the format is tied to talordning and talskuld, not generic light content,
- record this protocol in `protocols/2026-06-13_storbastuting_anchor_pass.md`.

Rules:

- Recipients are not ranked.
- Talskuld numbers remain internal.
- Consent-bound and missing/not-declared-dead cases remain visibly bounded.
- Deceased figures omitted by source rule remain omitted.

## Patch Flow

1. Identify the ting, decision, stop, yrkande, andeförskjutning, or slussed value.
2. Identify the product-gate status.
3. Choose whether it is a public format, a status edge, a closed door, or a 404.
4. Patch the smallest relevant web surface as a digital handtag.
5. Keep source-protection language explicit when a block is visible.
6. Leave a reviewable diff: HTML, CSS, docs, or navigation only.

## Active Subpage Contract

`webbsamen.html` is the current public route for this module. It may show:

- Webbsamen as a repo role,
- the working chain from editorial outcome to web surface,
- buildable format families,
- non-content stop states,
- proof that Yarpie has boundaries.

It must not show:

- protected source text,
- internal editorial material,
- unpublished candidates represented as release,
- claims that Webbsamen is the editorial machine.
