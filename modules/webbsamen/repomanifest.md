# Webbsamen Repomanifest

Status: pilot module
Active public surface: `webbsamen.html`
Repo mode: static HTML, CSS, assets, reviewable patches
Last executed: 2026-06-13 against Drive passage patch and `_redaktionell_contentlogik/_register/STATUS_LEDGER_v0.md`

## Purpose

This manifest makes `explainerv0.md` actionable inside the Yarpie repo.

It defines what Webbsamen may build, what must remain only a visible stop, and what must not enter the public web surface.

## Allowed Repo Consequences

- Create or extend static HTML pages when product gate has left a buildable consequence.
- Add navigation links when a page becomes a real public route.
- Add public status blocks for waiting, held, blocked, or review states.
- Add recurring layout patterns for approved public formats.
- Improve 404 and closed-edge copy when a blocked state needs to be visible.
- Keep module documentation current when scope changes.

## Stop Rules

- Do not open protected sources.
- Do not publish product candidates as if they are released material.
- Do not make the core into a website.
- Do not write free lore to fill missing editorial output.
- Do not replace editorial judgment with repo convenience.

## Current Web Map

| Outcome | Repo treatment | Public treatment |
| --- | --- | --- |
| `veckans_same` | Repeating light-format page block or archive item after product gate. | Public, readable, low-friction format. |
| `kontent_kronikor` | Yarpie window, chronicle list, or single chronicle page. | Public web window, not raw source. |
| `press_release/regional_initiatives` | Event-like public notice, dated page, or signal card. | Public event surface with clear status. |
| `hold_internal` | Status line, closed-edge copy, or internal-hold indicator. | Visible discipline, not content. |
| `blocked_protected_source` | 404 language, blocked-edge notice, or proof-of-integrity marker. | Proof that a boundary exists, not a source excerpt. |

## Executed Passage: 2026-06-13

Source layer: Drive filesystem, `_redaktionell_contentlogik`.

| Run | Source status | Webbsamen decision | Repo consequence |
| --- | --- | --- | --- |
| A | `official_candidate_not_published` in `press_release/regional_initiatives` | Show as regional candidate status, not release. | Status row on `webbsamen.html`. |
| B | `blocked_protected_source` / `needs_human_provenance_decision` | Show the stop as proof-of-integrity without source detail. | Stop edge on `webbsamen.html` and 404 discipline. |
| C | `official_candidate_not_published` in `veckans_same` | Prepare recurring light format after light human review. | Format card and run row on `webbsamen.html`. |
| H | `official_candidate_not_published` in `kontent_kronikor` | Install Yarpie-window logic without exposing core. | Active Webbsamen status surface on `webbsamen.html`. |
| J | `hold_internal` | Keep as internal hold; only the edge is visible. | Closed-edge status on `webbsamen.html`. |

No candidate draft text is published by this run. The web page shows status, format, and boundary only.

## Specialpass: Veckans Same 2026-06-13

Source layer: Drive filesystem, `04_product/veckans_same`.

Decision: build a focused Veckans Same page with previous recipients as value additions, while preserving the source status `official_candidate_not_published`.

Repo consequences:

- `veckans-same.html`
- `protocols/2026-06-13_veckans_same_specialpass.md`
- `registers/veckans_same_recipients_v0.md`

Rules:

- Recipients are not ranked.
- Talskuld numbers remain internal.
- Consent-bound and missing/not-declared-dead cases remain visibly bounded.
- Deceased figures omitted by source rule remain omitted.

## Patch Flow

1. Identify the outcome and its product-gate status.
2. Choose whether it is a public format, a status edge, or a blocked edge.
3. Patch the smallest relevant web surface.
4. Keep source-protection language explicit when a block is visible.
5. Leave a reviewable diff: HTML, CSS, docs, or navigation only.

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
