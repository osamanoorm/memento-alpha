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
    # connections: older line (a day ago) comes back when a related line is written
    conns=[("try that new sushi place","dinner sat?",True),("watch Dune part two","movie tonight?",True),("Hooked by Nir Eyal book","ordering from daraz",True),
           ("oil changed at 68,946 km","car service next week",True),("Ali owes me 2000","dinner sat?",False),("netflix password abc pass99","watch something",False)]
    for old,new,want in conns:
        pg.evaluate("localStorage.clear();S={lines:[],threads:{},acted:{},pinned:{},rhythms:{},snooze:{}};uid=1")
        got=pg.evaluate("([a,b])=>{add(a);S.lines[0].ts=new Date(+S.lines[0].ts-864e5);add(b);return !!S.lines[1].conn}",[old,new])
        if got!=want: fails+=1;print('FAIL connection',repr(old),'→',repr(new),'got',got)
    # Done closes the old line; it never comes back
    pg.evaluate("localStorage.clear();S={lines:[],threads:{},acted:{},pinned:{},rhythms:{},snooze:{}};uid=1")
    r=pg.evaluate("()=>{add('try that new sushi place');S.lines[0].ts=new Date(+S.lines[0].ts-864e5);add('dinner sat?');S.acted['cn'+S.lines[1].id]='Done';S.lines[0].done=true;S.lines[1].ts=new Date(+S.lines[1].ts-864e5);add('lunch out tomorrow');return !!S.lines[2].conn}")
    if r: fails+=1;print('FAIL done line came back')
    cases=cases+[0]*7
    if errs: fails+=1;print('PAGE ERRORS',errs)
    b.close()
print(f"{len(cases)-fails}/{len(cases)} passed");sys.exit(1 if fails else 0)
