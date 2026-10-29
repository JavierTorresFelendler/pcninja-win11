# win11.pcninja.pro

Source of the PcNinja "latest ISO" page, served by GitHub Pages at https://win11.pcninja.pro

- `index.html` – the ISO download page (plain HTML + CSS, no build step)
- `home/` – redirect from the old Google Sites `/home` address
- `assets/` – images

The Download buttons point at the `*.pcninja.pro` short links (e.g. `aio11.pcninja.pro`),
which are forwarded at the domain registrar to the actual files. To publish a new ISO, add a
forwarding sub-domain at the registrar and add a row to `index.html`.
