import os

def svg(w, h, defs, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>{defs}</defs>
{body}
</svg>'''

def grain():
    return ('<filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/>'
            '<feColorMatrix type="saturate" values="0"/><feComponentTransfer>'
            '<feFuncA type="linear" slope=".08"/></feComponentTransfer>'
            '<feComposite operator="over" in2="SourceGraphic"/></filter>')

def save(name, content):
    os.makedirs("img", exist_ok=True)
    with open(f"img/{name}.svg", "w", encoding="utf-8") as f:
        f.write(content)

W, H = 640, 420

def base(c1, c2):
    return (f'<linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient>',)

def noise_rect():
    return f'<rect width="{W}" height="{H}" filter="url(#n)" fill="transparent"/>'

# 1 Инструмент: шуруповёрт
d, = base("#c2571b", "#7a2e0e")
body = f'''<rect width="{W}" height="{H}" fill="url(#g)"/>
<rect x="250" y="120" width="150" height="90" rx="14" fill="#f2e7c9"/>
<rect x="280" y="205" width="55" height="120" rx="12" fill="#f2e7c9"/>
<rect x="400" y="145" width="70" height="24" rx="8" fill="#f2e7c9"/>
<circle cx="292" cy="165" r="12" fill="#7a2e0e"/><circle cx="325" cy="165" r="12" fill="#7a2e0e"/>
<circle cx="540" cy="90" r="60" fill="#f2e7c9" opacity=".14"/>
{noise_rect()}'''
save("shop1", svg(W, H, d + grain(), body))

# 2 Краска: ведро + капля
d, = base("#14406b", "#0a1e33")
body = f'''<rect width="{W}" height="{H}" fill="url(#g)"/>
<path d="M 220 170 h 200 l -20 160 a 24 24 0 0 1 -24 20 h -112 a 24 24 0 0 1 -24 -20 z" fill="#bfe3f2"/>
<ellipse cx="320" cy="170" rx="100" ry="18" fill="#7fd0ff"/>
<path d="M 470 90 q 30 55 0 85 q -30 -30 0 -85" fill="#7fd0ff"/>
<rect x="215" y="140" width="210" height="14" rx="7" fill="#7fd0ff"/>
<circle cx="130" cy="320" r="65" fill="#7fd0ff" opacity=".12"/>
{noise_rect()}'''
save("shop2", svg(W, H, d + grain(), body))

# 3 Плитка: ромбовидная кладка
d, = base("#2c6e3f", "#123a20")
rows = ""
for r in range(6):
    for c in range(8):
        x = 40 + c * 80 + (r % 2) * 40
        y = 40 + r * 66
        rows += f'<path d="M {x} {y} l 40 24 l -40 24 l -40 -24 z" fill="#f2e7c9" opacity="{0.9 if (r+c)%3 else 0.55}"/>'
body = f'''<rect width="{W}" height="{H}" fill="url(#g)"/>
{rows}
{noise_rect()}'''
save("shop3", svg(W, H, d + grain(), body))

# 4 Сантехника: кран + труба
d, = base("#4a2c1a", "#221209")
body = f'''<rect width="{W}" height="{H}" fill="url(#g)"/>
<path d="M 180 150 h 180 q 60 0 60 60 v 30" fill="none" stroke="#f2e7c9" stroke-width="34" stroke-linecap="round"/>
<rect x="150" y="130" width="60" height="60" rx="10" fill="#f2e7c9"/>
<circle cx="180" cy="110" r="26" fill="#e8a13a"/>
<path d="M 420 260 q 10 40 -10 70 M 420 260 q -10 45 12 75" stroke="#7fd0ff" stroke-width="10" fill="none" stroke-linecap="round"/>
<circle cx="520" cy="120" r="50" fill="#f2e7c9" opacity=".12"/>
{noise_rect()}'''
save("shop4", svg(W, H, d + grain(), body))

# 5 Электрика: розетка + молния
d, = base("#1a1a1a", "#3d3d3d")
body = f'''<rect width="{W}" height="{H}" fill="url(#g)"/>
<circle cx="320" cy="210" r="125" fill="#f5f5f5"/>
<circle cx="320" cy="210" r="95" fill="none" stroke="#1a1a1a" stroke-width="6"/>
<circle cx="285" cy="180" r="10" fill="#1a1a1a"/><circle cx="355" cy="180" r="10" fill="#1a1a1a"/>
<circle cx="285" cy="245" r="10" fill="#1a1a1a"/><circle cx="355" cy="245" r="10" fill="#1a1a1a"/>
<path d="M 330 130 l -30 55 h 25 l -20 50 l 55 -70 h -28 l 25 -35 z" fill="#e8c547"/>
<circle cx="120" cy="110" r="48" fill="#e8c547" opacity=".7"/>
{noise_rect()}'''
save("shop5", svg(W, H, d + grain(), body))

# 6 Пиломатериалы: доски
d, = base("#d2691e", "#8a3a12")
boards = "".join(f'<g transform="translate({40+i*16},{60+i*46}) rotate(-8 140 30)"><rect width="280" height="46" rx="6" fill="#f2c14e"/><line x1="20" y1="12" x2="260" y2="12" stroke="#8a3a12" stroke-width="4" opacity=".4"/><line x1="20" y1="34" x2="260" y2="34" stroke="#8a3a12" stroke-width="4" opacity=".4"/></g>' for i in range(6))
body = f'''<rect width="{W}" height="{H}" fill="url(#g)"/>
{boards}
<circle cx="530" cy="90" r="55" fill="#f2c14e" opacity=".2"/>
{noise_rect()}'''
save("shop6", svg(W, H, d + grain(), body))

# 7 Крепёж: гайка
d, = base("#1e3a5f", "#0c1c30")
body = f'''<rect width="{W}" height="{H}" fill="url(#g)"/>
<polygon points="320,90 438,158 438,262 320,330 202,262 202,158" fill="#bfe3f2"/>
<circle cx="320" cy="210" r="62" fill="#0c1c30"/>
<circle cx="320" cy="210" r="62" fill="none" stroke="#bfe3f2" stroke-width="10" stroke-dasharray="14 12"/>
<circle cx="130" cy="120" r="46" fill="#bfe3f2" opacity=".18"/>
<circle cx="520" cy="320" r="34" fill="#bfe3f2" opacity=".14"/>
{noise_rect()}'''
save("shop7", svg(W, H, d + grain(), body))

# 8 Окна: окно с рамой
d, = base("#3a1a5f", "#150a26")
body = f'''<rect width="{W}" height="{H}" fill="url(#g)"/>
<rect x="170" y="80" width="300" height="260" fill="#bfe3f2"/>
<line x1="320" y1="80" x2="320" y2="340" stroke="#150a26" stroke-width="12"/>
<line x1="170" y1="210" x2="470" y2="210" stroke="#150a26" stroke-width="12"/>
<rect x="170" y="80" width="300" height="260" fill="none" stroke="#f2e7c9" stroke-width="18"/>
<path d="M 200 130 l 60 -30 M 230 160 l 50 -25" stroke="#ffffff" stroke-width="8" opacity=".7"/>
<circle cx="520" cy="100" r="40" fill="#e8c547" opacity=".6"/>
{noise_rect()}'''
save("shop8", svg(W, H, d + grain(), body))

# 9 Сыпучие/камень: куча щебня + кирпичи
d, = base("#a3271b", "#5e130c")
rocks = "".join(f'<circle cx="{230+i*38}" cy="{330-(i%3)*22}" r="26" fill="#d9cfc0" opacity=".95"/>' for i in range(6))
body = f'''<rect width="{W}" height="{H}" fill="url(#g)"/>
<path d="M 150 340 Q 320 150 490 340 Z" fill="#d9cfc0" opacity=".5"/>
{rocks}
<g transform="translate(430,110) rotate(6)"><rect width="120" height="54" fill="#f2c14e"/><line x1="0" y1="27" x2="120" y2="27" stroke="#5e130c" stroke-width="5"/></g>
<g transform="translate(452,168) rotate(-4)"><rect width="120" height="54" fill="#f2c14e"/><line x1="0" y1="27" x2="120" y2="27" stroke="#5e130c" stroke-width="5"/></g>
{noise_rect()}'''
save("shop9", svg(W, H, d + grain(), body))

def rent(name, c1, c2, inner):
    d, = base(c1, c2)
    body = f'<rect width="{W}" height="{H}" fill="url(#g)"/>\n{inner}\n{noise_rect()}'
    save(name, svg(W, H, d + grain(), body))

# аренда 1: торговый ряд (витрины)
rent("rent1", "#5f4a1e", "#2b2008",
     '<path d="M 80 340 v -140 a 60 60 0 0 1 120 0 v 140 z" fill="#f2e7c9" opacity=".9"/>'
     '<path d="M 260 340 v -140 a 60 60 0 0 1 120 0 v 140 z" fill="#f2e7c9" opacity=".7"/>'
     '<path d="M 440 340 v -140 a 60 60 0 0 1 120 0 v 140 z" fill="#f2e7c9" opacity=".5"/>'
     '<rect x="60" y="340" width="520" height="14" fill="#f2e7c9" opacity=".4"/>')

# аренда 2: склад/эскалатор накладная
rent("rent2", "#1e4a5f", "#0a2230",
     '<path d="M 120 90 h 90 v 80 h 90 v 80 h 90 v 80 h 90 v 40" fill="none" stroke="#bfe3f2" stroke-width="26"/>'
     '<path d="M 120 90 h 90 v 80 h 90 v 80 h 90 v 80 h 90 v 40" fill="none" stroke="#0a2230" stroke-width="6" stroke-dasharray="10 22"/>'
     '<circle cx="500" cy="120" r="46" fill="#bfe3f2" opacity=".3"/>')

# аренда 3: офис
rent("rent3", "#3d3d3d", "#161616",
     '<rect x="140" y="100" width="360" height="220" fill="#e8e4da" opacity=".92"/>'
     '<line x1="140" y1="165" x2="500" y2="165" stroke="#3d3d3d" stroke-width="8"/>'
     '<line x1="140" y1="230" x2="500" y2="230" stroke="#3d3d3d" stroke-width="8"/>'
     '<line x1="140" y1="295" x2="500" y2="295" stroke="#3d3d3d" stroke-width="8"/>'
     '<line x1="320" y1="100" x2="320" y2="320" stroke="#3d3d3d" stroke-width="8"/>'
     '<circle cx="470" cy="355" r="30" fill="#d2401e"/>')

# аренда 4: большой блок — складские стеллажи
shelv = "".join(f'<g transform="translate({80+i*130},90)"><rect width="100" height="250" fill="none" stroke="#f2c14e" stroke-width="10"/>' + "".join(f'<rect x="8" y="{14+j*58}" width="84" height="36" fill="#f2c14e" opacity="{.85-.12*j}"/>' for j in range(4)) + '</g>' for i in range(4))
rent("rent4", "#6b1a2a", "#2b080e", shelv +
     '<rect x="60" y="345" width="520" height="12" fill="#f2c14e" opacity=".3"/>')

print("ok:", sorted(f for f in os.listdir("img") if f.endswith(".svg")))
