"""Integrity and payload budgets for the static portal; no dependencies."""
from pathlib import Path
import hashlib
import json
import re
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parent.parent
raw = (ROOT / 'index.html').read_bytes()
html = raw.decode('utf-8')
assert len(raw) <= 45_000, 'HTML exceeds 45 KB'
assert 'base64,' not in html, 'Embedded binary increases initial payload'

def metadata(script_id):
    match = re.search(r'<script id="' + script_id + r'" type="application/json">(.*?)</script>', html, re.S)
    assert match, f'Missing metadata: {script_id}'
    return json.loads(match[1])

files, photos = metadata('filedata'), metadata('photodata')
assert len(files) == 13 and len(photos) == 7, 'Document or photo missing'
assert sum(f['kind'] == 'PDF' for f in files) == 8
assert sum(f['kind'] == 'DWG' for f in files) == 5

def resource(url):
    path = (ROOT / url).resolve()
    assert path.is_relative_to(ROOT) and path.is_file(), f'Invalid resource: {url}'
    return path

for item in files + photos:
    data = resource(item['url']).read_bytes()
    assert len(data) == item['size'], f'Size changed: {item["name"]}'
    assert hashlib.sha256(data).hexdigest() == item['sha256'], f'Original changed: {item["name"]}'
    for key in ['preview', 'thumbnail', 'display']:
        if key in item:
            assert resource(item[key]).stat().st_size > 0

class HeroParser(HTMLParser):
    hero = None
    def handle_starttag(self, tag, attrs):
        fields = dict(attrs)
        if tag == 'img' and fields.get('id') == 'heroImage':
            self.hero = fields

parser = HeroParser()
parser.feed(html)
assert parser.hero and parser.hero.get('fetchpriority') == 'high'
variants = {}
for variant in parser.hero['srcset'].split(','):
    url, width = variant.strip().split()
    variants[int(width[:-1])] = resource(url)
assert len(raw) + variants[960].stat().st_size <= 250_000, 'Desktop opening exceeds 250 KB'
assert len(raw) + variants[480].stat().st_size <= 100_000, 'Mobile opening exceeds 100 KB'
assert 'width' in parser.hero and 'height' in parser.hero
print('OK: 20 original downloads, all previews and photos, and initial payload budgets.')
