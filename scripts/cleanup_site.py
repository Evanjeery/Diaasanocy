from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')
site_url = 'https://evanjeery.github.io/Diaasanocy/'

s = s.replace('https://diaasanocy.me/', site_url)
s = s.replace('https://evanjeery.github.io/Diaasanocy/og-image.jpg', site_url + 'bg-poster.jpg')
s = s.replace(site_url + 'og-image.jpg', site_url + 'bg-poster.jpg')

s = re.sub(r'\s*<script>\s*/\* ===== PREMIUM INTERACTIONS ===== \*/[\s\S]*?</script>', '', s, count=1)

for pattern in [
    r'\s*\.cv-section\.cv-collapsible[^\n]*\n', r'\s*\.cv-section\.cv-collapsible\.open[^\n]*\n',
    r'\s*\.cv-section\.cv-collapsible \.cv-collapse-body[^\n]*\n', r'\s*\.cv-section\.cv-collapsible\.open \.cv-collapse-body[^\n]*\n',
    r'\s*\.contact-modal[^\n]*\n', r'\s*\.contact-modal\.show[^\n]*\n', r'\s*\.contact-box[^\n]*\n',
    r'\s*\.contact-box h3[^\n]*\n', r'\s*\.contact-box p[^\n]*\n', r'\s*\.contact-option[^\n]*\n',
    r'\s*\.contact-close[^\n]*\n', r'\s*\.premium-toast[^\n]*\n', r'\s*\.premium-toast\.show[^\n]*\n',
    r'\s*\.name\.premium-secret[^\n]*\n']:
    s = re.sub(pattern, '', s)

s = re.sub(r'\s*<div class="portfolio-actions"[\s\S]*?</div>\s*', '\n', s, count=1)

pdf_button = '<button class="lang-toggle-btn" type="button" onclick="window.print()" aria-label="Print or save CV as PDF">PDF</button>'
lang_button = '<button class="lang-toggle-btn" id="langToggleBtn" onclick="toggleLang()">العربية</button>'
control = '<div style="display:flex;align-items:center;gap:8px">' + pdf_button + lang_button + '</div>'
cv_top = re.compile(r'(<div class="cv-top-bar">\s*<button class="back-btn"[\s\S]*?</button>)[\s\S]*?(\s*</div>\s*</div>)', re.M)
m = cv_top.search(s)
if m:
    s = s[:m.start()] + m.group(1) + '\n                ' + control + m.group(2) + s[m.end():]
else:
    raise SystemExit('CV top bar was not found')

# Repair the malformed CV wrapper created by the previous cleanup pass.
s = s.replace('</div></div><div class="cv-header">', '</div><div class="cv-header">', 1)

pdf_matches = list(re.finditer(r'<button[^>]*onclick="window\.print\(\)"[^>]*>PDF</button>', s))
if len(pdf_matches) > 1:
    for match in reversed(pdf_matches[1:]):
        s = s[:match.start()] + s[match.end():]

for phrase in ['Main Stores', 'Main Store', 'Main Warehouse', 'Main Warehouses', 'المخازن الرئيسية', 'المخزن الرئيسي', 'المخازن الرئيسيه', 'المخزن الرئيسى']:
    s = s.replace(phrase, '')

s = s.replace(
    "bgVideo.volume=.3;bgVideo.play().then(()=>{isPlaying=true;audioBtn.textContent='♫'}).catch(()=>{isPlaying=false;bgVideo.muted=true;bgVideo.play();audioBtn.textContent='♪'})",
    "bgVideo.volume=Number(volumeSlider.value)/100;bgVideo.muted=false;bgVideo.play().then(()=>{isPlaying=true;audioBtn.textContent='♫'}).catch(()=>{isPlaying=false;bgVideo.muted=true;audioBtn.textContent='♪'})"
)

if 'audioBtn.addEventListener' not in s:
    marker = "function showCV(){"
    audio_js = "audioBtn.addEventListener('click',()=>{bgVideo.muted=!bgVideo.muted;isPlaying=!bgVideo.muted;audioBtn.textContent=bgVideo.muted?'♪':'♫';if(!bgVideo.muted)bgVideo.play().catch(()=>{})});volumeSlider.addEventListener('input',()=>{bgVideo.volume=Number(volumeSlider.value)/100;volumeValue.textContent=volumeSlider.value+'%';if(Number(volumeSlider.value)>0){bgVideo.muted=false;isPlaying=true;audioBtn.textContent='♫';bgVideo.play().catch(()=>{})}});"
    s = s.replace(marker, audio_js + marker, 1)

if 'diaasanocy.me' in s:
    raise SystemExit('Stale custom-domain reference remains in index.html')

p.write_text(s, encoding='utf-8')
print('site cleanup completed: repaired CV HTML, one PDF control, no stale domain, working video audio')
