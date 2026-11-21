# Run: python3 tests/run.py   (needs: pip install playwright && playwright install chromium)
import json,os,sys
from playwright.sync_api import sync_playwright
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cases=json.load(open(os.path.join(root,'tests','phrases.json')))
fails=0
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file://'+os.path.join(root,'index.html'))
    for c in cases:
        pg.evaluate("localStorage.clear();S={lines:[],threads:{},acted:{},pinned:{},rhythms:{}};uid=1")
        try:
            r=pg.evaluate("(t)=>{add(t);const l=S.lines[S.lines.length-1];return {type:l.type,m:meaning(l,NOW())||'',people:l.f.people||[]}}",c['in'])
        except Exception as e:
            r={'type':'CRASH','m':str(e)[:80],'people':[]}
        ok=r['type']==c['type'] and c.get('has','') in r['m'] and not (c.get('nopeople') and r['people'])
        if not ok: fails+=1;print('FAIL',repr(c['in']),'→',r['type'],'|',r['m'],r['people'])
    if errs: fails+=1;print('PAGE ERRORS',errs)
    b.close()
print(f"{len(cases)-fails}/{len(cases)} passed");sys.exit(1 if fails else 0)
