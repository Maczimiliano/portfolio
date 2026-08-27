# Builds portfolio-web/index.html: a simple, minimalist, media-first portfolio
# showing real embedded videos and images instead of links.

VIDEOS = [
    # (file, client, caption, featured)
    ("arm-own-mountain.mp4", "American Resort Partners", "Own the mountain", True),
    ("gree-w2.mp4", "Greenlite Holdings", "Weekly investor update, batch 2", True),
    ("gree-broader-access.mp4", "Greenlite Holdings", "Broader access, same brand engine", True),
    ("fr-video1.mp4", "Client FR", "Vertical brand film", False),
    ("rc-video2.mp4", "Roll Craft", "Vertical brand video, cut 2", False),
    ("awe-already-standing.mp4", "Ethos Baja", "Already standing, built on real footage", False),
    ("awe-own-it.mp4", "Ethos Baja", "Own it, the perk-led angle", False),
    ("roxg-v2.mp4", "RoxStart AI Logistics (RoxVault)", "Lead-gen film, cut 2", False),
    ("roxg-v1.mp4", "RoxStart AI Logistics (RoxVault)", "Lead-gen film, cut 1", False),
    ("spo-v2.mp4", "Spongelle", "Vertical ad, cut 2", False),
    ("glo-v1.mp4", "GLO by Gabbi", "Investor webinar cut", False),
    ("pye-v2.mp4", "Pytheas Energy", "Investor film, cut 2", False),
    ("pye-ai-finds-20s.mp4", "Pytheas Energy", "20-second cut: AI Finds / We Buy / You Invest", False),
    ("rox-webinarvid2.mp4", "RoxStart AI Logistics", "Investor webinar ad, cut 2", False),
]

# One flowing sequence, not grouped by brand. Ordered from strongest to weakest,
# per Mateo's picks: Spongelle 3 named first, GLO's 3 best next, Ethos Baja
# clustered around the middle, then all of Pytheas as a block, then the rest.
ALL_IMAGES = [
    ("spo-ad1.png", "Spongelle", "Static ad", True),
    ("spo-retargeting-11.png", "Spongelle", "Retargeting ad", True),
    ("spo-retargeting-5.png", "Spongelle", "Retargeting ad", True),
    ("glo-ad6.png", "GLO by Gabbi", "Static ad", True),
    ("glo-brand-deal.png", "GLO by Gabbi", "Brand-deal angle ad", True),
    ("glo-ad3.png", "GLO by Gabbi", "Static ad", True),
    ("roxlg-43.png", "RoxStart AI Logistics (RoxVault)", "Static ad", True),
    ("roxlg-scene.png", "RoxStart AI Logistics (RoxVault)", "AI-generated product scene", True),
    ("glo-webinar.png", "GLO by Gabbi", "Webinar promo ad", True),
    ("roxlg-extra.png", "RoxStart AI Logistics (RoxVault)", "Static ad", False),
    ("awe-get-in-first.png", "Ethos Baja", "Get in first: the timing angle", False),
    ("awe-own-your-rest.png", "Ethos Baja", "Own your rest: the perk-led angle", False),
    ("awe-the-wave.png", "Ethos Baja", "The wave: market size framed as an invitation", False),
    ("awe-napa-of-mexico.png", "Ethos Baja", "Napa of Mexico: place as the proof", False),
    ("awe-already-standing.png", "Ethos Baja", "Already standing", False),
    ("awe-the-window.png", "Ethos Baja", "The window", False),
    ("awe-use-it.png", "Ethos Baja", "Use it", False),
    ("pye-ad5.png", "Pytheas Energy", "Static ad, 1:1", True),
    ("pye-ad6.png", "Pytheas Energy", "Static ad, 1:1", False),
    ("pye-ad5-2.png", "Pytheas Energy", "Static ad, 9:16 cut", False),
    ("pye-ad5-4.png", "Pytheas Energy", "Static ad, 9:16 cut", False),
    ("roxlg-41-safe-carrier.png", "RoxStart AI Logistics (RoxVault)", "The equalizer: small brokers against the giants' compliance department", False),
    ("roxlg-42-shippers-proof.png", "RoxStart AI Logistics (RoxVault)", "Win more freight: the untested growth angle", False),
    ("glo-editing-campaign.png", "GLO by Gabbi", "Campaign ad", False),
    ("spo-scene.png", "Spongelle", "AI-generated product scene", False),
    ("spo-webinar-ad5.png", "Spongelle", "Webinar promo ad", False),
    ("spo-webinar-ad1.png", "Spongelle", "Webinar promo ad", False),
    ("spo-op5-b3.png", "Spongelle", "Static ad", False),
]

EARLY = [
    dict(name="helloCash", sub="Brand videos, AI production",
         files=[dict(f="hellocash-1.mp4"), dict(f="hellocash-2.mp4"), dict(f="hellocash-3.mp4")],
         note="AI-produced brand videos for a digital-wallet product."),
    dict(name="helloVEA", sub="Sub-brand videos",
         files=[dict(f="hellovea-1.mp4"), dict(f="hellovea-2.mp4", aspect="16:9")],
         note="Sub-brand video work under the same product family."),
    dict(name="Hudbay Perú: Ping Pong", sub="Internal communications campaign",
         files=[dict(f="hudbay-1.mp4", aspect="16:9"), dict(f="hudbay-2.mp4", aspect="16:9")],
         note="Internal video series created for a multinational mining company, to humanize corporate culture across a distributed workforce, part of a culture and recognition programme that lifted internal engagement by 30%."),
    dict(name="Suplemento Funcional", sub="Entrepreneurship, product video",
         files=[dict(f="suplemento-1.mp4")],
         note="Product video for an independent functional-supplement venture."),
    dict(name="Mcz Workout", sub="Wellness project, Instagram Reels",
         files=[dict(f="mcz-1.mp4", link="https://www.instagram.com/reel/ClVFUeZj9Ck/"),
                dict(f="mcz-2.mp4", link="https://www.instagram.com/reel/Cdj6cvWD3To/")],
         note="Personal wellness project: sport, health and fitness content."),
    dict(name="La Casa del Gato: Bungalows", sub="Brand identity",
         files=[],
         note="Full identity for a coastal bungalow brand: mark, wordmark and a five-colour system built to survive signage, social and print. The source file behind the original link is a Canva PDF, not a video, so no media is embedded here per the no-Canva rule."),
    dict(name="UtelStays: listing templates", sub="Social template system",
         files=[],
         note="A locked grid, type scale and colour system that let a non-designer publish on-brand property posts daily. The source file behind the original link is a Canva PDF, not a video, so no media is embedded here per the no-Canva rule."),
]

def video_card(file, client, caption, group="grohak"):
    src = f"media/{group}/videos/{file}"
    return f"""
      <figure class="vcard">
        <video src="{src}" controls preload="metadata" playsinline></video>
        <figcaption><b>{client}</b><span>{caption}</span></figcaption>
      </figure>"""

def early_video_card(item, group_dir):
    file = item["f"]
    aspect = item.get("aspect", "9:16")
    link = item.get("link")
    src = f"media/early/{group_dir}/{file}"
    cls = "vcard small landscape" if aspect == "16:9" else "vcard small"
    if link:
        cls += " linked"
    ar = "16/9" if aspect == "16:9" else "9/16"
    linkhtml = f'<figcaption><a href="{link}" target="_blank" rel="noopener">View on Instagram &#8599;</a></figcaption>' if link else ""
    return f"""
      <figure class="{cls}">
        <video src="{src}" controls preload="metadata" playsinline style="aspect-ratio:{ar}"></video>{linkhtml}
      </figure>"""

def image_card(file, client, caption, featured):
    src = f"media/grohak/images/{file}"
    cls = "icard featured" if featured else "icard"
    return f"""
      <figure class="{cls}">
        <img src="{src}" alt="" loading="lazy">
        <figcaption><b>{client}</b><span>{caption}</span></figcaption>
      </figure>"""

featured_videos = [v for v in VIDEOS if v[3]]
rest_videos = [v for v in VIDEOS if not v[3]]

hero_videos_html = "\n".join(video_card(f, c, cap) for f, c, cap, feat in featured_videos)
rest_videos_html = "\n".join(video_card(f, c, cap) for f, c, cap, feat in rest_videos)

image_grid_html = "\n".join(image_card(f, client, cap, feat) for f, client, cap, feat in ALL_IMAGES)

early_html = ""
early_dirs = {
    "helloCash": "hellocash", "helloVEA": "hellovea", "Hudbay Perú: Ping Pong": "hudbay",
    "Suplemento Funcional": "suplemento", "Mcz Workout": "mczworkout",
    "La Casa del Gato: Bungalows": "casa-del-gato", "UtelStays: listing templates": "utel",
}
for item in EARLY:
    gdir = early_dirs[item["name"]]
    cards = "\n".join(early_video_card(f, gdir) for f in item["files"])
    mediahtml = f'<div class="vgrid small">{cards}\n      </div>' if item["files"] else ""
    early_html += f"""
    <div class="egroup">
      <div class="ehead">
        <h3>{item['name']}</h3>
        <span class="esub">{item['sub']}</span>
        <p>{item['note']}</p>
      </div>
      {mediahtml}
    </div>"""

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Mateo Calderón · Portfolio</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {{
    --bg: #FAFAF8;
    --panel: #FFFFFF;
    --ink: #14151A;
    --muted: #6B6D76;
    --line: #E7E5E0;
    --accent: #1B75BB;
  }}
  * {{ box-sizing: border-box; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    margin: 0; background: var(--bg); color: var(--ink);
    font-family: -apple-system, "Segoe UI", Helvetica, Arial, sans-serif;
    line-height: 1.5;
  }}
  a {{ color: var(--accent); }}
  .wrap {{ max-width: 1180px; margin: 0 auto; padding: 0 28px; }}

  header.top {{
    position: sticky; top: 0; z-index: 20; background: rgba(250,250,248,.92);
    backdrop-filter: blur(6px); border-bottom: 1px solid var(--line);
  }}
  .topbar {{ display: flex; align-items: center; justify-content: space-between; padding: 14px 0; }}
  .brand {{ display: flex; align-items: center; gap: 10px; font-weight: 600; letter-spacing: .2px; }}
  .brand img {{ height: 26px; width: auto; }}
  nav a {{ color: var(--ink); text-decoration: none; margin-left: 22px; font-size: 14px; }}
  nav a:hover {{ color: var(--accent); }}

  .hero {{ padding: 64px 0 40px; }}
  .kick {{ text-transform: uppercase; letter-spacing: 1.5px; font-size: 12px; color: var(--muted); font-weight: 600; }}
  h1.title {{ font-size: 42px; margin: 10px 0 14px; letter-spacing: -.5px; }}
  .lede {{ max-width: 680px; color: #33343B; font-size: 17px; }}
  .contact {{ margin-top: 20px; font-size: 14px; color: var(--muted); }}
  .contact span {{ margin-right: 18px; }}

  section {{ padding: 52px 0; border-top: 1px solid var(--line); }}
  .shead {{ display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 26px; flex-wrap: wrap; gap: 8px; }}
  .shead h2 {{ font-size: 24px; margin: 0; }}
  .shead p {{ margin: 0; color: var(--muted); font-size: 14px; max-width: 460px; }}

  .vgrid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 18px; }}
  .vgrid.hero-grid {{ grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); }}
  .vgrid.small {{ grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); }}

  .vcard {{ margin: 0; background: var(--panel); border: 1px solid var(--line); border-radius: 10px; overflow: hidden; }}
  .vcard video {{ width: 100%; aspect-ratio: 9/16; object-fit: cover; background: #000; display: block; }}
  .vcard figcaption {{ padding: 10px 12px; font-size: 13px; }}
  .vcard figcaption b {{ display: block; font-size: 12.5px; }}
  .vcard figcaption span {{ color: var(--muted); font-size: 12px; }}
  .vcard.small figcaption {{ display: none; }}
  .vcard.small.landscape figcaption, .vcard.small.linked figcaption {{ display: block; padding: 8px 10px; }}
  .vcard.small.landscape figcaption a, .vcard.small.linked figcaption a {{ font-size: 12px; text-decoration: none; }}
  .vgrid.small .vcard.landscape {{ grid-column: span 2; }}

  .igrid {{ column-count: 4; column-gap: 14px; }}
  .icard {{ margin: 0 0 14px; break-inside: avoid; background: var(--panel); border: 1px solid var(--line); border-radius: 8px; overflow: hidden; }}
  .icard img {{ width: 100%; display: block; }}
  .icard figcaption {{ padding: 8px 10px; font-size: 11.5px; }}
  .icard figcaption b {{ display: block; font-size: 11px; }}
  .icard figcaption span {{ color: var(--muted); font-size: 11px; }}
  .icard.featured {{ border-color: var(--accent); }}

  .egroup {{ margin-bottom: 36px; }}
  .ehead h3 {{ font-size: 16px; margin: 0 0 2px; }}
  .ehead .esub {{ font-size: 12px; color: var(--accent); font-weight: 600; }}
  .ehead p {{ margin: 6px 0 14px; color: var(--muted); font-size: 13.5px; max-width: 640px; }}

  footer {{ padding: 56px 0 70px; border-top: 1px solid var(--line); }}
  footer h2 {{ font-size: 26px; margin: 0 0 16px; }}
  .ctgrid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px,1fr)); gap: 16px; margin-top: 24px; font-size: 14px; }}
  .ctgrid dt {{ color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: .5px; }}
  .ctgrid dd {{ margin: 4px 0 0; }}

  @media (max-width: 720px) {{
    .igrid {{ column-count: 2; }}
    h1.title {{ font-size: 30px; }}
  }}
</style>
</head>
<body>

<header class="top">
  <div class="wrap topbar">
    <div class="brand"><img src="assets/mc-mark.png" alt="MC"> Mateo Calderón</div>
    <nav>
      <a href="#video">Video</a>
      <a href="#campaigns">Campaigns</a>
      <a href="#early">Earlier work</a>
      <a href="#contact">Contact</a>
    </nav>
  </div>
</header>

<div class="hero wrap">
  <div class="kick">Selected work · 2026</div>
  <h1 class="title">I build the ads, videos and copy that convert.</h1>
  <p class="lede">Growth Creative Specialist: conversion-driven ad design, short-form vertical and landscape video,
    scripts and copy, for a range of client brands. This page embeds the actual deliverables, videos and
    images, so you can watch and see the work directly.</p>
  <div class="contact">
    <span>Growth Creative Specialist</span>
    <span>Lima, Peru · Remote</span>
    <span>mateo_cz@hotmail.com</span>
    <span>linkedin.com/in/mateocz</span>
  </div>
</div>

<section id="video" class="wrap">
  <div class="shead">
    <h2>Grohak Agency · Video</h2>
    <p>Script to export: hooks, AI scene generation, edit, burned-in captions, brand end-cards.</p>
  </div>
  <div class="vgrid hero-grid">{hero_videos_html}
  </div>
  <div class="vgrid" style="margin-top:18px">{rest_videos_html}
  </div>
</section>

<section id="campaigns" class="wrap">
  <div class="shead">
    <h2>Grohak Agency · Ad campaigns</h2>
    <p>Static ads for Meta, one fixed spine and one variable per batch.</p>
  </div>
  <div class="igrid">{image_grid_html}
  </div>
</section>

<section id="early" class="wrap">
  <div class="shead">
    <h2>Earlier work</h2>
    <p>Brand video, internal comms and identity work from before Grohak Agency.</p>
  </div>
  {early_html}
</section>

<footer id="contact" class="wrap">
  <h2>Let's make the next one convert.</h2>
  <p style="color:var(--muted);max-width:560px">Full campaign files, scripts and edit notes behind any piece
    shown here are available on request.</p>
  <dl class="ctgrid">
    <div><dt>Email</dt><dd>mateo_cz@hotmail.com</dd></div>
    <div><dt>Phone</dt><dd>+51 931 949 380</dd></div>
    <div><dt>LinkedIn</dt><dd>/in/mateocz</dd></div>
    <div><dt>Based in</dt><dd>Lima, Peru · Remote</dd></div>
  </dl>
</footer>

</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(HTML)
print("wrote index.html,", len(HTML), "bytes")
