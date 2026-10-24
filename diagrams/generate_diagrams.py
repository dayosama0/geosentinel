"""Editable source for the three diploma architecture SVG/PNG diagrams.
Run: python generate_diagrams.py
Dependencies: svgwrite, cairosvg
"""
from pathlib import Path
import svgwrite, cairosvg
P = Path(__file__).resolve().parent
P.mkdir(exist_ok=True)
NAVY='#18334D'; TEXT='#244057'; MUTED='#607589'; BLUE='#eaf3ff'; BLUE_BORDER='#91b9dc'; TEAL='#e6f6f1'; TEAL_BORDER='#54ac96'; GOLD='#fff4e8'; GOLD_BORDER='#dda96d'; PURPLE='#f1effa'; PURPLE_BORDER='#b3a7d5'; PALE='#f7fafc'; GRAY='#ccd7df'

def init(name,title,sub='',height=880):
 d=svgwrite.Drawing(str(P/name), size=('1500px',f'{height}px'), viewBox=f'0 0 1500 {height}', profile='full')
 d.add(d.rect(insert=(0,0),size=(1500,height), fill='white'))
 d.add(d.text(title, insert=(55,48), font_size=26, font_weight='bold', font_family='DejaVu Sans,Arial',fill=NAVY))
 if sub: d.add(d.text(sub,insert=(55,75),font_size=14,font_family='DejaVu Sans,Arial',fill=MUTED))
 m=d.marker(id='arrow', insert=(9,5), size=(10,10), orient='auto', markerUnits='strokeWidth'); m.add(d.path(d='M 1,1 L 9,5 L 1,9 Z', fill='#648296')); d.defs.add(m)
 return d

def box(d,x,y,w,h,lines,fill=BLUE,stroke=BLUE_BORDER,fs=17,r=14,weight='normal'):
 d.add(d.rect(insert=(x,y),size=(w,h),rx=r,ry=r,fill=fill,stroke=stroke,stroke_width=1.7))
 lineh=fs*1.4
 sy=y+h/2-(len(lines)-1)*lineh/2+fs*.34
 for i,s in enumerate(lines):
  d.add(d.text(s,insert=(x+w/2,sy+i*lineh),text_anchor='middle',font_size=fs,fill=TEXT,font_weight=weight if i==0 else 'normal',font_family='DejaVu Sans,Arial'))

def text(d,x,y,label,size=14,color=TEXT,weight='normal',anchor='start'):
 d.add(d.text(label,insert=(x,y),font_family='DejaVu Sans,Arial',font_size=size,fill=color,font_weight=weight,text_anchor=anchor))

def line(d,points,arrow=False,style='solid',color='#708DA1',width=1.7):
 p=' '.join(f'{x},{y}' for x,y in points)
 kwargs=dict(points=points,fill='none',stroke=color,stroke_width=width,stroke_linejoin='round');
 if style=='dashed': kwargs['stroke_dasharray']='7 5'
 if arrow: kwargs['marker_end']='url(#arrow)'
 d.add(d.polyline(**kwargs))

def save(d):
 d.save()
 cairosvg.svg2png(url=d.filename,write_to=str(Path(d.filename).with_suffix('.png')),scale=1.65)

# SYSTEM CONTEXT
D=init('01_system_context.svg','SYSTEM CONTEXT DIAGRAM','External actors and data providers vs. one prototype system boundary',height=800)
D.add(D.rect(insert=(488,213),size=(524,368),rx=22,ry=22,fill=TEAL,stroke=TEAL_BORDER,stroke_width=2.4))
text(D,750,264,'UNAUTHORIZED LANDFILL',23,NAVY,'bold','middle')
text(D,750,299,'MONITORING PROTOTYPE',23,NAVY,'bold','middle')
text(D,750,341,'Satellite detection + geospatial matching',17,TEXT,anchor='middle')
text(D,750,370,'Verification missions + cleanup history',17,TEXT,anchor='middle')
text(D,750,399,'Controlled model feedback + re-dumping alerts',16,TEXT,anchor='middle')
D.add(D.line(start=(538,442),end=(962,442),stroke=TEAL_BORDER,stroke_width=1.2))
text(D,750,481,'System under development — no government integration',14,MUTED,anchor='middle')
box(D,56,145,358,96,['CITIZEN / VOLUNTEER','Photo + location report, status'],fs=15)
box(D,56,322,358,96,['AUTHORIZED INSPECTOR','Evidence, missions, clearance'],fs=15)
box(D,56,499,358,96,['ADMIN / ML OPERATOR','Curate datasets, approve models'],fs=15)
box(D,1086,145,358,96,['LICENSED SATELLITE IMAGERY','GeoTIFF + CRS + acquisition date'],GOLD,GOLD_BORDER,fs=15)
box(D,1086,322,358,96,['RESEARCH DATASETS','SWAD / compatible annotated images'],GOLD,GOLD_BORDER,fs=15)
box(D,1086,499,358,96,['BASEMAP / TILE PROVIDER','Third-party tiles under license'],GOLD,GOLD_BORDER,fs=15)
line(D,[(414,193),(449,193),(449,290),(488,290)],arrow=True)
line(D,[(414,370),(488,370)],arrow=True)
line(D,[(414,547),(449,547),(449,504),(488,504)],arrow=True)
line(D,[(1086,193),(1051,193),(1051,290),(1012,290)],arrow=True)
line(D,[(1086,370),(1012,370)],arrow=True)
line(D,[(1086,547),(1051,547),(1051,504),(1012,504)],arrow=True)
text(D,54,688,'Boundary note:',15,NAVY,'bold')
text(D,198,688,'Imagery access and redistribution rights are not yet confirmed. Government agency connections are out of MVP scope.',14,MUTED)
text(D,54,722,'Data note:',15,NAVY,'bold')
text(D,154,722,'Training JPEGs may lack georeferencing; map positions require separate trusted geospatial metadata.',14,MUTED)
save(D)

# USE CASE
D=init('02_use_case.svg','USE CASE DIAGRAM','Three prototype roles and their major user goals (association lines grouped by role)',height=940)
D.add(D.rect(insert=(300,110),size=(1140,760),rx=18,ry=18,fill='#FBFDFC',stroke='#7EB5A3',stroke_width=2))
text(D,870,143,'Unauthorized Landfill Monitoring System',19,NAVY,'bold','middle')
# Role band tint inside system
for top,bottom,fill in [(167,334,'#f3f8ff'),(351,654,'#f2faf7'),(671,845,'#fbf8ef')]:
 D.add(D.rect(insert=(324,top),size=(1090,bottom-top),rx=12,ry=12,fill=fill,stroke='none'))
# Actors drawn as stick persons

def actor(d,x,y,label):
 d.add(d.circle(center=(x,y-30),r=16,fill='white',stroke=NAVY,stroke_width=2.6))
 d.add(d.line(start=(x,y-14),end=(x,y+37),stroke=NAVY,stroke_width=2.6))
 d.add(d.line(start=(x-29,y+3),end=(x+29,y+3),stroke=NAVY,stroke_width=2.6))
 d.add(d.line(start=(x,y+37),end=(x-22,y+64),stroke=NAVY,stroke_width=2.6))
 d.add(d.line(start=(x,y+37),end=(x+22,y+64),stroke=NAVY,stroke_width=2.6))
 text(d,x,y+95,label,17,NAVY,'bold','middle')
actor(D,150,202,'Citizen')
actor(D,150,445,'Inspector')
actor(D,150,718,'Admin / ML')
# Use cases grouped into 3 rows, with local role routing
coordsC=[(525,216),(875,216),(1225,216)]
coordsI=[(525,414),(875,414),(1225,414),(525,561),(875,561),(1225,561)]
coordsA=[(459,731),(723,731),(987,731),(1251,731)]
# Association lines: a per-role bus above the ellipses; no false links between use cases.
# Citizen
line(D,[(218,209),(268,209),(268,158),(1225,158)],color='#A0BBD8',width=1.6)
for cx,cy in coordsC: line(D,[(cx,158),(cx,cy-53)],color='#A0BBD8',width=1.6)
# Inspector (two rows)
line(D,[(218,457),(277,457),(277,341),(1225,341)],color='#89B9A9',width=1.6)
line(D,[(277,457),(277,492),(1225,492)],color='#89B9A9',width=1.6)
for cx,cy in coordsI[:3]: line(D,[(cx,341),(cx,cy-53)],color='#89B9A9',width=1.6)
for cx,cy in coordsI[3:]: line(D,[(cx,492),(cx,cy-53)],color='#89B9A9',width=1.6)
# ML operator
line(D,[(218,730),(278,730),(278,662),(1251,662)],color='#D3B27D',width=1.6)
for cx,cy in coordsA: line(D,[(cx,662),(cx,cy-53)],color='#D3B27D',width=1.6)

def uc(cx,cy,lines,edge,rx=142):
 D.add(D.ellipse(center=(cx,cy),r=(rx,53),fill='#fff',stroke=edge,stroke_width=2))
 sy=cy-6 if len(lines)==2 else cy+5
 for j,l in enumerate(lines): text(D,cx,sy+j*23,l,14,TEXT,'normal','middle')
for (x,y),lines in zip(coordsC,[['Submit geolocated','citizen report'],['Track permitted','report status'],['Explore monitored','locations']]): uc(x,y,lines,BLUE_BORDER)
for (x,y),lines in zip(coordsI,[['Review evidence','match candidates'],['Manage verification','missions'],['Record verification','and evidence'],['Record cleared','site / cleanup'],['Review re-dumping','alerts'],['Inspect monitoring','history']]): uc(x,y,lines,TEAL_BORDER)
for (x,y),lines in zip(coordsA,[['Import imagery;','run detection'],['Curate / export','reviewed samples'],['Retrain / evaluate;','approve model'],['Manage access','and user roles']]): uc(x,y,lines,GOLD_BORDER,rx=120)
text(D,50,913,'Note: system uses authenticated inspector/operator roles; citizen reporting need not require registration.',14,MUTED)
save(D)

# COMPONENT
D=init('03_component.svg','COMPONENT DIAGRAM','Logical responsibilities and data flows; no mandatory external government integration',height=1150)
# visual group panels
panels=[(45,102,1410,166,'PRESENTATION  —  React + TypeScript PWA',BLUE,BLUE_BORDER),(45,290,1410,283,'BACKEND  —  FastAPI (RBAC + validation)',TEAL,TEAL_BORDER),(45,595,1410,246,'ASYNC / OFFLINE PROCESSING  —  Python + PyTorch + Rasterio',GOLD,GOLD_BORDER),(45,866,1410,190,'PERSISTENCE  —  PostGIS and protected artifacts',PURPLE,PURPLE_BORDER)]
for x,y,w,h,label,fill,stroke in panels:
 D.add(D.rect(insert=(x,y),size=(w,h),rx=16,ry=16,fill=fill,stroke=stroke,stroke_width=1.5))
 text(D,x+20,y+31,label,17,NAVY,'bold')
# presentation
box(D,87,166,385,73,['Citizen reporting','photos + geolocation'],fill='#fff',stroke=BLUE_BORDER,fs=15)
box(D,559,166,385,73,['Inspector dashboard','missions + evidence + alerts'],fill='#fff',stroke=BLUE_BORDER,fs=15)
box(D,1030,166,385,73,['Admin / ML operator UI','datasets + model approval'],fill='#fff',stroke=BLUE_BORDER,fs=15)
# backend gateway
box(D,520,346,460,61,['REST API gateway  •  authentication / RBAC'],fill='#d5f1e5',stroke=TEAL_BORDER,fs=15)
for cx in [280,751,1223]: line(D,[(cx,239),(cx,270),(750,270),(750,346)],arrow=True,color='#7399b3',width=1.6)
backend=[(89,'Observations + locations','reports / geo / evidence'),(438,'Evidence association','candidate matches / review'),(787,'Verification + alerts','missions / cleanup / recurrence'),(1136,'ML orchestration','jobs / model approval')]
for x,t1,t2 in backend:
 box(D,x,462,277,76,[t1,t2],fill='white',stroke=TEAL_BORDER,fs=14)
 line(D,[(750,407),(750,437),(x+139,437),(x+139,462)],arrow=True,color='#69968A',width=1.3)
# process jobs
box(D,105,656,345,102,['Raster tiling + inference','GeoTIFF CRS / affine -> boxes'],fill='white',stroke=GOLD_BORDER,fs=15)
box(D,578,656,345,102,['Reviewed data export','annotations + versioned manifest'],fill='white',stroke=GOLD_BORDER,fs=15)
box(D,1050,656,345,102,['Controlled offline retraining','fixed held-out test + promotion'],fill='white',stroke=GOLD_BORDER,fs=15)
line(D,[(1275,538),(1275,597),(279,597),(279,656)],arrow=True,color='#A58B64')
line(D,[(1275,538),(1275,614),(750,614),(750,656)],arrow=True,color='#A58B64')
line(D,[(1275,538),(1275,639),(1222,639),(1222,656)],arrow=True,color='#A58B64')
# storage
box(D,90,936,381,78,['PostgreSQL + PostGIS','features / events / audit history'],fill='white',stroke=PURPLE_BORDER,fs=15)
box(D,558,936,381,78,['Restricted file storage','licensed rasters + citizen photos'],fill='white',stroke=PURPLE_BORDER,fs=15)
box(D,1027,936,381,78,['Versioned ML artifacts','manifests + model checkpoints'],fill='white',stroke=PURPLE_BORDER,fs=15)
# Service repository access is routed outside the panels to avoid crossing processing modules.
line(D,[(230,538),(22,538),(22,975),(90,975)],arrow=True,color='#998ab6',width=1.7)
# ML jobs persist source rasters, curated datasets, and model artifacts.
line(D,[(279,758),(279,821),(750,821),(750,936)],arrow=True,color='#A58B64')
line(D,[(750,758),(750,936)],arrow=True,color='#A58B64')
line(D,[(1222,758),(1222,936)],arrow=True,color='#A58B64')
# Opaque title strips keep arrows from running through panel headings.
D.add(D.rect(insert=(55,596),size=(615,41),fill=GOLD,stroke='none'))
text(D,61,626,'ASYNC / OFFLINE PROCESSING  —  Python + PyTorch + Rasterio',17,NAVY,'bold')
D.add(D.rect(insert=(55,867),size=(622,42),fill=PURPLE,stroke='none'))
text(D,61,897,'PERSISTENCE  —  PostGIS and protected artifacts',17,NAVY,'bold')
text(D,55,1091,'External interfaces: licensed satellite GeoTIFF imports and basemap tiles; third-party imagery is not part of the system.',14,MUTED)
text(D,55,1120,'Safety: observation provenance is retained; operator reviews model promotion; old imagery cannot trigger a recurrence alert by upload date alone.',14,MUTED)
save(D)
print('Created SVG and PNG diagrams in',P)
