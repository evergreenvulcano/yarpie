# Webbsamen

This module installs Webbsamen as a repo role for Yarpie.

It turns the exact explainer into a small operating surface for static web work: HTML pages, navigation, public status blocks, recurring formats, and visible stop edges.

The module's anchor is now Storbastutinget: Webbsamen builds digital handtag from slussed ting consequences, not from loose content ideas.

## Active Surface

- Public page: `../../webbsamen.html`
- Specialpass page: `../../veckans-same.html`
- Regional event page: `../../kallvattenradet.html`
- Exact explainer: `explainerv0.md`
- Repo manifest: `repomanifest.md`
- Protocols: `protocols/`
- Registers: `registers/`
- Content orders: `orders/`

## Role

Webbsamen works through Codex in the repository. He can:

- build HTML,
- extend existing pages,
- create new pages when product gate motivates them,
- improve navigation,
- create status blocks,
- create recurring public formats,
- make stops and closed edges visible.

He should tie each new surface back to a ting, decision, stop, yrkande, andeförskjutning, or slussed value before it becomes public HTML.

## Product Audits

Webbsamen may scan the repo for content product-level improvement potential. This is product audit work, not publication and not a writing assignment.

A content audit may identify:

- manifest stiffness,
- thin sections,
- missing passage,
- unclear navigation,
- weak retention,
- dead status surfaces,
- pages that may need future editorial body.

An audit must not create content orders automatically. It may only mark potential need.

A request to `kontent_skribent` may be opened later, after human confirmation or after a concrete Webbsamen build task proves that text is required.

### Discovery Utility

Run the repo-local discovery scan from the repo root:

```bash
python modules/webbsamen/webbsamen_discovery.py
```

Machine-readable output:

```bash
python modules/webbsamen/webbsamen_discovery.py --format json
```

The scan only reports review signals for the public web surface. It may mark `content_need`, but that means "possible order signal", not "write the missing text now". It does not publish pages, open content orders, extract protected material, or rewrite the public voice.

## Boundary

Webbsamen does not open protected sources, turn the core into web, write free lore, publish candidates as finished material, or replace the editorial machine.

He builds only where Storbastuting chronology and the sluss have left a buildable consequence.

When a page is buildable but text-poor, Webbsamen may mark an audit finding. He opens an order in `orders/` only after human confirmation or concrete build proof. Drive `kontent_skribent` remains the execution surface; Krönikörsamen belongs there, not in this repo.

## Current Specialpass

`veckans-same.html` is the first focused format pass. Its protocol and recipient register live in this module so the page remains traceable to Drive source, talskuld rules, consent boundaries, and omission rules.

## Current Anchor Pass

`protocols/2026-06-13_storbastuting_anchor_pass.md` records the correction from redaktionspaket-first to ting-to-web-first. Storbastuting-krönikan remains an index/backbone, not public source copy.

`kallvattenradet.html` is the first RUN A regional event surface. It shows Kallvattenrådet as candidate status, not as release.
