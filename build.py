#!/usr/bin/env python3
"""Generates the static pages for the Shetty Infraventures website.

Edit the CONFIG and PROJECTS sections below, then run:  python3 build.py
No dependencies. Output: index.html, projects.html, about.html, contact.html,
and one page per project inside /projects/.
"""
import os
from html import escape as esc

ROOT = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ CONFIG
SITE = {
    "name": "Shetty Infraventures",
    "tagline": "Architecture, interiors & construction",
    "email": "Siddharth.shetty0@gmail.com",
    "phones": [("+91 90609 49999", "+919060949999"), ("+61 450 099 527", "+61450099527")],
    "whatsapp": "919060949999",
    "instagram": "https://www.instagram.com/shettyinfraventures/",
    "address": "",            # add studio address text when ready
    "maps": "https://maps.app.goo.gl/HRz9M48eS24KtbBNA",
    "year": 2026,
}

SERVICES = [
    ("Architecture", "Concept to construction drawings for homes and institutions, shaped around climate, light and the way people actually live."),
    ("Interior Design", "Complete interiors, from layouts and joinery to lighting, finishes and styling, detailed to be built well."),
    ("Building & Construction", "In-house execution that keeps the design intent intact, with clear scheduling and site supervision."),
    ("Space Planning", "Practical, efficient plans for residential, workplace and institutional spaces."),
    ("Real Estate", "Guidance on land and property, supported by design and build expertise under one roof."),
]

PROCESS = [
    ("Consult", "We listen first: your goals, site, budget and timeline."),
    ("Concept", "Layouts, mood and material direction, presented for your feedback."),
    ("Develop", "Detailed drawings, specifications and 3D renders before anything is built."),
    ("Build", "Careful execution with regular site visits and quality checks."),
    ("Handover", "Final styling, snagging and a space that is ready to live in."),
]

# cover = image used on cards / hero. Add more fields (year, location, area, client) to show them as facts.
PROJECTS = [
    dict(slug="sgi-canteen", folder="canteen", title="SGI Canteen", cat="Institutional", n=17, cover=5,
         tag="Where nature breathes, air flows, and the table becomes the heart of design.",
         text=["An open, semi-covered dining space organised around mature trees and terracotta jaali screens. Light and air move freely through the pattern, throwing soft, shifting shadows across the day.",
               "Patterned floor tiles, warm earthy tones and generous planting keep the space grounded and honest. It is a canteen designed to feel like a courtyard."],
         notes=["Spaces that breathe", "Textures that tell stories"],
         facts=[("Type", "Institutional"), ("Scope", "Interior design")]),
    dict(slug="sgi-auditorium", folder="auditorium", title="SGI Auditorium", cat="Institutional", n=11, cover=2,
         tag="Spaces designed for sound. Where audience and stage unite.",
         text=["A tiered auditorium where architecture does the work of acoustics. Soft wall panels wrap the room, while concealed warm LED coves trace the walls and ceiling in lines of light.",
               "The curved seating focuses attention on the stage, and a restrained palette of charcoal and sand keeps the room quiet, so the performance takes centre stage."],
         notes=["Where audience and stage unite"],
         facts=[("Type", "Institutional"), ("Scope", "Interior design")]),
    dict(slug="sgi-office-cabin", folder="office-cabin", title="SGI Office Cabin", cat="Institutional", n=11, cover=4,
         tag="Spaces of solitude. Shelter shaped by simplicity.",
         text=["A workspace that feels more like a retreat. Raw timber, a geometric lattice partition and bamboo-textured panels bring warmth and a sense of calm to a working day.",
               "Soft, layered light and a few well-chosen plants complete a room that celebrates simplicity and focus."],
         notes=["Spaces of solitude", "Shelter shaped by simplicity"],
         facts=[("Type", "Institutional"), ("Scope", "Interior design")]),
    dict(slug="living-room", folder="living-room", title="Living Room", cat="Residential", n=13, cover=3,
         tag="Living beautifully between walls and windows.",
         text=["A living space that balances heritage and calm. Carved wooden seating sits against clean white walls, softened by woven accent chairs, brass details and framed artworks.",
               "A stone-clad niche with a touch of greenery becomes the quiet focal point of the room."],
         notes=[],
         facts=[("Type", "Residential"), ("Scope", "Interior design")]),
    dict(slug="bedroom-sage", folder="sid-bedroom", title="Bedroom · Sage", cat="Residential", n=19, cover=3,
         tag="Soft fabrics, warm wood and muted tones: a haven for calm.",
         text=["A bedroom suite built around a sage-green palette. Fluted wall panels, a floating platform bed and textured plaster create depth without noise.",
               "Concealed linear lighting, a lush dressing-area vignette and sculptural details finish a retreat that feels both calm and considered."],
         notes=[],
         facts=[("Type", "Residential"), ("Scope", "Interior design")]),
    dict(slug="bedroom-noir", folder="bedroom", title="Bedroom · Noir", cat="Residential", n=8, cover=4,
         tag="Designing dreams, one detail at a time.",
         text=["A dramatic bedroom in deep tones, anchored by a tall padded headboard wall and framed by full-height windows with layered drapes.",
               "Patterned panels, warm sconces and curated accents keep the darkness inviting rather than heavy."],
         notes=[],
         facts=[("Type", "Residential"), ("Scope", "Interior design")]),
    dict(slug="bedroom-arches", folder="anirudh-bedroom", title="Bedroom · Arches", cat="Residential", n=10, cover=3,
         tag="Curves, light and a quiet sense of play.",
         text=["A contemporary bedroom with arched, softly lit niches framing a botanical mural, a sculptural curved sofa and a sleek media wall.",
               "Textured grey cladding, layered curtains and a well-organised wardrobe bring structure and comfort together."],
         notes=[],
         facts=[("Type", "Residential"), ("Scope", "Interior design")]),
]

for i, p in enumerate(PROJECTS, 1):
    p["no"] = f"{i:02d}"
    p["thumbs"] = [f"{p['folder']}-{k:02d}.jpg" for k in range(1, p["n"] + 1)]
    p["cover_img"] = p["thumbs"][p["cover"] - 1]


def pby(slug):
    return next(p for p in PROJECTS if p["slug"] == slug)


# ------------------------------------------------------------------ SHARED PARTS
def head(title, desc, depth, og_img="canteen-05.jpg"):
    r = "../" * depth
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{r}images/{og_img}">
<meta name="theme-color" content="#f4f1ec">
<link rel="icon" type="image/png" href="{r}images/favicon.png">
<link rel="apple-touch-icon" href="{r}images/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;1,400&family=Jost:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}css/style.css">
</head>
"""


def nav(depth, current, over=False):
    r = "../" * depth
    def a(href, label, key):
        cur = ' aria-current="page"' if key == current else ""
        return f'<a href="{r}{href}"{cur}>{label}</a>'
    cls = "nav nav--over" if over else "nav nav--solid"
    return f"""<body>
<a class="skip" href="#main">Skip to content</a>
<header class="{cls}">
  <div class="wrap nav__in">
    <a class="brand" href="{r}index.html" aria-label="Shetty Infraventures home"><img src="{r}images/logo.png" alt="" width="38" height="38"><span>Shetty<small>Infraventures</small></span></a>
    <nav class="nav__links" aria-label="Main">
      {a("index.html", "Home", "home")}
      {a("projects.html", "Projects", "projects")}
      {a("about.html", "Studio", "about")}
      <a class="nav__cta" href="{r}contact.html"{' aria-current="page"' if current == "contact" else ""}>Enquire</a>
    </nav>
    <button class="burger" aria-label="Menu" aria-expanded="false"><span></span><span></span></button>
  </div>
</header>
"""


def footer(depth):
    r = "../" * depth
    phones = "".join(f'<li><a href="tel:{t}">{esc(l)}</a></li>' for l, t in SITE["phones"])
    insta = f'<li><a href="{esc(SITE["instagram"])}" target="_blank" rel="noopener">Instagram</a></li>' if SITE["instagram"] else ""
    addr = f'<li>{esc(SITE["address"])}</li>' if SITE["address"] else ""
    if SITE["maps"]:
        addr += f'<li><a href="{esc(SITE["maps"])}" target="_blank" rel="noopener">Find us on Google Maps</a></li>'
    return f"""<footer class="footer">
  <div class="wrap">
    <div class="footer__grid">
      <div>
        <a class="brand" href="{r}index.html"><img src="{r}images/logo.png" alt="" width="54" height="54"><span>Shetty<small>Infraventures</small></span></a>
        <p class="about">Architect · Builder · Interior designer · Real estate · Planner.</p>
      </div>
      <div><h4>Explore</h4><ul><li><a href="{r}projects.html">Projects</a></li><li><a href="{r}about.html">Studio</a></li><li><a href="{r}contact.html">Contact</a></li></ul></div>
      <div><h4>Projects</h4><ul>{"".join(f'<li><a href="{r}projects/{p["slug"]}.html">{esc(p["title"])}</a></li>' for p in PROJECTS[:4])}</ul></div>
      <div><h4>Contact</h4><ul><li><a href="mailto:{esc(SITE["email"])}">{esc(SITE["email"])}</a></li>{phones}{insta}{addr}</ul></div>
    </div>
    <div class="footer__base"><span>© {SITE["year"]} Shetty Infraventures. All rights reserved.</span><span>Design · Build · Inhabit</span></div>
  </div>
</footer>
<script src="{r}js/main.js"></script>
</body>
</html>
"""


def card(p, depth, cls="", sizes="(max-width:760px) 100vw, 50vw"):
    r = "../" * depth
    return f"""<a class="card {cls} rv" href="{r}projects/{p["slug"]}.html" data-cat="{p["cat"]}">
  <div class="card__img"><span class="card__no">{p["no"]}</span><img src="{r}images/thumbs/{p["cover_img"]}" alt="{esc(p["title"])} by Shetty Infraventures" loading="lazy" sizes="{sizes}"></div>
  <div class="card__cap"><h3>{esc(p["title"])}</h3><span>{p["cat"]}</span></div>
</a>"""


def cta_block(depth):
    r = "../" * depth
    return f"""<section class="cta"><div class="wrap rv">
  <span class="eyebrow">Start a project</span>
  <h2 class="display"><a href="{r}contact.html">Let's build<br>something <em>lasting.</em></a></h2>
  <a class="btn" href="{r}contact.html">Get in touch <span class="arrow">→</span></a>
</div></section>
"""


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


# ------------------------------------------------------------------ PAGES
def page_home():
    hero_ids = ["canteen-05.jpg", "sid-bedroom-03.jpg", "auditorium-02.jpg", "living-room-03.jpg"]
    slides = "".join(
        f'<div class="hero__slide{" on" if i == 0 else ""}"><img src="images/{h}" alt="" {"fetchpriority=high" if i == 0 else "loading=lazy"}></div>'
        for i, h in enumerate(hero_ids))
    mq = "".join(f"<span>{w}</span>" for w in ["Architecture", "Interior Design", "Construction", "Space Planning", "Real Estate"] * 2)
    svc = "".join(f'<div class="svc rv"><span class="svc__n">{i:02d}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
                  for i, (t, d) in enumerate(SERVICES, 1))
    steps = "".join(f'<div class="step rv d{min(i,3)}"><b>{i:02d}</b><h3>{esc(t)}</h3><p>{esc(d)}</p></div>'
                    for i, (t, d) in enumerate(PROCESS, 1))
    cls = ["w1", "w2", "w3", "w4"]
    feat = [pby("sgi-canteen"), pby("bedroom-sage"), pby("living-room"), pby("sgi-auditorium")]
    works = "".join(card(p, 0, c) for p, c in zip(feat, cls))
    ld = f"""<script type="application/ld+json">{{"@context":"https://schema.org","@type":"HomeAndConstructionBusiness","name":"Shetty Infraventures","description":"Architecture, interior design, construction, planning and real estate.","email":"{SITE["email"]}","telephone":"{SITE["phones"][0][1]}"}}</script>"""
    return (head("Shetty Infraventures — Architecture, Interiors & Construction",
                 "Shetty Infraventures is a design-build studio: architect, builder, interior designer, planner and real estate. Explore our residential and institutional projects.", 0)
            + ld + nav(0, "home", over=True) + f"""<main id="main">
<section class="hero" style="padding:0">
  {slides}
  <div class="hero__body"><div class="wrap">
    <span class="eyebrow" style="color:#e9e2d6">Architect · Builder · Interior Designer</span>
    <h1 class="display">Spaces shaped by light, <em>material</em> &amp; intent.</h1>
    <div class="hero__row">
      <p>Shetty Infraventures designs and builds homes, workplaces and institutions: crafted with care from the first sketch to the final handover.</p>
      <div style="display:flex;gap:26px;align-items:center;flex-wrap:wrap">
        <a class="btn btn--light" href="projects.html">View projects <span class="arrow">→</span></a>
        <div class="hero__count"><span class="hero__cur">01</span><i></i><span>{len(hero_ids):02d}</span></div>
      </div>
    </div>
  </div></div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee__t">{mq}{mq}</div></div>

<section><div class="wrap intro">
  <div class="rv"><span class="eyebrow">The studio</span></div>
  <div class="rv d1">
    <p class="lead">We are a design-build practice. <em>One team</em> carries your project from architecture and interiors through to construction, so what is imagined is exactly what is built.</p>
    <div class="meta"><p>From a courtyard-style canteen to a sage-green bedroom suite, our work is rooted in natural light, honest materials and details that are made to last.</p>
    <a class="link" href="about.html">About the studio <span class="arrow">→</span></a></div>
  </div>
</div></section>

<section style="padding-top:0"><div class="wrap">
  <div class="sec-head"><div class="rv"><span class="eyebrow">Selected work</span><h2 class="display">Recent projects</h2></div>
  <a class="link rv" href="projects.html">All projects <span class="arrow">→</span></a></div>
  <div class="works">{works}</div>
</div></section>

<section class="services"><div class="wrap">
  <div class="sec-head"><div class="rv"><span class="eyebrow">What we do</span><h2 class="display">One studio, <em>every stage</em></h2></div></div>
  {svc}
</div></section>

<section><div class="wrap">
  <div class="sec-head"><div class="rv"><span class="eyebrow">How we work</span><h2 class="display">A clear process</h2></div></div>
  <div class="steps">{steps}</div>
</div></section>

<div class="band"><img src="images/office-cabin-06.jpg" alt="" loading="lazy">
  <blockquote class="rv">Every space tells a story. We shape it with light, material and care.</blockquote></div>

{cta_block(0)}
</main>
""" + footer(0))


def page_projects():
    cards = "".join(card(p, 0, "", "(max-width:560px) 100vw, (max-width:980px) 50vw, 33vw") for p in PROJECTS)
    cats = ["Residential", "Institutional"]
    btns = '<button class="on" data-f="all">All</button>' + "".join(f'<button data-f="{c}">{c}</button>' for c in cats)
    return (head("Projects — Shetty Infraventures", "Residential and institutional interiors by Shetty Infraventures: canteen, auditorium, office, living room and bedroom designs.", 0)
            + nav(0, "projects") + f"""<main id="main">
<section class="phead" style="padding-bottom:20px"><div class="wrap rv">
  <span class="eyebrow">Portfolio</span>
  <h1 class="display">Projects</h1>
  <p>A selection of residential and institutional interiors, designed and delivered by our studio.</p>
</div></section>
<section style="padding-top:30px"><div class="wrap">
  <div class="filters" role="group" aria-label="Filter projects">{btns}</div>
  <div class="pgrid">{cards}</div>
</div></section>
{cta_block(0)}
</main>
""" + footer(0))


def page_project(idx):
    p = PROJECTS[idx]
    nxt = PROJECTS[(idx + 1) % len(PROJECTS)]
    paras = "".join(f"<p>{esc(t)}</p>" for t in p["text"])
    notes = ""
    if p["notes"]:
        notes = '<p style="font-family:var(--serif);font-style:italic;font-size:1.3rem;color:var(--ink)">' + " &nbsp;·&nbsp; ".join(esc(n) for n in p["notes"]) + "</p>"
    facts = "".join(f"<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>" for k, v in p["facts"])
    gal = "".join(
        f'<button class="rv" data-full="../images/{t}" aria-label="Open image {i} of {len(p["thumbs"])}"><img src="../images/thumbs/{t}" alt="{esc(p["title"])}, photo {i}" loading="lazy"></button>'
        for i, t in enumerate(p["thumbs"], 1))
    return (head(f"{p['title']} — Shetty Infraventures", p["tag"], 1, p["cover_img"])
            + nav(1, "projects") + f"""<main id="main">
<div class="phero"><img src="../images/{p["cover_img"]}" alt="{esc(p["title"])} by Shetty Infraventures" fetchpriority="high"></div>
<div class="wrap pmeta">
  <div class="rv"><span class="eyebrow">{p["no"]} / {len(PROJECTS):02d} · {p["cat"]}</span><h1 class="display">{esc(p["title"])}</h1><p class="tag">{esc(p["tag"])}</p></div>
  <div class="rv d1">{paras}{notes}<dl class="facts">{facts}</dl></div>
</div>
<section style="padding-top:10px"><div class="wrap"><div class="gal">{gal}</div></div></section>
<a class="next" href="{nxt["slug"]}.html"><img src="../images/thumbs/{nxt["cover_img"]}" alt="" loading="lazy"><span class="eyebrow" style="color:#ddd">Next project</span><h2 class="display">{esc(nxt["title"])}</h2></a>
</main>
""" + footer(1))


def page_about():
    return (head("The Studio — Shetty Infraventures", "Shetty Infraventures is a design-build studio covering architecture, interior design, construction, planning and real estate.", 0)
            + nav(0, "about") + f"""<main id="main">
<section class="phead"><div class="wrap rv">
  <span class="eyebrow">The studio</span>
  <h1 class="display">Design, built <em>with care.</em></h1>
  <p>Architect. Builder. Interior designer. Planner. We bring every discipline under one roof.</p>
</div></section>
<section style="padding-top:20px"><div class="wrap split">
  <div class="rv"><img src="images/sid-bedroom-05.jpg" alt="Interior detail by Shetty Infraventures" loading="lazy"></div>
  <div class="rv d1"><span class="eyebrow">Who we are</span><h2 class="display">Where design and construction meet</h2>
    <p>Shetty Infraventures is a design-build studio. We take on architecture, interior design, planning and construction, along with real estate guidance, so you work with one accountable team from the first idea to the day you move in.</p>
    <p>Our projects range from private residences to institutional spaces such as canteens, auditoriums and offices. Each starts with the place itself: its light, its climate and the people who will use it.</p>
    <a class="link" href="projects.html">See our work <span class="arrow">→</span></a></div>
</div></section>
<section style="background:var(--bg-2)"><div class="wrap">
  <div class="sec-head"><div class="rv"><span class="eyebrow">Our approach</span><h2 class="display">What guides us</h2></div></div>
  <div class="values">
    <div class="value rv"><h3>Light first</h3><p>Daylight and carefully layered artificial light shape every room we design.</p></div>
    <div class="value rv d1"><h3>Honest materials</h3><p>Timber, stone, clay and textured finishes that age well and feel good to the touch.</p></div>
    <div class="value rv d2"><h3>Built as drawn</h3><p>Because we also build, the detail you approve on paper is the detail you get on site.</p></div>
  </div>
</div></section>
<section class="services"><div class="wrap">
  <div class="sec-head"><div class="rv"><span class="eyebrow">Services</span><h2 class="display">What we offer</h2></div></div>
  {"".join(f'<div class="svc rv"><span class="svc__n">{i:02d}</span><h3>{esc(t)}</h3><p>{esc(d)}</p></div>' for i, (t, d) in enumerate(SERVICES, 1))}
</div></section>
{cta_block(0)}
</main>
""" + footer(0))


def page_contact():
    phones = "".join(f'<li><small>Phone</small><a href="tel:{t}">{esc(l)}</a></li>' for l, t in SITE["phones"])
    insta = f'<li><small>Instagram</small><a href="{esc(SITE["instagram"])}" target="_blank" rel="noopener">Follow our work</a></li>' if SITE["instagram"] else ""
    addr = f'<li><small>Studio</small><span>{esc(SITE["address"])}</span></li>' if SITE["address"] else ""
    if SITE["maps"]:
        addr += f'<li><small>Location</small><a href="{esc(SITE["maps"])}" target="_blank" rel="noopener">View on Google Maps</a></li>'
    return (head("Contact — Shetty Infraventures", "Get in touch with Shetty Infraventures to discuss your architecture, interior design or construction project.", 0)
            + nav(0, "contact") + f"""<main id="main">
<section class="phead" style="padding-bottom:30px"><div class="wrap rv">
  <span class="eyebrow">Contact</span>
  <h1 class="display">Let's talk about <em>your space.</em></h1>
  <p>Tell us about your project and we will get back to you.</p>
</div></section>
<section style="padding-top:30px"><div class="wrap contact">
  <div class="rv"><ul class="clist">
    <li><small>Email</small><a href="mailto:{esc(SITE["email"])}">{esc(SITE["email"])}</a></li>
    {phones}
    <li><small>WhatsApp</small><a href="https://wa.me/{SITE["whatsapp"]}" target="_blank" rel="noopener">Message us</a></li>
    {insta}{addr}
  </ul></div>
  <div class="rv d1">
    <h2 class="display">Send an enquiry</h2>
    <form id="enquiry" data-to="{esc(SITE["email"])}">
      <div class="row2"><div><label for="name">Name</label><input id="name" name="name" required autocomplete="name"></div>
      <div><label for="phone">Phone</label><input id="phone" name="phone" type="tel" autocomplete="tel"></div></div>
      <div><label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email"></div>
      <div><label for="type">I'm interested in</label>
        <select id="type" name="type"><option>Architecture</option><option>Interior design</option><option>Construction</option><option>Space planning</option><option>Real estate</option><option>Something else</option></select></div>
      <div><label for="message">Tell us about your project</label><textarea id="message" name="message" required></textarea></div>
      <div><button class="btn btn--fill" type="submit">Send enquiry <span class="arrow">→</span></button></div>
      <p class="note">Sending opens your email app with the message ready to go.</p>
    </form>
  </div>
</div></section>
</main>
""" + footer(0))


# ------------------------------------------------------------------ RUN
if __name__ == "__main__":
    write("index.html", page_home())
    write("projects.html", page_projects())
    write("about.html", page_about())
    write("contact.html", page_contact())
    for i, p in enumerate(PROJECTS):
        write(f"projects/{p['slug']}.html", page_project(i))
    print("Built", 4 + len(PROJECTS), "pages")
