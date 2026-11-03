"""Render self-contained SVG panels; no network or dependencies."""
from pathlib import Path
from html import escape
A = Path(__file__).resolve().parents[1] / 'assets'
A.mkdir(exist_ok=True)
BG, FG, MUTED, ACCENT, LINE = '#0b111b', '#e6edf7', '#9aacc3', '#66e0ce', '#243448'
def t(x,y,s,size=22,c=FG,bold=False):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{c}" font-weight="{700 if bold else 400}">{escape(s)}</text>'
def shell(w,h,title,desc):
 return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>', '<style>text{font-family:"DejaVu Sans Mono","Liberation Mono",Consolas,monospace}.cursor{animation:blink 1.4s steps(1,end) infinite}@keyframes blink{0%,45%{opacity:1}46%,90%{opacity:0}91%,100%{opacity:1}}@media(prefers-reduced-motion:reduce){.cursor{animation:none}}</style>',f'<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="16" fill="{BG}" stroke="{LINE}" stroke-width="2"/>',f'<path d="M1 64H{w-1}" stroke="{LINE}"/>','<circle cx="30" cy="33" r="6" fill="#f07888"/><circle cx="52" cy="33" r="6" fill="#eac17b"/><circle cx="74" cy="33" r="6" fill="#66e0ce"/>',t(108,40,title,18,MUTED)]
def save(name,p): (A/name).write_text('\n'.join(p+['</svg>'])+'\n')
for mobile in (False,True):
 w,h=(600,520) if mobile else (1040,448)
 p=shell(w,h,'zyzycode@github: ~','Backend and LLM engineer. Python, Go, TypeScript. RAG, MCP and Llama. APIs, event-driven systems and AI applications.')
 p += [t(32,112,'$ whoami',22,ACCENT),t(32,170,'zyzycode',48 if mobile else 58,FG,True),t(32,216,'Backend & LLM Engineer',26 if mobile else 30,ACCENT)]
 lines=['Build the backend.','Make AI useful.','Ship the whole thing.'] if mobile else ['Build the backend. Make AI useful.','Ship the whole thing.']
 for i,line in enumerate(lines): p.append(t(32,277+i*36,line,27))
 p += [t(32,411 if mobile else 367,'Python / Go / TypeScript',22,MUTED),t(32,466 if mobile else 415,'$ explore ./projects',22,ACCENT),f'<rect class="cursor" x="310" y="{445 if mobile else 394}" width="12" height="26" fill="{ACCENT}"/>']
 if not mobile:
  for y,label in [(123,'API'),(219,'QUEUE'),(315,'DATA')]: p += [f'<rect x="831" y="{y}" width="157" height="56" rx="8" fill="#122334"/>',t(854,y+36,label,23,ACCENT)]
  p.append(f'<path d="M909 179v40m0 56v40" stroke="{ACCENT}" stroke-width="2" stroke-dasharray="5 6"/>')
 save('header-mobile.svg' if mobile else 'header.svg',p)
ROWS=[('AI / LLM',['RAG · MCP · Llama','LLM integration · AI applications']),('LANGUAGES',['Python · Go · TypeScript · SQL','Bash · asyncio']),('BACKEND / APIs',['FastAPI · Django · Flask','REST API · JSON API · gRPC']),('ASYNC / EVENTS',['RabbitMQ · Celery · FastStream','Event-driven architecture']),('DATA / STORAGE',['PostgreSQL · ClickHouse · MongoDB','Redis · SQLAlchemy · Alembic']),('QUALITY / SPEED',['pytest · Selenium · Postman','Performance & code optimization']),('PLATFORM / TOOLS',['Linux · Docker · CI/CD · Git','GitHub · GitLab · Bash · PyCharm']),('CLIENT / GAMES',['React · Electron · Vite · Phaser','Desktop apps · Game systems'])]
for mobile in (False,True):
 w,h=(600,1534) if mobile else (1040,1000)
 p=shell(w,h,'stack --grouped','Engineering skills by domain. A complete text version is provided in the README below.')
 p.append(t(32,112,'$ cat stack.yml',22,ACCENT))
 for i,(label,lines) in enumerate(ROWS):
  y=166+i*(168 if mobile else 100)
  p.append(t(32,y,label,21 if mobile else 19,ACCENT,True))
  for j,line in enumerate(lines): p.append(t(32 if mobile else 310,y+(42+j*36 if mobile else j*33),line,24 if mobile else 23))
  if i<7: p.append(f'<path d="M32 {y+(126 if mobile else 62)}H{w-32}" stroke="{LINE}"/>')
 p.append(t(32,h-32,'$ less stack.txt  # text version below',18,MUTED))
 save('stack-mobile.svg' if mobile else 'stack.svg',p)
print('Rendered four profile panels')
