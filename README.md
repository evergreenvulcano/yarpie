# Yarpie static prototype

Detta repo innehåller en dependency-light statisk prototyp för Yarpie, det offentliga webbfönstret för **Det Djupsamiska Näringslivet**.

> Status: prototyp / internt arbetsmaterial. Ej slutlig offentlig copy.

## Lokal förhandsvisning

Du kan öppna `/home/runner/work/yarpie/yarpie/evergreenvulcano/yarpie/index.html` direkt i webbläsare, eller starta en enkel statisk server från repo-roten:

```bash
python -m http.server 8000
```

Öppna sedan `http://localhost:8000/index.html`.

## Struktur

- `index.html`
- `yarpie.html`
- `det-djupsamiska-naringslivet.html`
- `storbastutinget.html`
- `framtidsplaner-2040.html`
- `radio.html`
- `besoksfonster.html`
- `fjarde-generationen.html` (Mermaid-diagram via CDN)
- Stubb-sidor: `fraga-under-varme.html`, `radioskuggan.html`, `korna.html`, `kosmiska-kvadraten.html`, `scrolls.html`, `riskmotorn.html`, `world-events.html`, `ordlista.html`
- `assets/css/styles.css`
- `assets/js/site.js`
- `assets/images/portal-hero.svg`

## Innehållssäkerhet och publiceringsregler

- Publicera endast verifierat material; allt annat är under värme.
- Yarpie är ett kontrollerat portalfönster, inte ett fullständigt arkiv.
- LOMPOLO-CORE ska inte exponeras som fullt webbinnehåll.
- Publicera inte känslig genealogi, persondata eller påståenden om verkliga samiska institutioner.
- Ingen extern analytics eller backend används i prototypen.

## GitHub Pages

Denna struktur fungerar för GitHub Pages från default branch root.

Repositoryt är tänkt att ligga under `https://verbotenmedia.se/yarpie/`, därför används root-relativa länkar med `/yarpie/`-prefix.
