extensions = ["sphinx_seibootcamps", "sphinx_seibootcamps.admonitions"]
html_theme = "seibootcamps"
seibootcamps_html_preconnect = [
    "https://fonts.googleapis.com",
    "https://fonts.gstatic.com",
]

html_css_files = [
    "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&family=Source+Sans+3:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap",
    "overrides.css",
]
html_static_path = ["_static"]

exclude_patterns = ["_build", "_static", ".DS_Store"]
