# GitHub Pages Setup

This repository is prepared as a static GitHub Pages site for:

`yarpie.verbotenmedia.se`

## Recommended GitHub Pages Settings

Repository:

`evergreenvulcano/yarpie`

Pages source:

- Source: `Deploy from a branch`
- Branch: `main`
- Folder: `/ (root)`

Custom domain:

`yarpie.verbotenmedia.se`

The root `CNAME` file must contain only:

```text
yarpie.verbotenmedia.se
```

## Cloudflare DNS

Add this DNS record manually:

```text
Type:   CNAME
Name:   yarpie
Target: evergreenvulcano.github.io
Proxy:  DNS only
```

Keep the record as `DNS only` until GitHub Pages has accepted the custom domain and HTTPS is green.

Do not use a wildcard record such as `*.verbotenmedia.se` for this setup.

## Domain Boundary

The apex domain belongs to the main repository:

`verbotenmedia.se` -> `evergreenvulcano/VERBOTENMEDIA`

Do not set this repository's `CNAME` to:

`verbotenmedia.se`

This repository should own only:

`yarpie.verbotenmedia.se`

## Repo Shape

The site is static and publishes directly from repo root. There is no npm build, framework build output, `dist/`, or `docs/` publishing layer required for the current form.

The `.nojekyll` file is present so GitHub Pages serves the static root without Jekyll processing.
