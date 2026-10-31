"""Build win11.pcninja.pro in English (/), Spanish (/es/) and Hebrew (/he/).

To publish a new ISO: add a forwarding sub-domain at the registrar, move the current
LATEST into the top of OLDER, put the new one in LATEST, then run:  python tools/build.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://win11.pcninja.pro"

# ---- The ISOs -------------------------------------------------------------
# type: aio = All-in-one installer (needs internet), pre = preinstalled image (offline), two = 2 options
LATEST = {"ver": "Windows 11 Pro 26H2", "type": "aio", "size": "8.5 GB", "url": "https://aio11.pcninja.pro"}
OLDER = [
    ("Windows 11 Pro 25H2 v2", "pre", "10 GB", "https://3in11.pcninja.pro"),
    ("Windows 11 Pro 25H2 v2", "aio", "7.4 GB", "https://aio25h2v2.pcninja.pro"),
    ("Windows 11 Pro 24H2", "aio", "5 GB", "https://ninja11pro24h2.pcninja.pro"),
    ("Windows 11 Pro 24H2", "pre", "7.5 GB", "https://3in11pro24h2.pcninja.pro"),
    ("Windows 11 Pro 23H2", "aio", "5.8 GB", "https://ninja11pro23h2.pcninja.pro"),
    ("Windows 10 Pro 22H2", "two", "5 GB", "https://ninja10pro22h2.pcninja.pro"),
    ("Windows 10 Pro 21H2", "pre", "8.4 GB", "https://ninja10pro21h2.pcninja.pro"),
    ("Windows 10 Pro 21H1", "pre", "7.8 GB", "https://ninja10pro21h1.pcninja.pro"),
    ("Windows 10 Ninjutsu v1.0", "pre", "17.8 GB", "https://ninjutsu.pcninja.pro"),
]

# ---- Text -----------------------------------------------------------------
T = {
 "en": dict(
  title="Windows ISOs - PcNinja",
  desc="Clean Windows 11 Pro ISOs from PcNinja. Each ISO has three install options: Full, Basic apps or Vanilla.",
  nav_home="PcNinja", nav_help="Remote support", nav_office="Office installer",
  latest="Latest", lang_line="English", size="Size", update="Offline update: March 2026", dl_iso="Download ISO",
  aio="All-in-one · needs internet", pre="Preinstalled · works offline", two="2 install options",
  opts_h="Every ISO has the same three install options", option="option", pro="Pro edition only",
  intro="Every build starts from Microsoft's official image, and I keep only the Professional edition. Home, Education and the other editions are not included.",
  o1="Full", o1_t="Fully working system with Office, Chrome and 7-Zip.",
  o2="Basic apps", o2_t="Windows Pro with the essential programs.",
  o3="Vanilla", o3_t="Microsoft's Windows Pro image only, nothing added.",
  notes_h="Before you install",
  n1="The ISO language is always English (en-US). You can add your own display language after setup in Settings &gt; Time &amp; language. A step-by-step guide is coming.",
  n2="Don't use Rufus options to bypass hardware checks.",
  n3="Setup logs in automatically as the local Administrator. To skip that, delete <code>autounattend.xml</code> from the ISO root.",
  n4="All-in-one installs need internet (Office and Chrome download during setup). Preinstalled images work offline.",
  n5='Only need Office? Use the <a href="https://office.pcninja.pro/">Office Smart Installer</a>.',
  older_h="Earlier versions", th_ver="Version", th_type="Type", th_size="Size", dl="Download",
  f_home="PcNinja home", f_help="Remote support", f_office="Office installer", f_gh="GitHub"),
 "es": dict(
  title="ISOs de Windows - PcNinja",
  desc="ISOs limpias de Windows 11 Pro de PcNinja. Cada ISO tiene tres opciones de instalación: Completa, Programas básicos o Vanilla.",
  nav_home="PcNinja", nav_help="Soporte remoto", nav_office="Instalador de Office",
  latest="Última versión", lang_line="Inglés", size="Tamaño", update="Actualización offline: marzo de 2026", dl_iso="Descargar ISO",
  aio="All-in-one · requiere internet", pre="Preinstalado · funciona sin internet", two="2 opciones de instalación",
  opts_h="Cada ISO tiene las mismas tres opciones de instalación", option="opción", pro="Solo edición Pro",
  intro="Cada build parte de la imagen oficial de Microsoft y conservo solo la edición Professional. Home, Education y las demás ediciones no están incluidas.",
  o1="Completa", o1_t="Sistema totalmente funcional con Office, Chrome y 7-Zip.",
  o2="Programas básicos", o2_t="Windows Pro con los programas esenciales.",
  o3="Vanilla", o3_t="Solo la imagen de Windows Pro de Microsoft, sin nada añadido.",
  notes_h="Antes de instalar",
  n1="El idioma de la ISO es siempre inglés (en-US). Puedes añadir tu idioma después de instalar, en Configuración &gt; Hora e idioma. Pronto habrá una guía paso a paso.",
  n2="No uses las opciones de Rufus para saltarte la comprobación de hardware.",
  n3="La instalación inicia sesión automáticamente como Administrador local. Para evitarlo, borra <code>autounattend.xml</code> de la raíz de la ISO.",
  n4="Las instalaciones All-in-one necesitan internet (Office y Chrome se descargan durante la instalación). Las imágenes preinstaladas funcionan sin conexión.",
  n5='¿Solo necesitas Office? Usa el <a href="https://office.pcninja.pro/">Office Smart Installer</a>.',
  older_h="Versiones anteriores", th_ver="Versión", th_type="Tipo", th_size="Tamaño", dl="Descargar",
  f_home="Inicio PcNinja", f_help="Soporte remoto", f_office="Instalador de Office", f_gh="GitHub"),
 "he": dict(
  title="קבצי ISO של Windows - PcNinja",
  desc="קבצי ISO נקיים של Windows 11 Pro מבית PcNinja. בכל ISO יש שלוש אפשרויות התקנה: מלאה, תוכנות בסיסיות או Vanilla.",
  nav_home="PcNinja", nav_help="תמיכה מרחוק", nav_office="מתקין Office",
  latest="הגרסה האחרונה", lang_line="אנגלית", size="גודל", update="עדכון אופליין: מרץ 2026", dl_iso="הורדת ISO",
  aio="All-in-one · דורש אינטרנט", pre="מותקן מראש · עובד בלי אינטרנט", two="2 אפשרויות התקנה",
  opts_h="בכל ISO יש אותן שלוש אפשרויות התקנה", option="אפשרות", pro="מהדורת Pro בלבד",
  intro="כל Build שלי מתחיל מה-Image הרשמי של Microsoft, ואני משאיר בו רק את מהדורת Professional. מהדורות Home, Education ושאר המהדורות לא כלולות.",
  o1="מלאה", o1_t="מערכת עובדת לגמרי עם Office, 7-Zip ו-Chrome.",
  o2="תוכנות בסיסיות", o2_t="Windows Pro עם התוכנות החיוניות.",
  o3="Vanilla", o3_t="רק ה-Image של Windows Pro מ-Microsoft, בלי שום תוספת.",
  notes_h="לפני ההתקנה",
  n1="שפת ה-ISO היא תמיד אנגלית (en-US). אפשר להוסיף את השפה שלכם אחרי ההתקנה, בהגדרות &gt; שעה ושפה. מדריך מפורט בדרך.",
  n2="אל תשתמשו באפשרויות של Rufus לעקיפת בדיקות החומרה.",
  n3="ההתקנה נכנסת אוטומטית למשתמש Administrator המקומי. כדי לבטל את זה, מחקו את <code>autounattend.xml</code> מתיקיית השורש של ה-ISO.",
  n4="התקנות All-in-one צריכות אינטרנט (Office ו-Chrome יורדים במהלך ההתקנה). תמונות שמותקנות מראש עובדות בלי אינטרנט.",
  n5='צריכים רק Office? השתמשו ב-<a href="https://office.pcninja.pro/">Office Smart Installer</a>.',
  older_h="גרסאות קודמות", th_ver="גרסה", th_type="סוג", th_size="גודל", dl="הורדה",
  f_home="PcNinja - דף הבית", f_help="תמיכה מרחוק", f_office="מתקין Office", f_gh="GitHub"),
}
LANGS = [  # code, path, dir, label, help site
    ("en", "/", "ltr", "EN", "https://help.pcninja.pro/en/", "https://www.pcninja.pro/"),
    ("es", "/es/", "ltr", "ES", "https://help.pcninja.pro/es/", "https://www.pcninja.pro/es/"),
    ("he", "/he/", "rtl", "עב", "https://help.pcninja.pro/", "https://www.pcninja.pro/he/"),
]
PATHS = {c: p for c, p, *_ in LANGS}

# Only the home address "/" redirects: to the language picked with the buttons
# (remembered in this browser), else to the browser's language (es / he), else English.
LANG_JS = """(function(){var P=%s,K='pcninja-lang',s=null,q=/[?&]lang=(en|es|he)\\b/.exec(location.search);
try{if(q){localStorage.setItem(K,q[1]);}s=localStorage.getItem(K);}catch(e){}
if(q){history.replaceState(null,'',location.pathname+location.hash);return;}
if(location.pathname!=='/')return;
if(!s){var L=navigator.languages||[navigator.language||''];for(var i=0;i<L.length;i++){var c=String(L[i]).slice(0,2).toLowerCase();if(c==='iw')c='he';if(P[c]){s=c;break;}}}
if(s&&s!=='en'&&P[s])location.replace(P[s]+location.hash);})();""" % (
    "{" + ",".join("%s:'%s'" % (c, p) for c, p in PATHS.items()) + "}")

PAGE = """<!doctype html>
<html lang="{lang}" dir="{dir}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{site}{path}">
{alternates}
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{site}{path}">
  <meta property="og:image" content="https://www.pcninja.pro/assets/logo-512.png">
  <meta name="theme-color" content="#012456">
  <link rel="icon" type="image/png" href="/assets/favicon.png">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Assistant:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/site.css">
  <script>{langjs}</script>
</head>
<body>
  <header class="topbar">
    <div class="wrap">
      <a class="brand" href="{path}"><img src="/assets/logo.png" alt="" width="40" height="40"><span>Win11 Pc Ninja</span></a>
      <div class="menus">
        <ul class="nav">
          <li><a href="{www}">{nav_home}</a></li>
          <li><a href="{help}">{nav_help}</a></li>
          <li><a href="https://office.pcninja.pro/">{nav_office}</a></li>
        </ul>
{langs}
      </div>
    </div>
  </header>

  <main>
    <div class="latest">
      <div class="wrap">
        <span class="tag">{latest}</span>
        <h1>{l_ver}</h1>
        <ul class="meta">
          <li>{lang_line}</li>
          <li>{pro}</li>
          <li>{l_type}</li>
          <li>{size} <b class="num" dir="ltr">{l_size}</b></li>
          <li>{update}</li>
        </ul>
        <a class="btn btn-primary" href="{l_url}">{dl_iso}</a>
      </div>
    </div>

    <section>
      <div class="wrap">
        <h2 class="h2">{opts_h}</h2>
        <p class="intro">{intro}</p>
        <ol class="opts">
          <li class="opt"><span class="k">{option} 1</span><h3>{o1}</h3><p>{o1_t}</p></li>
          <li class="opt"><span class="k">{option} 2</span><h3>{o2}</h3><p>{o2_t}</p></li>
          <li class="opt"><span class="k">{option} 3</span><h3>{o3}</h3><p>{o3_t}</p></li>
        </ol>
      </div>
    </section>

    <section>
      <div class="wrap">
        <div class="note">
          <h2>{notes_h}</h2>
          <ul>
            <li>{n1}</li>
            <li>{n2}</li>
            <li>{n3}</li>
            <li>{n4}</li>
            <li>{n5}</li>
          </ul>
        </div>
      </div>
    </section>

    <section>
      <div class="wrap">
        <h2 class="h2">{older_h}</h2>
        <div class="tbl">
          <table>
            <thead><tr><th>{th_ver}</th><th>{th_type}</th><th class="size">{th_size}</th><th><span hidden>{dl}</span></th></tr></thead>
            <tbody>
{rows}
            </tbody>
          </table>
        </div>
      </div>
    </section>
  </main>

  <footer class="site-footer">
    <div class="wrap">
      <span>Win11 Pc Ninja</span>
      <ul>
        <li><a href="{www}">{f_home}</a></li>
        <li><a href="{help}">{f_help}</a></li>
        <li><a href="https://office.pcninja.pro/">{f_office}</a></li>
        <li><a href="https://github.com/JavierTorresFelendler">{f_gh}</a></li>
      </ul>
    </div>
  </footer>
</body>
</html>
"""

def main():
    alternates = "\n".join('  <link rel="alternate" hreflang="%s" href="%s%s">' % (c, SITE, p) for c, p in PATHS.items())
    alternates += '\n  <link rel="alternate" hreflang="x-default" href="%s/">' % SITE
    for code, path, d, _label, help_url, www in LANGS:
        t = T[code]
        langs = '        <ul class="langs" aria-label="Language">' + "".join(
            '<li><a href="%s?lang=%s" hreflang="%s" lang="%s"%s>%s</a></li>' % (
                p, c, c, c, ' aria-current="true"' if c == code else "", lb)
            for c, p, _d, lb, *_ in LANGS) + "</ul>"
        rows = "\n".join(
            '              <tr><td class="ver">%s</td><td class="type">%s</td><td class="size num">%s</td>'
            '<td class="dl"><a class="btn btn-line" href="%s">%s</a></td></tr>' % (v, t[ty], sz, url, t["dl"])
            for v, ty, sz, url in OLDER)
        html = PAGE.format(lang=code, dir=d, path=path, site=SITE, alternates=alternates, langjs=LANG_JS,
                           langs=langs, help=help_url, www=www, rows=rows,
                           l_ver=LATEST["ver"], l_type=t[LATEST["type"]], l_size=LATEST["size"], l_url=LATEST["url"], **t)
        dest = os.path.join(ROOT, path.strip("/"), "index.html")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w", encoding="utf-8", newline="\n").write(html)
        print("wrote", os.path.relpath(dest, ROOT))
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for p in PATHS.values():
            f.write("  <url><loc>%s%s</loc></url>\n" % (SITE, p))
        f.write("</urlset>\n")

if __name__ == "__main__":
    main()
