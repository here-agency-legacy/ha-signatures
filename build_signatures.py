import json, html, os, sys
OUT = sys.argv[1]
CDN = "https://pirhda.stripocdn.email/content/guids/CABINET_308c3da5d12f2a8c4bff7867edb4a615/images/"
TEAM = [
 # file stem, name, title, phone display, tel, email
 ("Lincoln_Assis",      "Lincoln Assis",      "Managing Partner",      "0401 495 143", "+61401495143", "lincoln@wearehere.digital"),
 ("Kevin_Berot",        "Kevin Berot",        "Managing Partner",      "0432 736 197", "+61432736197", "kev@wearehere.digital"),
 ("Brodie_Edwards",     "Brodie Edwards",     "Creative Director",     None,           None,           "brodie@wearehere.digital"),
 ("Carolina_Magalhaes", "Carolina Magalhaes", "Project Manager",       "0402 212 509", "+61402212509", "carol@wearehere.digital"),
 ("Lucia_Baldi",        "Lucia Baldi",        "Designer",              None,           None,           "lucia@wearehere.digital"),
 ("Marcus_Nascimento",  "Marcus Nascimento",  "Marketing Coordinator", "0452 460 824", "+61452460824", "marcus@wearehere.digital"),
 ("Do_Viet_Liem",       "Do Viet Liem",       "Lead Web Engineer",     None,           None,           "liemdo@wearehere.digital"),
 ("Ernest_Pineda",      "Ernest Pineda",      "Web Developer",         None,           None,           "ernest@wearehere.digital"),
 ("Marbien_Parel",      "Marbien Parel",      "Sr. QA Engineer",       None,           None,           "marbien@wearehere.digital"),
 ("Nam_Bui",            "Nam Bui",            "Sr. UI/UX Designer",    None,           None,           "nam@wearehere.digital"),
 ("Thai_Thi_Yen_Nhi",   "Thai Thi Yen Nhi",   "Web Developer",         None,           None,           "nhi@wearehere.digital"),
]
FONT = "Arial,'Helvetica Neue',Helvetica,sans-serif"
LINK = f"color:#ffffff;text-decoration:none;font-family:{FONT};font-size:12px;line-height:18px;"

def sig(name, title, phone, tel, email):
    e = html.escape
    lines = []
    if phone:
        lines.append(f'<a href="tel:{tel}" style="{LINK}">{e(phone)}</a>')
    lines.append(f'<a href="mailto:{email}" style="{LINK}">{e(email)}</a>')
    lines.append(f'<a href="https://wearehere.digital/" style="{LINK}">wearehere.digital</a>')
    contact = "<br>".join(lines)
    return f'''<table cellpadding="0" cellspacing="0" border="0" width="600" bgcolor="#131415" style="width:100%;max-width:600px;background-color:#131415;border-collapse:collapse;border-spacing:0;">
<tr>
<td align="center" valign="middle" bgcolor="#131415" style="padding:0;background-color:#131415;font-size:0;line-height:0;text-align:center;">
<div style="display:inline-block;width:100%;max-width:340px;vertical-align:middle;text-align:left;">
<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;border-spacing:0;">
<tr>
<td width="100" valign="top" style="width:100px;padding:5px 15px 5px 5px;font-size:0;line-height:0;"><a href="https://wearehere.digital/" style="text-decoration:none;"><img src="{CDN}emailgif.gif" alt="Here Agency" width="100" height="200" style="display:block;width:100px;height:200px;border:0;outline:none;"></a></td>
<td valign="top" style="padding:25px 5px 12px 0;">
<p style="margin:0;font-family:{FONT};font-size:24px;line-height:29px;font-weight:normal;color:#ffffff;">{e(name)}</p>
<p style="margin:5px 0 0 0;font-family:{FONT};font-size:12px;line-height:18px;color:#bababa;">{e(title)}</p>
<p style="margin:30px 0 0 0;font-family:{FONT};font-size:12px;line-height:18px;color:#ffffff;">{contact}</p>
<table cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse;border-spacing:0;margin-top:10px;">
<tr>
<td style="padding:0 10px 0 0;font-size:0;line-height:0;"><a href="https://www.instagram.com/here_agency/" style="text-decoration:none;"><img src="{CDN}igemail.png" alt="Instagram" width="24" height="24" style="display:block;width:24px;height:24px;border:0;outline:none;"></a></td>
<td style="padding:0;font-size:0;line-height:0;"><a href="https://www.linkedin.com/company/here-agency/" style="text-decoration:none;"><img src="{CDN}inemail.png" alt="LinkedIn" width="24" height="24" style="display:block;width:24px;height:24px;border:0;outline:none;"></a></td>
</tr>
</table>
</td>
</tr>
</table>
</div><div style="display:inline-block;width:100%;max-width:260px;vertical-align:middle;text-align:center;">
<table cellpadding="0" cellspacing="0" border="0" width="100%" style="border-collapse:collapse;border-spacing:0;">
<tr>
<td align="center" style="padding:24px 0 12px 0;font-size:0;line-height:0;"><a href="https://wearehere.digital/" style="text-decoration:none;"><img src="{CDN}herelogo.png" alt="Here Agency" width="195" height="39" style="display:block;width:195px;height:39px;border:0;outline:none;margin:0 auto;"></a></td>
</tr>
<tr>
<td align="center" style="padding:0 0 24px 0;"><p style="margin:0;font-family:{FONT};font-size:12px;line-height:18px;color:#bababa;text-align:center;">Your digital transformation is Here.</p></td>
</tr>
</table>
</div>
</td>
</tr>
</table>'''

os.makedirs(f"{OUT}/signatures", exist_ok=True)
data = []
for stem, name, title, phone, tel, email in TEAM:
    s = sig(name, title, phone, tel, email)
    # standalone file: open in a browser, select all, copy, paste into Gmail
    doc = f'<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(name)} | Here Agency signature</title></head>\n<body style="margin:0;padding:24px;background:#ffffff;">\n<!-- SIGNATURE START -->\n{s}\n<!-- SIGNATURE END -->\n</body></html>\n'
    open(f"{OUT}/signatures/{stem}.html", "w").write(doc)
    data.append({"name": name, "title": title, "phone": phone, "email": email, "file": f"signatures/{stem}.html", "html": s})
    print(stem, len(s), "chars")
json.dump(data, open(f"{OUT}/signatures.json", "w"), indent=2)

# ---------- preview / copy page ----------
# Preview shows images embedded (so it renders anywhere, offline included).
# The copy buttons and signature files always use the hosted image URLs Gmail needs.
import base64
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "preview_assets")
def embed(h):
    for f, mime in [("emailgif.gif","image/gif"),("herelogo.png","image/png"),("igemail.png","image/png"),("inemail.png","image/png")]:
        p = os.path.join(ASSETS, f)
        if os.path.exists(p):
            h = h.replace(CDN + f, f"data:{mime};base64," + base64.b64encode(open(p,"rb").read()).decode())
    return h
cards = []
for i, d in enumerate(data):
    cards.append(f'''<section class="card">
<header><div><h2>{html.escape(d["name"])}</h2><span>{html.escape(d["title"])}</span></div>
<div class="btns"><button onclick="copySig({i})">Copy signature</button><button class="ghost" onclick="copySrc({i})">Copy HTML source</button></div></header>
<div class="views"><div class="v"><small>Desktop</small><div class="frame d">{embed(d["html"])}</div></div>
<div class="v"><small>Phone (375px)</small><div class="frame m">{embed(d["html"])}</div></div></div>
</section>''')
src = json.dumps([d["html"] for d in data])
page = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Here Agency email signatures</title>
<style>
body{{margin:0;padding:40px 24px;background:#f2f2f2;font-family:Arial,Helvetica,sans-serif;color:#131415}}
.wrap{{max-width:1120px;margin:0 auto}} h1{{font-size:24px;margin:0 0 8px}} p.lead{{margin:0 0 32px;color:#555;font-size:14px;line-height:20px}}
.card{{background:#fff;border-radius:8px;padding:24px;margin-bottom:24px}}
header{{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-bottom:16px;flex-wrap:wrap}}
h2{{font-size:16px;margin:0}} header span{{font-size:12px;color:#777}}
.btns{{display:flex;gap:8px}} button{{font:600 12px Arial;padding:8px 16px;border-radius:4px;border:1px solid #131415;background:#131415;color:#fff;cursor:pointer}}
button.ghost{{background:#fff;color:#131415}}
.views{{display:flex;gap:16px;overflow-x:auto;align-items:flex-start;flex-wrap:wrap}} .v small{{display:block;font-size:11px;color:#999;margin-bottom:8px;text-transform:uppercase;letter-spacing:.08em}}
.frame{{flex:none;border:1px solid #e4e4e4;padding:16px;background:#fff;box-sizing:content-box}} .frame.d{{width:600px}} .frame.m{{width:343px}}
#toast{{position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#131415;color:#fff;padding:8px 16px;border-radius:4px;font-size:12px;opacity:0;transition:opacity .2s}}
</style></head><body><div class="wrap">
<h1>Here Agency email signatures</h1>
<p class="lead">"Copy signature" copies the rendered version, ready to paste into Gmail &gt; Settings &gt; Signature. "Copy HTML source" copies the raw HTML for the Gmail API. See README.md for both routes.</p>
{"".join(cards)}
</div><div id="toast">Copied</div>
<script>
const SRC={src};
function toast(t){{const e=document.getElementById('toast');e.textContent=t;e.style.opacity=1;setTimeout(()=>e.style.opacity=0,1400)}}
function copySig(i){{const n=document.createElement('div');n.style.cssText='position:fixed;left:-9999px;top:0';n.innerHTML=SRC[i];document.body.appendChild(n);const r=document.createRange();r.selectNodeContents(n);const s=getSelection();s.removeAllRanges();s.addRange(r);document.execCommand('copy');s.removeAllRanges();n.remove();toast('Signature copied. Paste it into Gmail.')}}
function copySrc(i){{const t=document.createElement('textarea');t.value=SRC[i];document.body.appendChild(t);t.select();document.execCommand('copy');t.remove();toast('HTML source copied')}}
</script></body></html>'''
open(f"{OUT}/index.html", "w").write(page)
