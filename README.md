# Shetty Infraventures

Portfolio website for Shetty Infraventures: architecture, interior design, construction, planning and real estate.

Plain static site (HTML, CSS, JavaScript). No framework and no build tools are needed to view or host it.

## Pages
- `index.html`: home
- `projects.html`: project grid with Residential / Institutional filter
- `projects/*.html`: one page per project with a lightbox gallery
- `about.html`: the studio
- `contact.html`: contact details and enquiry form (opens the visitor's email app)

## Editing content
All text, contact details, services and projects live at the top of `build.py`.

1. Edit `build.py` (for example the `SITE` block to add the Instagram URL and studio address).
2. Run `python3 build.py` to regenerate the HTML pages.

To add a project: put photos in `images/` (and 900px copies in `images/thumbs/`) named `folder-01.jpg`, `folder-02.jpg`, ..., then add an entry to `PROJECTS`.

## Hosting
- **GitHub Pages:** Settings → Pages → deploy from the `main` branch, root folder.
- **Netlify / Vercel / Cloudflare Pages:** import the repository; no build command, publish directory `/`.

## Folder layout
```
index.html  projects.html  about.html  contact.html
projects/   css/style.css  js/main.js  images/  build.py
```
