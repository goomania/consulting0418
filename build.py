"""
AISprint site builder.
Reads page-specific content from `pages/` and assembles final static HTML
using shared partials (nav, footer, head). Outputs to the repo root.

Usage:  python build.py
"""

from pathlib import Path

ROOT = Path(__file__).parent
PAGES_DIR = ROOT / "pages"
PARTIALS_DIR = ROOT / "partials"
OUT_DIR = ROOT

HEAD_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
<link rel="stylesheet" href="css/styles.css">
</head>
<body>
"""


def nav(active: str) -> str:
    def a(slug, label, href):
        cls = ' class="active"' if slug == active else ""
        return f'<li><a href="{href}"{cls}>{label}</a></li>'

    items = [
        ("home", "Home", "index.html"),
        ("about", "About", "about.html"),
        ("services", "Services", "services.html"),
        ("how-we-help", "How we help", "how-we-help.html"),
        ("case-studies", "Case studies", "case-studies.html"),
        ("insights", "Insights", "insights.html"),
        ("contact", "Contact", "contact.html"),
    ]
    links = "\n        ".join(a(s, l, h) for s, l, h in items)
    return f"""<header class="topbar">
  <div class="topbar-inner">
    <a href="index.html" class="brand">
      <span class="brand-mark">A</span>
      <span class="brand-name">AI<em>Sprint</em></span>
    </a>
    <nav>
      <ul class="nav-primary">
        {links}
      </ul>
    </nav>
    <div class="nav-right">
      <a href="insights.html" class="nav-search">Insights →</a>
      <a href="contact.html" class="btn btn-primary">Contact us</a>
      <button class="nav-toggle" aria-expanded="false" aria-label="Menu">☰</button>
    </div>
  </div>
</header>
"""


FOOTER = """<footer class="footer">
  <div class="container-wide">
    <div class="affiliation">
      <div class="affiliation-mark">SU</div>
      <div class="affiliation-text">
        <strong>In collaboration with Syracuse University.</strong><br>
        AISprint maintains active consulting engagements with Syracuse University programs and research centers.
      </div>
    </div>
    <div class="footer-top">
      <div>
        <div class="brand">
          <span class="brand-mark">A</span>
          <span class="brand-name">AI<em>Sprint</em></span>
        </div>
        <p class="footer-tag">A boutique AI consulting practice for institutions that need AI to actually work.</p>
        <div class="footer-social">
          <a href="#" aria-label="LinkedIn">in</a>
          <a href="#" aria-label="X / Twitter">X</a>
          <a href="#" aria-label="Medium">M</a>
        </div>
      </div>
      <div>
        <h4>Navigate</h4>
        <ul>
          <li><a href="index.html">Home</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="services.html">Services</a></li>
          <li><a href="how-we-help.html">How we help</a></li>
          <li><a href="case-studies.html">Case studies</a></li>
          <li><a href="insights.html">Insights</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="services.html#strategy">AI Strategy</a></li>
          <li><a href="services.html#architecture">Architecture</a></li>
          <li><a href="services.html#program">Program Design</a></li>
          <li><a href="services.html#research">Applied Research</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="mailto:hello@aisprint.ai">hello@aisprint.ai</a></li>
          <li>Syracuse, New York</li>
          <li><a href="contact.html">Schedule a call</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-base">
      <span>© <span data-year>2026</span> AISprint Consulting, LLC. All rights reserved.</span>
      <span>Syracuse, NY · Made with care</span>
    </div>
  </div>
</footer>

<script src="js/main.js"></script>
</body>
</html>
"""


def build_page(slug: str, title: str, description: str, body: str, nav_slug: str) -> str:
    return (
        HEAD_TEMPLATE.format(title=title, description=description)
        + nav(nav_slug)
        + "<main id=\"main\">\n"
        + body
        + "\n</main>\n"
        + FOOTER
    )


if __name__ == "__main__":
    print("This file documents how the pages are structured. The pages/ directory")
    print("contains the per-page body HTML. Run-time assembly is done at publish time.")
