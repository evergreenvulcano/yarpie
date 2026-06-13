# Yarpie

Static website prototype for `yarpie.verboten.se`.

Yarpie is the public-facing portal for Det Djupsamiska Näringslivet: a controlled web window, not a full archive and not the exposed LOMPOLO-CORE engine.

## Structure

- `index.html` — portal start page.
- `yarpie.html` — Yarpie / Orrengonjo Jarpie.
- `det-djupsamiska-naringslivet.html` — public system explanation.
- `storbastutinget.html` — governance and decisions under heat.
- `framtidsplaner-2040.html` — succession and long-term preparation.
- `radio.html` — Ruinradio and signal window.
- `besoksfonster.html` — controlled contact / visit path.
- `fjarde-generationen.html` — Mermaid-rendered succession map.
- Additional stub rooms: radioskugga, korna, kosmiska kvadraten, scrolls, riskmotorn, world-events, ordlista.
- `assets/css/styles.css` — site styling.
- `assets/js/site.js` — small progressive enhancements.
- `assets/images/` — local visual assets.

## Local Preview

Open `index.html` directly in a browser, or serve the folder with:

```bash
python -m http.server 8141 --bind 127.0.0.1
```

Then open:

```text
http://127.0.0.1:8141/
```

## Content Safety

This is a prototype, not final public copy.

- Do not expose LOMPOLO-CORE as the public website.
- Do not publish sensitive genealogy or real personal data.
- Do not treat Mermaid succession nodes as verified people.
- Do not treat Strålsamen, Spräck, or Flempo as the entire portal voice.
- Do not make KSA/Korna into ordinary corporate governance.

## External Notes

The prototype links to:

- https://VMNODEN.SE/
- https://JAMDA.APP/
- https://acarta.app/

