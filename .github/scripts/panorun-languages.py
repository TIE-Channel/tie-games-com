"""tie-games.com/panorun in Panorun's twelve languages (the player's request,
2026-10-28): writes panorun/<language>/index.html from the English page,
panorun/index.html, each block of it said in that language
(.github/scripts/panorun_languages/<language>.py), and puts the language
menu - a globe and the language's name, the twelve under it - into every
page, English too, with the pages' links to each other for search engines.

    py -3.11 .github/scripts/panorun-languages.py

Run it whenever the English page changes - each release, after its download
buttons are written: what the English page says that a language has no
words for stays English there, and is listed. The Privacy Policy and the
Terms stay English."""

from __future__ import annotations

import importlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(os.path.dirname(HERE))
ENGLISH = os.path.join(SITE, "panorun", "index.html")
URL = "https://tie-games.com/panorun/"

sys.path.insert(0, HERE)

#: The languages: (folder, BCP 47 tag, own name, module), English first.
LANGUAGES = (
    ("", "en", "English", None),
    ("es", "es", "Español", "es"),
    ("de", "de", "Deutsch", "de"),
    ("fr", "fr", "Français", "fr"),
    ("pt-br", "pt-BR", "Português (Brasil)", "pt_br"),
    ("ru", "ru", "Русский", "ru"),
    ("ja", "ja", "日本語", "ja"),
    ("ko", "ko", "한국어", "ko"),
    ("zh", "zh-Hans", "简体中文", "zh"),
    ("hi", "hi", "हिन्दी", "hi"),
    ("id", "id", "Bahasa Indonesia", "id"),
    ("ar", "ar", "العربية", "ar"),
)

MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December")

MENU_START, MENU_END = "<!-- languages -->", "<!-- /languages -->"
LINKS_START, LINKS_END = "<!-- language links -->", "<!-- /language links -->"
STYLE_START, STYLE_END = "/* languages */", "/* /languages */"

STYLE = """  /* languages */
  .languages { position: relative; font-family: 'Courier New', monospace; font-size: 12px; font-weight: 700; letter-spacing: 0.05em; }
  .languages summary { cursor: pointer; list-style: none; display: flex; align-items: center; gap: 6px; }
  .languages summary::-webkit-details-marker { display: none; }
  .languages summary svg { width: 16px; height: 16px; }
  .languages ul { position: absolute; right: 0; top: 24px; background: #fff; border: 2px solid #1a1a1a; list-style: none; padding: 6px 0; margin: 0; z-index: 20; min-width: 200px; }
  [dir="rtl"] .languages ul { right: auto; left: 0; }
  .languages li { margin: 0; }
  .languages li a { display: block; padding: 4px 14px; border: none; color: #1a1a1a; font-family: 'Helvetica Neue', Arial, sans-serif; font-size: 14px; letter-spacing: 0; font-weight: 400; }
  .languages li a:hover { background: #b50026; color: #fff; }
  .languages li a.here { color: #b50026; font-weight: 700; }
  [dir="rtl"] h1, [dir="rtl"] h2, [dir="rtl"] .platform, [dir="rtl"] .button,
  [dir="rtl"] .back-link, [dir="rtl"] .play-badge-line2 { letter-spacing: 0;
    font-family: 'Helvetica Neue', Arial, sans-serif; }
  [dir="rtl"] ul, [dir="rtl"] ol { padding-left: 0; padding-right: 24px; }
  [dir="rtl"] .links { padding-right: 0; }
  [dir="rtl"] .note, [dir="rtl"] .download .test, [dir="rtl"] .download .next {
    border-left: none; border-right: 4px solid #b50026; }
  /* /languages */
"""

#: The header's way back to tie-games.com, in each language.
BACK = {"es": "Volver", "de": "Zurück", "fr": "Retour", "pt-br": "Voltar", "ru": "Назад",
        "ja": "戻る", "ko": "뒤로", "zh": "返回", "hi": "वापस", "id": "Kembali", "ar": "رجوع"}

GLOBE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">'
         '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15 15 0 0 1 0 20M12 2a15 15 0 0 0 0 20"/></svg>')


def folder_url(folder):
    return URL + (folder + "/" if folder else "")


def menu(current):
    """The header's language menu, `current` (a folder) marked."""
    items = []
    for folder, tag, name, _module in LANGUAGES:
        here = ' class="here"' if folder == current else ""
        items.append(f'<li><a href="/panorun/{folder + "/" if folder else ""}" hreflang="{tag}" lang="{tag}"'
                     f' data-language="{folder or "en"}"{here}>{name}</a></li>')
    name = dict((f, n) for f, _t, n, _m in LANGUAGES)[current]
    return (f"{MENU_START}\n    <details class=\"languages\"><summary>{GLOBE}<span>{name}</span></summary>"
            f"<ul>{''.join(items)}</ul></details>\n    {MENU_END}")


def alternates():
    lines = [f'<link rel="alternate" hreflang="{tag}" href="{folder_url(folder)}">'
             for folder, tag, _name, _module in LANGUAGES]
    lines.append(f'<link rel="alternate" hreflang="x-default" href="{URL}">')
    return LINKS_START + "\n" + "\n".join(lines) + "\n" + LINKS_END


#: The English page's own script: a first visit in a browser of another of
#: the languages goes to its page, once; a language chosen in the menu is
#: remembered and taken.
CHOOSER = """<script>
// The visitor's language (.github/scripts/panorun-languages.py): a language
// chosen in the menu is kept; else, the first time, the browser's.
(function () {
  var pages = { es: 'es', de: 'de', fr: 'fr', pt: 'pt-br', ru: 'ru', ja: 'ja', ko: 'ko', zh: 'zh', hi: 'hi', id: 'id', 'in': 'id', ar: 'ar' };
  document.addEventListener('click', function (e) {
    var link = e.target.closest && e.target.closest('[data-language]');
    if (link) { try { localStorage.setItem('panorun-language', link.getAttribute('data-language')); } catch (err) {} }
  });
  if (document.documentElement.lang !== 'en') return;
  var chosen = null;
  try { chosen = localStorage.getItem('panorun-language'); } catch (err) {}
  if (chosen === null) {
    var tag = ((navigator.languages && navigator.languages[0]) || navigator.language || '').toLowerCase();
    chosen = pages[tag.split('-')[0]] || null;
  }
  if (chosen && chosen !== 'en' && /\\/panorun\\/?$/.test(location.pathname)) {
    location.replace('/panorun/' + chosen + '/' + location.hash);
  }
})();
</script>"""
CHOOSER_START, CHOOSER_END = "<!-- language chooser -->", "<!-- /language chooser -->"


def put_between(text, start, end, block, anchor, before=True):
    """`block` (with its markers) in place of what is between `start` and
    `end`, or put next to `anchor` the first time."""
    if start in text:
        a = text.index(start)
        b = text.index(end, a) + len(end)
        return text[:a] + block + text[b:]
    i = text.index(anchor)
    return text[:i] + block + "\n" + text[i:] if before else text[:i + len(anchor)] + "\n" + block + text[i + len(anchor):]


def common(text, folder):
    """What every page has, English too: the menu, the links, the style."""
    if STYLE_START in text:
        a = text.index("  " + STYLE_START)
        b = text.index(STYLE_END, a) + len(STYLE_END) + 1
        text = text[:a] + STYLE + text[b:]
    else:
        text = text.replace("</style>", STYLE + "</style>", 1)
    text = put_between(text, LINKS_START, LINKS_END, alternates(), "<style>")
    text = put_between(text, MENU_START, MENU_END, menu(folder),
                       '<a href="/" class="back-link">')
    return text


def translate(text, folder, tag, module):
    words = importlib.import_module(f"panorun_languages.{module}")
    missing = []
    out = text.replace('<html lang="en">', f'<html lang="{tag}"' + (' dir="rtl"' if tag == "ar" else "") + ">", 1)
    out = out.replace(CHOOSER_START, "").replace(CHOOSER_END, "")
    if CHOOSER in out:
        out = out.replace(CHOOSER, "")

    # The version's own lines: the buttons, the file lines and their dates.
    def button(match):
        return ">" + words.WORDS[match.group(2).lower()].replace("{version}", match.group(1)) + "<"
    out = re.sub(r">Download Panorun ([\d.]+) for (Windows|Android|Mac|Linux)<", button, out)

    def day(match):
        return words.date(int(match.group(1)), MONTHS.index(match.group(2)) + 1, int(match.group(3)))
    out = re.sub(r"(\d{1,2}) (" + "|".join(MONTHS) + r") (\d{4})", day, out)
    out = out.replace(" &middot; downloads Panorun as it installs it<br>",
                      " &middot; " + words.WORDS["small"] + "<br>")

    def full(match):
        return words.WORDS["full"].replace("{url}", match.group(1)).replace("{size}", match.group(2))
    out = re.sub(r'Or the <a href="([^"]+)">full installer</a> \(([^)]+)\), with everything in it: '
                 r'it installs without a connection\.', full, out)

    # The script's words.
    script_words = ("    windows: '{windows}',\n    android: '{android}',\n    mac: '{mac}',\n"
                    "    linux: '{linux}',\n    small: '{small}',\n"
                    "    full: '{full}',\n    locale: '{locale}'\n").format(
        **{k: v.replace("'", "\\'") for k, v in words.WORDS.items()})
    out = re.sub(r"(  var WORDS = \{\n)(.*?)(  \};)", lambda m: m.group(1) + script_words + m.group(3),
                 out, count=1, flags=re.S)

    # Every block: a paragraph, a list item, a heading, a title - and the
    # meta words, the picture's words.
    # The longest first: a heading's words are a link's too.
    for english, said in sorted(words.BLOCKS.items(), key=lambda kv: -len(kv[0])):
        hits = 0
        for before, after in ((">", "</"), ('content="', '"'), ('alt="', '"'), ('aria-label="', '"')):
            key = before + english + after
            if key in out:
                hits += out.count(key)
                out = out.replace(key, before + said + after)
        if not hits:
            missing.append(english)
    arrow = "&rarr;" if tag == "ar" else "&larr;"
    out = out.replace('class="back-link">&larr; Back</a>', f'class="back-link">{arrow} {BACK[folder]}</a>')
    # The page's own address: the canonical, og:url, Open in Chrome.
    out = out.replace(f'href="{URL}">', f'href="{folder_url(folder)}">').replace(
        f'content="{URL}">', f'content="{folder_url(folder)}">')
    left = []
    for m in re.finditer(r"<(title|h1|h2|p|li)(?:\s[^>]*)?>(.*?)</\1>", out, re.S):
        inner = m.group(2).strip()
        # What Windows itself says (<em>) may stay as Windows says it.
        plain = re.sub(r"<em>.*?</em>|<[^>]+>|&\w+;|&#\d+;", " ", inner)
        if inner in words.BLOCKS or not re.search(r"\b(the|and|you|your|is|of|to)\b", plain):
            continue
        left.append(inner[:70])
    return out, missing, left


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    with open(ENGLISH, encoding="utf-8") as handle:
        english = handle.read()
    english = common(english, "")
    if CHOOSER_START not in english:
        english = english.replace("</body>", CHOOSER_START + "\n" + CHOOSER + "\n" + CHOOSER_END + "\n</body>", 1)
    with open(ENGLISH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(english)
    for folder, tag, name, module in LANGUAGES[1:]:
        page, missing, left = translate(english, folder, tag, module)
        page = common(page, folder)
        os.makedirs(os.path.join(SITE, "panorun", folder), exist_ok=True)
        with open(os.path.join(SITE, "panorun", folder, "index.html"), "w", encoding="utf-8",
                  newline="\n") as handle:
            handle.write(page)
        note = ""
        if missing:
            note += f"  no longer on the English page: {[m[:50] for m in missing]}"
        if left:
            note += f"  still English: {left}"
        print(f"{folder}: {name}{note}")


if __name__ == "__main__":
    main()
