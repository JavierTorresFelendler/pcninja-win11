# win11.pcninja.pro

Source of the PcNinja Windows ISO page, served by GitHub Pages at https://win11.pcninja.pro
in English (`/`), Spanish (`/es/`) and Hebrew (`/he/`).

- `tools/build.py` – the ISO list and all page text; run `python tools/build.py` to regenerate the three pages and `sitemap.xml`
- `assets/site.css` – shared styles (same family as www and help)
- `home/` – redirect from the old Google Sites `/home` address

Visitors who open `/` are sent to their browser's language (Spanish or Hebrew) the first time;
the language buttons remember their choice.

The Download buttons point at the `*.pcninja.pro` short links (e.g. `aio11.pcninja.pro`),
which are forwarded at the domain registrar to the actual files. To publish a new ISO, add a
forwarding sub-domain at the registrar, then update `LATEST` / `OLDER` in `tools/build.py` and rebuild.
