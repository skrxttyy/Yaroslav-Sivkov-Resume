import html
import json
from pathlib import Path
from urllib.parse import urlparse

def render(projects):
    rows = []
    for project in projects:
        if urlparse(project['url']).scheme != 'https':
            raise ValueError('HTTPS project links required')
        rows.append('<li><a href="' + html.escape(project['url'], quote=True) + '">' + html.escape(project['name']) + '</a></li>')
    return '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Yaroslav Sivkov</title><style>body{font:18px/1.6 system-ui;max-width:850px;margin:60px auto;padding:0 24px;color:#17202a}a{color:#145da0}li{margin:16px 0}</style><h1>Yaroslav Sivkov</h1><p>Data Scientist · Machine Learning · Model Evaluation &amp; Validation</p><h2>Projects</h2><ul>' + ''.join(rows) + '</ul></html>\n'

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    projects = json.loads((root / 'data/projects.json').read_text(encoding='utf-8'))
    output = root / 'site/index.html'
    output.parent.mkdir(exist_ok=True)
    output.write_text(render(projects), encoding='utf-8')
    print(output)
