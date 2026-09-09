from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

video = '''    <!-- Background Video -->
    <video class="bg-video" id="bgVideo" autoplay muted loop playsinline preload="metadata" poster="bg-poster.jpg" aria-hidden="true">
        <source src="bg-mobile.webm" type="video/webm" media="(max-width: 600px)">
        <source src="bg-mobile.mp4" type="video/mp4" media="(max-width: 600px)">
        <source src="bg-optimized.webm" type="video/webm">
        <source src="bg-optimized.mp4" type="video/mp4">
        <source src="bg.mp4" type="video/mp4">
    </video>'''
s, n = re.subn(r'    <!-- Background Video -->\s*<video[^>]*id="bgVideo"[\s\S]*?</video>', video, s, count=1)
if n != 1:
    raise SystemExit('Background video block was not found')

if 'application/ld+json' not in s:
    marker = '    <link rel="canonical" href="https://diaasanocy.me/">'
    jsonld = '''
    <script type="application/ld+json">
    {"@context":"https://schema.org","@type":"Person","name":"Diaa Sanocy","url":"https://diaasanocy.me/","jobTitle":"Accountant & Inventory Manager","email":"mailto:diaawork31@gmail.com","sameAs":["https://discord.com/users/xx_evan_xx","https://t.me/DiaaSanocy"]}
    </script>'''
    s = s.replace(marker, marker + jsonld, 1)

# Add safe rel attributes to external links.
s = re.sub(r'<a(\s[^>]*target="_blank"[^>]*)>', lambda m: ('<a' + (m.group(1) if 'rel="' in m.group(1) else m.group(1) + ' rel="noopener noreferrer"') + '>'), s)

# Replace the old CSS-only tricolor with a real Egyptian flag asset.
old_flag = '<span class="flag" style="background: linear-gradient(to bottom, #ce1126 33.33%, #fff 33.33%, #fff 66.66%, #000 66.66%);"></span>'
new_flag = '<img class="flag" src="egypt-flag.svg" alt="Egypt" width="24" height="18" loading="eager">'
s = s.replace(old_flag, new_flag, 1)

responsive = '''

        /* ===== MOBILE / PERFORMANCE POLISH ===== */
        .bg-video { opacity: 0; transition: opacity .45s ease; }
        .bg-video.ready { opacity: .4; }
        .content, .cv-content { overflow-wrap: anywhere; }
        .social-link, .back-btn, .lang-toggle-btn, .audio-btn { -webkit-tap-highlight-color: transparent; }
        @media (max-width: 600px) {
            .content { max-width: 100%; padding: 34px 18px 90px; }
            .header { align-items: center; margin-bottom: 16px; }
            .name-group { gap: 8px; min-width: 0; }
            .name { font-size: clamp(2.15rem, 11vw, 2.8rem); }
            .nickname { font-size: clamp(1rem, 5vw, 1.25rem); }
            .header-right { gap: 10px; }
            .nav { display: none; }
            .field-row { margin-bottom: 22px; font-size: .62rem; }
            .bio-carousel { max-width: 100%; min-height: 0; margin-bottom: 10px; }
            .bio-slide { font-size: 1.02rem; line-height: 1.65; }
            .bio-dots { margin-bottom: 30px; }
            .obsession-card { max-width: 100%; margin-bottom: 38px; padding: 15px 16px; }
            .obsession-icon { width: 46px; height: 46px; font-size: 1.25rem; }
            .social-link { padding: 13px 0; }
            .audio-control-wrapper { left: 50%; right: auto; bottom: 12px; transform: translateX(-50%); padding: 7px 12px; }
            .volume-slider { width: 72px; }
            .cv-content { padding: 30px 18px 50px; }
            .cv-header { margin-bottom: 34px; }
            .cv-header h1 { font-size: 2.25rem; }
            .cv-header .cv-title { font-size: .72rem; letter-spacing: .12em; }
            .cv-section { margin-bottom: 30px; }
            .cv-section-title { font-size: 1.3rem; margin-bottom: 15px; }
            .cv-item { padding-left: 14px; padding-right: 0; }
            #cv-page.lang-ar .cv-item { padding-right: 14px; padding-left: 0; }
            .cv-item p { font-size: 1rem; }
            .cv-skill { font-size: .68rem; padding: 6px 11px; }
        }
        @media (prefers-reduced-motion: reduce) {
            *, *::before, *::after { scroll-behavior: auto !important; animation-duration: .01ms !important; animation-iteration-count: 1 !important; transition-duration: .01ms !important; }
        }
        @media print {
            body { background: #fff !important; color: #111 !important; }
            #landing, #main, .bg-video, .bg-overlay, .audio-control-wrapper, .cv-top-bar { display: none !important; }
            #cv-page, #cv-page.active { display: block !important; opacity: 1 !important; }
            .cv-content { max-width: none; padding: 0; background: none; color: #111; }
            .cv-section { opacity: 1 !important; transform: none !important; break-inside: avoid; }
            .cv-section-title, .cv-header h1 { color: #222 !important; }
            .cv-item p, .cv-item h4, .cv-header .cv-title { color: #222 !important; }
        }
'''
if 'MOBILE / PERFORMANCE POLISH' not in s:
    s = s.replace('        /* Responsive */', responsive + '\n        /* Responsive */', 1)

# Add a print/save-PDF action to the CV header.
old_top = '<button class="lang-toggle-btn" id="langToggleBtn" onclick="toggleLang()">العربية</button>'
new_top = '<div style="display:flex;align-items:center;gap:8px"><button class="lang-toggle-btn" type="button" onclick="window.print()" aria-label="Print or save CV as PDF">PDF</button><button class="lang-toggle-btn" id="langToggleBtn" onclick="toggleLang()">العربية</button></div>'
s = s.replace(old_top, new_top, 1)

# Copy email on tap; no WhatsApp or LinkedIn added.
email_link = '<a href="mailto:diaawork31@gmail.com" target="_blank" class="social-link">'
email_link_new = '<a href="mailto:diaawork31@gmail.com" target="_blank" class="social-link" onclick="copyEmail(event)">'
s = s.replace(email_link, email_link_new, 1)
copy_fn = '''

        function copyEmail(event) {
            if (!navigator.clipboard) return;
            navigator.clipboard.writeText('diaawork31@gmail.com').then(() => {
                const link = event.currentTarget;
                const label = link.querySelector('[data-en]');
                if (!label) return;
                const oldEn = label.dataset.en;
                const oldAr = label.dataset.ar;
                label.dataset.en = 'Email copied';
                label.dataset.ar = 'تم نسخ الإيميل';
                label.textContent = siteLang === 'ar' ? label.dataset.ar : label.dataset.en;
                setTimeout(() => {
                    label.dataset.en = oldEn;
                    label.dataset.ar = oldAr;
                    label.textContent = siteLang === 'ar' ? oldAr : oldEn;
                }, 1400);
            }).catch(() => {});
        }
'''
if 'function copyEmail(' not in s:
    s = s.replace('        // Audio toggle', copy_fn + '\n        // Audio toggle', 1)

s = s.replace("bgVideo.setAttribute('preload', 'auto');", "bgVideo.setAttribute('preload', 'metadata');", 1)
p.write_text(s, encoding='utf-8')
print('index.html polished successfully')
