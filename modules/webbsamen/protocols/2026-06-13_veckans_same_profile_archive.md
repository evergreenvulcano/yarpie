# Webbsamen Protocol — Veckans Same Profile + Archive

Date: 2026-06-13
Status: `repo_patch_executed`
Surface:

```text
veckans-same.html
veckans-same-profil.html
```

## Decision

Veckans Same should not remain only a format explanation and recipient grid.

The running format now needs:

- one current profile page that presents the latest registered Veckans Same,
- an archive of previous recipients,
- public-facing facts that increase reader understanding of Lompoloätten and the verksamheter without opening the protected core.

## Current Profile

Current profile: `Dösamen`

Reason: Dösamen is the latest registered recipient in `veckans_same_recipients_v0.md`. The profile is therefore a web split from the existing register, not a new recipient invented by the repo.

## Public Facts Allowed

The profile may show:

- popularity band,
- family relation at public-orientation level,
- brief CV,
- web/status boundary.

The profile must not show:

- talskuld numbers,
- ranked popularity,
- protected family mapping,
- source-copy from Drive,
- final publication claims.

## Repo Consequence

- `veckans-same.html` now points to the current profile and treats earlier recipients as archive/value additions.
- `veckans-same-profil.html` presents Dösamen with introduction, orienting facts, and boundary language.
- The registry records the split so the next profile can replace the current one after review while previous profiles move into the archive.
