# Lemo-Opuscar 风格影展：STYLES.md + cards.json → catalog.json → index.html（并刷新 README 里的风格清单）
# 本地：python3 styleboard/build.py          GitHub Pages：python3 styleboard/build.py --site _site
import argparse, json, re, html, os, glob, shutil, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
cards = json.load(open(os.path.join(HERE, 'cards.json'), encoding='utf-8'))   # 卡片文案：英文片名、一句话故事、适用场景

CN = {'pixel-rpg': '16-bit 像素 RPG', 'brick-toy': '积木玩具', 'paper-popup': '纸片立体书', 'halftone-dossier': '复古半调案卷',
      'game-show': '综艺节奏扁平', 'editorial-minimal': '东方杂志排版', 'dark-keynote': '暗色科技发布', 'living-screencast': '活体实机录屏', 'watercolor': '水彩笔刷',
      'photo-parallax': '照片视差纪念片', 'crayon-book': '蜡笔儿童绘本', 'risograph': 'Risograph 丝网印刷', 'rubber-hose': '1930s 橡皮管卡通',
      'ink-wash': '中国水墨', 'shadow-puppet': '皮影戏', 'ukiyoe': '浮世绘', 'felt-knit': '毛毡针织', 'felt-knit-2d': '毛毡针织 · 2D 版',
      'tilt-shift': '移轴微缩', 'lowpoly-island': '低多边形等距', 'film-noir': '黑色电影', 'glass-product': '玻璃质感产品',
      'origami': '折纸', 'backrooms': '后室 / 新怪谈', 'blueprint': '蓝图 / 工程制图', 'microgame': '微游戏快闪（瓦里奥制造式）', 'synthwave': '霓虹合成波', 'swiss-motion': '瑞士动态排版', 'voxel': '体素', 'gameboy': 'Game Boy 四色',
      'cardboard': '瓦楞纸板', 'dunhuang': '敦煌壁画', 'papercut-red': '红色窗花剪纸', 'impasto': '油画厚涂', 'one-line': '一笔画',
      'stained-glass': '彩色玻璃窗', 'silent-film': '1920s 默片', 'spy-titles': '60s 间谍片头', 'ascii-crt': 'ASCII / CRT 终端',
      'dataviz': '数据叙事', 'whiteboard': '白板讲解', 'iso-infographic': '等距信息图', 'hd-2d': 'HD-2D', 'urban-sketch': '钢笔淡彩', 'cel-anime-80s': '80 年代赛璐璐动画', 'scifi-toon': '科幻情景喜剧卡通', 'art-deco': '装饰艺术', 'woodcut': '木刻版画', 'pop-art': '波普漫画', 'paper-lantern': '纸雕灯影', 'pictogram-motion': '象形运动图形'}

REPO = 'lemomo-ai/lemo-opuscar'                                   # GitHub 仓库
FILMS_URL = f'https://github.com/{REPO}/releases/download/films'   # 成片放在 Release「films」里，文件名 <slug>.mp4
BLOB_URL = f'https://github.com/{REPO}/blob/main'
ROOT = os.path.join(HERE, '..')
CATALOG = os.path.join(HERE, 'catalog.json')   # 公开的风格目录（STYLES.md 不进仓库，CI 和 README 都读它）


def parse_styles_md():
    """本地维护：从 STYLES.md + cards.json 生成风格目录（带成片时长）。"""
    md = open(os.path.join(ROOT, 'STYLES.md'), encoding='utf-8').read()
    out, cat, cat_en = [], '', ''
    for block in re.split(r'\n(?=##+ )', md):
        head = block.split('\n', 1)[0]
        mb = re.match(r'## (.+?) · (.+)', head)
        if mb: cat, cat_en = mb.group(1).strip(), mb.group(2).strip(); continue
        m = re.match(r'### \[(x)\] (\d+[A-Z]?) · (.+?) · `([\w-]+)`', head)
        if not m: continue
        _, num, en, slug = m.groups()
        c = cards.get(slug, {})
        s = dict(slug=slug, num=num, en=en, cn=CN.get(slug, en), cat=cat, cat_en=cat_en,
                 film=c.get('film', ''), line=c.get('line', ''), line_cn=c.get('line_cn', ''), uses=c.get('uses', []), dur=0)
        mp4 = os.path.join(ROOT, 'styles', slug, slug + '.mp4')
        if os.path.exists(mp4):
            try: s['dur'] = round(float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', mp4], capture_output=True, text=True).stdout), 1)
            except ValueError: pass
        out.append(s)
    return out


ap = argparse.ArgumentParser()
ap.add_argument('--site', help='build the GitHub Pages site into this folder (films from Releases)')
args = ap.parse_args()

if os.path.exists(os.path.join(ROOT, 'STYLES.md')):
    styles = parse_styles_md()
    json.dump(styles, open(CATALOG, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
else:
    styles = json.load(open(CATALOG, encoding='utf-8'))

site = args.site
if site:   # 公开的图鉴只收有 STYLE.md 的（做完的）风格
    styles = [s for s in styles if os.path.exists(os.path.join(ROOT, 'styles', s['slug'], 'STYLE.md'))]
for s in styles:
    slug = s['slug']
    s['imgs'] = sorted(os.path.basename(p) for p in glob.glob(os.path.join(HERE, 'img', slug + '_*.jpg')))
    has_poster = os.path.exists(os.path.join(ROOT, 'styles', slug, 'poster.jpg'))
    has_md = os.path.exists(os.path.join(ROOT, 'styles', slug, 'STYLE.md'))
    if site:
        s['video'] = f'films/{slug}.mp4' if s['dur'] else ''          # 720p web cut, served by Pages as video/mp4 (Safari needs it)
        s['full'] = f'{FILMS_URL}/{slug}.mp4' if s['dur'] else ''       # full quality on Releases
        s['poster'] = f'posters/{slug}.jpg' if has_poster else ''
        s['stylemd'] = f'{BLOB_URL}/styles/{slug}/STYLE.md' if has_md else ''
    else:
        s['video'] = f'../styles/{slug}/{slug}.mp4' if os.path.exists(os.path.join(ROOT, 'styles', slug, slug + '.mp4')) else ''
        s['poster'] = f'../styles/{slug}/poster.jpg' if has_poster else ''
        s['stylemd'] = f'../styles/{slug}/STYLE.md' if has_md else ''

esc = lambda t: html.escape(t or '')

def laurel_symbol():
    # 月桂：左右两枝，每枝 9 片叶子沿圆弧排列
    import math
    leaves = []
    for side in (-1, 1):
        for i in range(9):
            a = math.radians(200 - i * 17) if side < 0 else math.radians(-20 + i * 17)
            cx, cy = 59 + 44 * math.cos(a), 34 + 27 * math.sin(a)
            rot = math.degrees(a) + (90 if side > 0 else -90) + side * 28
            leaves.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="2.3" ry="5.6" transform="rotate({rot:.1f} {cx:.1f} {cy:.1f})"/>')
    stems = '<path d="M22 50 Q10 30 24 10" fill="none" stroke="currentColor" stroke-width="1"/><path d="M96 50 Q108 30 94 10" fill="none" stroke="currentColor" stroke-width="1"/>'
    return f'<symbol id="laurel" viewBox="0 0 118 62"><g fill="currentColor">{"".join(leaves)}</g>{stems}</symbol>'

def mmss(d): return f'{int(d // 60)}:{int(round(d) % 60):02d}'

def card(s):
    img = f'img/{s["imgs"][0]}' if s['imgs'] else s.get('poster', '')
    vid = bool(s.get('video'))
    film = s.get('film') or s['en']
    main = f'<img class="still" src="{esc(img)}" alt="{esc(s["en"])} — {esc(film)}" loading="lazy">' if img else '<div class="empty">Coming soon</div>'
    play = (f'<button class="play" type="button" data-src="{esc(s["video"])}" data-poster="{esc(s.get("poster", ""))}" '
            f'aria-label="Play {esc(film)}"><i></i><span>{mmss(s["dur"])}</span></button>') if vid else ''
    uses = ''.join(f'<li>{esc(u)}</li>' for u in s.get('uses', []))
    links = []
    if vid: links.append(f'<a class="watch" href="{esc(s.get("full") or s["video"])}" data-play>Watch the film</a>')
    if s.get('stylemd'): links.append(f'<a href="{esc(s["stylemd"])}" target="_blank" rel="noopener">STYLE.md</a>')
    return (f'<article class="nominee" data-slug="{esc(s["slug"])}" data-en="{esc(s["en"])}" data-cn="{esc(s["cn"])}" data-film="{esc(film)}">\n'
            f'  <div class="screen">{main}{play}</div>\n'
            f'  <div class="plate">\n'
            f'    <h3>{esc(s["en"])}</h3><p class="cn">{esc(s["cn"])}</p>\n'
            f'    <p class="for">for <em>{esc(film)}</em></p>\n'
            f'    <p class="line">{esc(s.get("line", ""))}</p><p class="line-cn">{esc(s.get("line_cn", ""))}</p>\n'
            f'    {f"<ul class=uses aria-label=\"Best for\">{uses}</ul>" if uses else ""}\n'
            f'    <nav class="links">{"".join(links)}</nav>\n'
            f'  </div>\n</article>')

cats = list(dict.fromkeys((s['cat'], s['cat_en']) for s in styles))
sections, tabs = [], []
for i, (cn, en) in enumerate(cats, 1):
    group = [s for s in styles if s['cat'] == cn]
    sid = re.sub(r'[^a-z0-9]+', '-', en.lower()).strip('-')
    tabs.append(f'<button data-f="{sid}">{esc(en)}<small>{esc(cn)}</small></button>')
    sections.append(
        f'<section class="category" id="{sid}">\n'
        f'  <header class="cat-head"><svg class="lf"><use href="#laurel"/></svg>'
        f'<div><p class="cat-no">Category {i:02d}</p><h2>{esc(en)}</h2><p class="cat-cn">{esc(cn)} · {len(group)} nominees</p></div>'
        f'<svg class="lf"><use href="#laurel"/></svg></header>\n'
        f'  <div class="grid">\n' + '\n'.join(map(card, group)) + '\n  </div>\n</section>')

n_vid = sum(bool(s.get('video')) for s in styles)
minutes = sum(s.get('dur', 0) for s in styles) / 60
page = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
for k, v in {'{{LAUREL}}': laurel_symbol(), '{{SECTIONS}}': '\n'.join(sections), '{{TABS}}': ''.join(tabs),
             '{{N_ALL}}': str(len(styles)), '{{N_VID}}': str(n_vid), '{{N_CAT}}': str(len(cats)), '{{MIN}}': f'{minutes:.0f}',
             '{{REPO_URL}}': f'https://github.com/{REPO}', '{{REPO}}': REPO}.items():
    page = page.replace(k, v)
out_dir = site or HERE
os.makedirs(out_dir, exist_ok=True)
open(os.path.join(out_dir, 'index.html'), 'w', encoding='utf-8').write(page)
if site:   # Pages 站点：页面 + 风格帧 + 海报
    shutil.copytree(os.path.join(HERE, 'img'), os.path.join(site, 'img'), dirs_exist_ok=True)
    os.makedirs(os.path.join(site, 'posters'), exist_ok=True)
    for s in styles:
        if s['poster']: shutil.copy(os.path.join(ROOT, 'styles', s['slug'], 'poster.jpg'), os.path.join(site, 'posters', s['slug'] + '.jpg'))


def readme_grid():
    """README 里 <!-- styles:start --> … <!-- styles:end --> 之间：按类别的图片网格（docs/frames/<slug>.jpg），中英双语。"""
    out = []
    for cn, en in cats:
        group = [x for x in styles if x['cat'] == cn and x['stylemd']]
        if not group: continue
        out.append(f'\n### {en} · {cn}\n\n<table>')
        for i in range(0, len(group), 3):
            out.append('<tr>')
            for s in group[i:i + 3]:
                cn_name = f' · {s["cn"]}' if s['cn'] != s['en'] else ''
                out.append(f'<td width="33%" valign="top"><a href="styles/{s["slug"]}/STYLE.md"><img src="docs/frames/{s["slug"]}.jpg" alt="{html.escape(s["en"])}"></a><br>'
                           f'<b>{html.escape(s["en"])}</b>{html.escape(cn_name)}<br><i>{html.escape(s["film"])}</i><br>'
                           f'<sub>{html.escape(s["line"])}<br>{html.escape(s["line_cn"])}</sub></td>')
            out.append('</tr>')
        out.append('</table>')
    return '\n'.join(out) + '\n'


for fn in ('README.md',):
    p = os.path.join(ROOT, fn)
    if not os.path.exists(p) or site: continue
    t = open(p, encoding='utf-8').read()
    t2 = re.sub(r'(<!-- styles:start -->\n).*?(<!-- styles:end -->)', lambda m: m.group(1) + readme_grid() + m.group(2), t, flags=re.S)
    if t2 != t: open(p, 'w', encoding='utf-8').write(t2)

print(f'{len(styles)} styles ({n_vid} with film, {minutes:.0f} min) → {os.path.relpath(os.path.join(out_dir, "index.html"), ROOT)}')
for s in styles:
    if not s['imgs']: print('  no image:', s['slug'])
    if not s.get('line'): print('  no card copy (cards.json):', s['slug'])
