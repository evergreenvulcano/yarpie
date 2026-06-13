# Webbsamen Protocol — Löpande format och regional event

Date: 2026-06-13
Status: `repo_patch_executed`
Surfaces: `veckans-same.html`, `kallvattenradet.html`, `index.html`, `webbsamen.html`

## Uppdrag

Keep:

- `webbsamen.html` as module status page.
- `storbastutinget.html` as heart/motor page.

Develop:

- `veckans-same.html` into the first running format.
- RUN A into a regional event page.
- Start page with a simple "senaste från tinget" component.

## RUN C Decision

`veckans-same.html` now behaves as a running format:

- previous recipients remain archive/value additions,
- the current loop explains talskuld → content order → review → HTML return,
- next issue is not guessed by the page,
- content need is ordered from `kontent_skribent`.

## RUN A Decision

`kallvattenradet.html` is created as a regional event surface for:

```text
RUN A / Kallvattenrådet vid Kevne Kaiser
```

It is not a press release. It shows candidate status, chronology, review need, and explicit constraints:

- no ice-pattern image,
- no miracle language,
- no tourism/attraction language,
- no causal explanation,
- no external release claim.

## Content Orders

Repo orders:

```text
modules/webbsamen/orders/2026-06-13_veckans_same_lopande_format.md
modules/webbsamen/orders/2026-06-13_kallvattenradet_eventkort.md
```

Drive intake:

```text
LOMPOLO-CORE/_redaktionell_contentlogik/03_artifacts/kontent_skribent/
```

Krönikörsamen remains a function inside `kontent_skribent`, not a repo module.

## Boundaries

- Candidate status remains visible.
- No protected source text is exposed.
- The start page shows slussed consequences only.
- Repo orders are not publication.
