#!/usr/bin/env python3
"""Produce un HTML con esquemas sin modificar el Markdown clínico original."""
from pathlib import Path
import hashlib
import html
import json
import re
import unicodedata

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt
from graficos_crm import add_graphics

BASE = Path(__file__).resolve().parent.parent
NAME = 'Algoritmos_CRM_2026_Revision_Clinica'
markdown_path = BASE / f'{NAME}.md'
markdown_hash_before = hashlib.sha256(markdown_path.read_bytes()).hexdigest()
source = markdown_path.read_text(encoding='utf-8')
body = re.sub(r'\A---\n.*?\n---\n', '', source, count=1, flags=re.S)
rendered = MarkdownIt('commonmark', {'html': True, 'typographer': False}).enable('table').render(body)
soup = BeautifulSoup(rendered, 'html.parser')

def slug(text):
    text = unicodedata.normalize('NFKD', text)
    return re.sub(r'[^a-z0-9]+', '-', ''.join(c for c in text if not unicodedata.combining(c)).lower()).strip('-')

used = {a['id'] for a in soup.select('[id]')}
toc = []
for heading in soup.select('h2, h3'):
    previous = heading.find_previous_sibling()
    anchor = previous.get('id') if previous and previous.name == 'a' else None
    if not anchor:
        anchor = slug(heading.get_text(' ', strip=True))
        if anchor in used:
            raise ValueError(f'ID duplicado: {anchor}')
        heading['id'] = anchor
        used.add(anchor)
    heading['data-anchor'] = anchor
    if heading.name == 'h2' or anchor.startswith('algoritmo-'):
        toc.append((heading.name, anchor, heading.get_text(' ', strip=True)))

for table in soup.select('table'):
    wrap = soup.new_tag('div', attrs={'class': 'table-scroll', 'tabindex': '0', 'role': 'region', 'aria-label': 'Tabla clínica; desplazamiento horizontal disponible'})
    table.wrap(wrap)
for link in soup.select('a[href]'):
    if link['href'].startswith('https://'):
        link['rel'] = 'noreferrer'

nav = '\n'.join(f'<a class="toc-{level}" href="#{anchor}">{html.escape(label)}</a>' for level, anchor, label in toc)
plain = soup.get_text(' ', strip=True)
word_count = len(re.findall(r'\b[\wÀ-ÿ]+(?:[’\-][\wÀ-ÿ]+)*\b', plain))
css = r'''
:root{--ink:#17212c;--muted:#536171;--blue:#002fa7;--paper:#fff;--soft:#f5f7fa;--line:#d8dee8;--warm:#a43d18;--aside:280px}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:30px}body{margin:0;background:var(--paper);color:var(--ink);font-family:"Helvetica Neue",Helvetica,Arial,sans-serif;font-size:17px;line-height:1.72}a{color:var(--blue);text-underline-offset:3px}a:hover{color:#001961}a:focus-visible,button:focus-visible,input:focus-visible,summary:focus-visible,[tabindex]:focus-visible{outline:3px solid #e7791c;outline-offset:3px}.skip{position:fixed;left:10px;top:-100px;background:#fff;padding:8px;z-index:9}.skip:focus{top:10px}
.sidebar{position:fixed;inset:0 auto 0 0;width:var(--aside);padding:30px 22px;background:var(--soft);border-right:1px solid var(--line);overflow-y:auto}.brand{font-size:16px;font-weight:750;letter-spacing:.08em;color:var(--blue)}.edition{font-size:12px;color:var(--muted);margin:5px 0 26px;letter-spacing:.02em}.search-label{font-size:12px;font-weight:700;display:block;margin-bottom:5px}.search{width:100%;font:inherit;font-size:14px;border:1px solid #aab4c4;border-radius:2px;padding:9px;background:#fff}.find-controls{display:flex;align-items:center;gap:5px;margin:8px 0 3px}.find-controls button{padding:4px 8px;font-size:12px}.search-status{display:block;font-size:12px;color:var(--muted);min-height:35px;line-height:1.45}button,.button{font:inherit;font-size:13px;line-height:1.5;border:1px solid var(--line);background:white;color:var(--ink);padding:8px 12px;border-radius:2px;cursor:pointer;text-decoration:none}button:hover,.button:hover{background:#edf1fa}button:disabled{opacity:.45;cursor:default}.toc{border-top:1px solid var(--line);padding-top:15px;margin-top:14px}.toc a{display:block;color:#455366;font-size:13px;line-height:1.45;text-decoration:none;padding:7px 9px;border-left:2px solid transparent}.toc a.current{color:var(--blue);border-left-color:var(--blue);background:#eaf0fc;font-weight:650}.toc .toc-h3{font-size:12px;padding-left:21px}.side-note{font-size:11px;color:var(--muted);line-height:1.55;margin-top:24px}.mobile-nav{display:none}
.page{margin-left:var(--aside)}.hero{padding:60px clamp(26px,5vw,92px) 44px;border-bottom:1px solid var(--line);max-width:1450px}.eyebrow{font-size:12px;letter-spacing:.12em;text-transform:uppercase;font-weight:700;color:var(--blue);margin:0 0 20px}.hero h1{font-size:clamp(32px,3.5vw,55px);line-height:1.08;letter-spacing:-.035em;max-width:940px;margin:0 0 24px;font-weight:700}.intro{font-size:18px;line-height:1.65;color:var(--muted);max-width:760px;margin:0 0 24px}.meta{display:flex;gap:12px 26px;flex-wrap:wrap;font-size:12px;color:var(--muted);padding:18px 0;border-top:1px solid var(--line)}.meta strong{color:var(--ink);display:block;font-size:14px}.actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}.source-note{max-width:850px;border-left:3px solid var(--warm);padding:10px 16px;background:#fcf6f1;font-size:13px;line-height:1.6;margin-top:24px}.quick{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0;margin-top:28px;border-top:1px solid var(--line);border-left:1px solid var(--line)}.quick a{display:flex;gap:10px;align-items:baseline;text-decoration:none;color:var(--ink);padding:13px;border-right:1px solid var(--line);border-bottom:1px solid var(--line);font-size:13px;line-height:1.45}.quick span{font-weight:750;color:var(--blue);font-size:15px}.quick a:hover{background:var(--soft)}
main{padding:12px clamp(26px,5vw,92px) 75px;max-width:1450px}#clinical>h1{font-size:25px;margin-top:36px;margin-bottom:12px}h2{font-size:29px;line-height:1.25;letter-spacing:-.025em;border-top:2px solid var(--ink);padding-top:28px;margin:66px 0 24px;scroll-margin-top:28px}h3{font-size:22px;line-height:1.35;margin:38px 0 18px;scroll-margin-top:28px}p{margin:0 0 18px;max-width:90ch}strong{font-weight:700}ul,ol{padding-left:24px}li{margin:7px 0}li>ul{margin-top:8px}code{font-size:.88em;padding:2px 5px;background:var(--soft);overflow-wrap:anywhere}a[id]{display:block;scroll-margin-top:24px}.table-scroll{width:100%;overflow-x:auto;margin:27px 0;border:1px solid var(--line)}table{width:100%;border-collapse:collapse;font-size:14px;line-height:1.6;min-width:570px}th{text-align:left;font-size:12px;letter-spacing:.02em;background:#edf1f8;color:var(--ink);border-bottom:1px solid #aebbd0}td,th{padding:13px 14px;vertical-align:top;border-right:1px solid var(--line);border-bottom:1px solid var(--line)}tr:last-child td{border-bottom:0}td:last-child,th:last-child{border-right:0}tbody tr:nth-child(even){background:#fafbfd}td strong{color:#162d56}.has-match{background:#fff1b9!important;outline:1px solid #e5c766;outline-offset:2px}.active-match{background:#ffe08a!important;outline:2px solid #aa6500}.footer{border-top:1px solid var(--line);padding:24px clamp(26px,5vw,92px);font-size:12px;color:var(--muted)}.backtop{position:fixed;bottom:18px;right:20px;background:#fff;box-shadow:0 2px 12px #0001}.noscript{padding:14px;background:#fff1b9}
@media(min-width:1600px){:root{--aside:310px}body{font-size:18px}.sidebar{padding:34px 26px}}
@media(max-width:950px){:root{--aside:240px}.sidebar{padding:22px 14px}.hero,main{padding-left:28px;padding-right:28px}.quick{grid-template-columns:repeat(2,minmax(0,1fr))}.hero{padding-top:36px}}
@media(max-width:720px){body{font-size:16px;line-height:1.7}.sidebar{position:static;width:100%;padding:18px 20px;border-right:0;border-bottom:1px solid var(--line)}.brand{font-size:14px}.edition{margin-bottom:12px}.sidebar .toc{display:none}.side-note{display:none}.mobile-nav{display:block;font-size:14px;border-top:1px solid var(--line);margin-top:12px;padding-top:12px}.mobile-nav summary{cursor:pointer;font-weight:650}.mobile-nav a{display:block;padding:5px 0;font-size:13px;text-decoration:none}.page{margin:0}.hero{padding:32px 20px}.hero h1{font-size:36px}.intro{font-size:16px}.meta{gap:12px 22px}.quick a{font-size:12px;padding:12px 9px}main{padding:0 20px 50px}h2{font-size:26px;margin-top:48px}h3{font-size:21px}.table-scroll{width:100%;margin:22px 0}td,th{padding:11px}.footer{padding:22px 20px}.backtop{font-size:12px;padding:5px 9px}.find-controls{margin-top:6px}.search-status{min-height:20px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
@media print{body{font-size:10pt;line-height:1.5;color:#000}.sidebar,.actions,.quick,.backtop,.search-status{display:none!important}.page{margin:0}.hero{padding:0 0 18pt;border:0}.hero h1{font-size:28pt}.intro{font-size:11pt}.source-note{font-size:9pt}.meta{font-size:8pt}.hero,main{max-width:none}main{padding:0}h2{font-size:19pt;margin-top:28pt;padding-top:12pt;break-after:avoid}h3{font-size:14pt;break-after:avoid}p{orphans:3;widows:3}table{font-size:8pt;min-width:0}td,th{padding:6pt}.table-scroll{overflow:visible;break-inside:auto}thead{display:table-header-group}tr{break-inside:avoid}a{color:#000;text-decoration:underline}.has-match,.active-match{background:transparent!important;outline:0}.footer{font-size:8pt;padding:16pt 0}#clinical>h1{display:none}@page{size:A4;margin:17mm}}
'''
js = r'''
const input=document.querySelector('#find');
const status=document.querySelector('#status');
const prev=document.querySelector('#prev');
const next=document.querySelector('#next');
let matches=[],current=-1,timer;
const normalize=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLocaleLowerCase('es');
function report(){status.textContent=matches.length?`${current+1} de ${matches.length} coincidencias`:input.value.trim().length>1?'Sin coincidencias':'Buscar en todo el documento';prev.disabled=next.disabled=!matches.length}
function move(delta){if(!matches.length)return;if(current>=0)matches[current].classList.remove('active-match');current=(current+delta+matches.length)%matches.length;matches[current].classList.add('active-match');matches[current].scrollIntoView({block:'center',behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'});report()}
function search(){document.querySelectorAll('.has-match,.active-match').forEach(e=>e.classList.remove('has-match','active-match'));matches=[];current=-1;const q=normalize(input.value.trim());if(q.length>1){const candidates=Array.from(document.querySelectorAll('#clinical p,#clinical li,#clinical td,#clinical th,#clinical h2,#clinical h3'));const found=candidates.filter(e=>normalize(e.textContent).includes(q));matches=found.filter(e=>!found.some(child=>child!==e&&e.contains(child)));matches.forEach(e=>e.classList.add('has-match'))}report()}
input.addEventListener('input',()=>{clearTimeout(timer);timer=setTimeout(search,160)});
input.addEventListener('keydown',e=>{if(e.key==='Enter'){e.preventDefault();clearTimeout(timer);if(current<0)search();move(e.shiftKey?-1:1)}if(e.key==='Escape'){input.value='';search()}});
prev.addEventListener('click',()=>move(-1));next.addEventListener('click',()=>move(1));
document.querySelector('#clear').addEventListener('click',()=>{input.value='';search();input.focus()});
document.querySelector('#print').addEventListener('click',()=>window.print());
const links=Array.from(document.querySelectorAll('.toc a'));
const observer=new IntersectionObserver(entries=>{const visible=entries.filter(e=>e.isIntersecting);if(!visible.length)return;const id=visible[0].target.dataset.anchor;links.forEach(a=>{const active=a.getAttribute('href')==='#'+id;a.classList.toggle('current',active);if(active)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')})},{rootMargin:'-5% 0px -70% 0px'});
document.querySelectorAll('#clinical h2[data-anchor],#clinical h3[data-anchor^="algoritmo-"]').forEach(h=>observer.observe(h));
report();
'''
page = f'''<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Revisión clínica extensa para Medicina Familiar, basada exclusivamente en fuentes ESC y KDIGO de 2026; seis algoritmos y cuatro casos razonados."><title>Síndrome cardiovascular, renal y metabólico · Revisión clínica 2026</title><style>{css}</style></head>
<body id="inicio"><a class="skip" href="#clinical">Saltar al contenido clínico</a>
<aside class="sidebar" aria-label="Navegación de la revisión"><div class="brand">CRM / 2026</div><div class="edition">Revisión clínica · Medicina Familiar</div><label class="search-label" for="find">Buscar en la revisión</label><input class="search" id="find" type="search" placeholder="Ej.: finerenona, potasio…" autocomplete="off"><div class="find-controls"><button id="prev" disabled aria-label="Coincidencia anterior">Anterior</button><button id="next" disabled aria-label="Coincidencia siguiente">Siguiente</button><button id="clear">Borrar</button></div><output id="status" class="search-status" aria-live="polite"></output><nav class="toc" aria-label="Índice de secciones">{nav}</nav><details class="mobile-nav"><summary>Índice de secciones y algoritmos</summary>{nav}</details><p class="side-note">Corte documental: 30.09.2026.<br>Guías, consensos y borrador identificados por separado.<br>Lectura disponible sin conexión.</p></aside>
<div class="page"><header class="hero"><p class="eyebrow">ESC · ERA · KDIGO / Medicina Familiar</p><h1>Síndrome cardiovascular,<br>renal y metabólico.</h1><p class="intro">Evaluación, decisiones terapéuticas y seguimiento. Seis algoritmos escritos, tablas de tratamiento y cuatro casos clínicos razonados.</p><div class="meta"><div><strong>30 septiembre 2026</strong>Fecha de corte</div><div><strong>{word_count:,} palabras</strong>Contenido de la revisión</div><div><strong>Consulta y descompensaciones</strong>Ámbito de aplicación</div></div><div class="actions"><a class="button" href="{NAME}.md" download>Descargar Markdown</a><button id="print">Imprimir / guardar PDF</button><a class="button" href="#referencias">Consultar fuentes</a></div><div class="source-note"><strong>Alcance de las fuentes.</strong> Solo ESC y KDIGO 2026. KDIGO Diabetes 2026 es un borrador y se mantiene separado. Las dosis se contrastan con la guía, sin validación CIMA/AEMPS. Consulte los límites de prescripción antes de utilizar las tablas.</div><nav class="quick" aria-label="Acceso a los seis algoritmos"><a href="#algoritmo-1"><span>01</span>DM2 y comorbilidades</a><a href="#algoritmo-2"><span>02</span>Confirmar ERC</a><a href="#algoritmo-3"><span>03</span>DM2 con ERC</a><a href="#algoritmo-4"><span>04</span>Diagnosticar IC</a><a href="#algoritmo-5"><span>05</span>Tratar IC por fenotipo</a><a href="#algoritmo-6"><span>06</span>Integración clínica</a></nav></header>
<main id="clinical">{soup}</main><footer class="footer">Revisión documental con corte 30.09.2026 · Texto clínico generado desde el mismo archivo Markdown · Sin datos de pacientes · Fuentes y límites al final del documento.</footer></div><a class="button backtop" href="#inicio" aria-label="Volver al inicio">↑ Inicio</a><noscript><p class="noscript">El índice y el documento completo están disponibles. La búsqueda interactiva necesita JavaScript.</p></noscript><script>{js}</script></body></html>'''
page = add_graphics(page)
(BASE / f'{NAME}.html').write_text(page, encoding='utf-8')
qa = BeautifulSoup(page, 'html.parser')
all_ids = [el['id'] for el in qa.select('[id]')]
internal = [a['href'][1:] for a in qa.select('a[href^="#"]')]
broken = sorted(set(internal) - set(all_ids))
assert not broken, broken
assert len(all_ids) == len(set(all_ids)), 'IDs repetidos'
assert not qa.select('img'), 'No se admiten imágenes incrustadas'
assert not re.search(r'\[[^\]\n]+\]\[(?:E\d|ES|K\d|KD)\]', qa.get_text()), 'Referencias sin resolver'
assert 10000 <= word_count <= 22000, word_count
clinical_rendered = BeautifulSoup(rendered, 'html.parser').get_text(' ', strip=True)
original_section = BeautifulSoup(str(qa.select_one('#clinical')), 'html.parser')
for graphic in original_section.select('.clinical-graphic'):
    graphic.decompose()
clinical_html = original_section.get_text(' ', strip=True)
assert clinical_rendered == clinical_html, 'Cambió el texto clínico al generar HTML'
assert hashlib.sha256(markdown_path.read_bytes()).hexdigest() == markdown_hash_before, 'Se modificó el Markdown'
assert len(qa.select('.clinical-graphic')) == 12
assert len(qa.select('.clinical-graphic .outcome')) == 8
assert len(qa.select('[data-ga-description]')) == 18
result = {'word_count': word_count, 'original_tables': len(original_section.select('table')), 'tables_including_diagrams': len(qa.select('#clinical table')), 'original_headings': len(original_section.select('h2,h3')), 'diagrams': len(qa.select('.clinical-graphic')), 'interactive_matrix_cells': len(qa.select('[data-ga-description]')), 'internal_links': len(internal), 'broken_internal_links': broken, 'original_clinical_text_preserved': True, 'markdown_unchanged': True, 'images': len(qa.select('img')), 'external_scripts': len(qa.select('script[src]')), 'files': {ext: {'bytes': (BASE/f'{NAME}.{ext}').stat().st_size,'sha256':hashlib.sha256((BASE/f'{NAME}.{ext}').read_bytes()).hexdigest()} for ext in ['md','html']}}
(BASE/'verificacion/validacion_estructural.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n',encoding='utf-8')
print(json.dumps(result, ensure_ascii=False, indent=2))
