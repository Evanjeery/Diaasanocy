from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Keep canonical/social metadata aligned with the actual free GitHub Pages URL.
site_url = 'https://evanjeery.github.io/Diaasanocy/'
s = s.replace('https://diaasanocy.me/', site_url)
s = s.replace('https://diaasanocy.me/og-image.jpg', site_url + 'bg-poster.jpg')

css = r'''
        /* ===== PREMIUM PORTFOLIO LAYER ===== */
        .premium-grid { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:12px; margin:0 0 42px; }
        .premium-card { position:relative; padding:18px; border:1px solid rgba(255,255,255,.08); border-radius:12px; background:rgba(8,8,8,.54); backdrop-filter:blur(10px); box-shadow:0 10px 28px rgba(0,0,0,.18); transition:transform .25s ease,border-color .25s ease,background .25s ease; }
        .premium-card:hover { transform:translateY(-2px); border-color:rgba(184,148,31,.35); background:rgba(12,12,12,.7); }
        .premium-card .eyebrow { font:600 .58rem/1 Inter,sans-serif; letter-spacing:.18em; text-transform:uppercase; color:var(--gold); margin-bottom:7px; }
        .premium-card h3 { font:500 1.05rem/1.2 'Cormorant Garamond',serif; color:#f5f5f5; margin-bottom:6px; }
        .premium-card p { font:400 .72rem/1.55 Inter,sans-serif; color:#bdbdbd; }
        .premium-card .mark { position:absolute; top:14px; right:15px; color:rgba(212,168,67,.7); font-size:1rem; }
        .premium-section { margin-bottom:42px; }
        .premium-section .section-label { margin-bottom:12px; }
        .work-list { display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:10px; }
        .work-item { border-left:2px solid rgba(184,148,31,.5); padding:12px 14px; background:rgba(255,255,255,.025); border-radius:0 8px 8px 0; }
        .work-item strong { display:block; font:500 .9rem/1.25 'Cormorant Garamond',serif; color:#eee; }
        .work-item span { display:block; margin-top:4px; font:400 .65rem/1.45 Inter,sans-serif; color:#aaa; }
        .portfolio-actions { display:flex; flex-wrap:wrap; gap:9px; margin:0 0 40px; }
        .portfolio-action { border:1px solid rgba(184,148,31,.4); background:rgba(10,10,10,.55); color:#eee; border-radius:999px; padding:9px 14px; font:600 .63rem Inter,sans-serif; letter-spacing:.08em; text-transform:uppercase; cursor:pointer; transition:all .2s ease; }
        .portfolio-action:hover { color:var(--gold-light); border-color:var(--gold); transform:translateY(-1px); }
        .cv-section.cv-collapsible .cv-section-title { cursor:pointer; user-select:none; display:flex; align-items:center; justify-content:space-between; gap:10px; }
        .cv-section.cv-collapsible .cv-section-title::after { content:'+'; font:400 1.1rem Inter,sans-serif; color:var(--gold); }
        .cv-section.cv-collapsible.open .cv-section-title::after { content:'−'; }
        .cv-section.cv-collapsible .cv-collapse-body { display:none; }
        .cv-section.cv-collapsible.open .cv-collapse-body { display:block; }
        .contact-modal { position:fixed; inset:0; display:flex; align-items:center; justify-content:center; padding:22px; background:rgba(0,0,0,.72); backdrop-filter:blur(8px); z-index:2500; opacity:0; visibility:hidden; transition:opacity .25s ease,visibility .25s ease; }
        .contact-modal.show { opacity:1; visibility:visible; }
        .contact-box { width:min(420px,100%); border:1px solid rgba(184,148,31,.35); border-radius:16px; background:#101010; padding:24px; box-shadow:0 25px 70px rgba(0,0,0,.55); }
        .contact-box h3 { color:var(--gold-light); font:500 1.6rem 'Cormorant Garamond',serif; margin-bottom:6px; }
        .contact-box p { color:#aaa; font:400 .7rem/1.5 Inter,sans-serif; margin-bottom:16px; }
        .contact-option { display:block; padding:12px 0; border-bottom:1px solid rgba(255,255,255,.07); color:#eee; text-decoration:none; font:500 .72rem Inter,sans-serif; }
        .contact-close { margin-top:16px; width:100%; }
        .premium-toast { position:fixed; left:50%; bottom:28px; transform:translate(-50%,18px); opacity:0; pointer-events:none; z-index:3000; padding:9px 14px; border:1px solid rgba(184,148,31,.5); border-radius:999px; background:#111; color:#eee; font:600 .65rem Inter,sans-serif; box-shadow:0 12px 35px rgba(0,0,0,.4); transition:all .25s ease; }
        .premium-toast.show { opacity:1; transform:translate(-50%,0); }
        .name.premium-secret { text-shadow:0 0 22px rgba(212,168,67,.65); }
        @media(max-width:600px){ .premium-grid,.work-list{grid-template-columns:1fr;} .premium-card{padding:15px;} .portfolio-actions{margin-bottom:30px;} }
'''
if 'PREMIUM PORTFOLIO LAYER' not in s:
    s = s.replace('</style>', css + '\n    </style>', 1)

html = r'''
        <section class="premium-section" id="professional-snapshot" aria-label="Professional snapshot">
            <div class="section-label" data-en="Professional snapshot" data-ar="نبذة مهنية">Professional snapshot</div>
            <div class="premium-grid">
                <article class="premium-card"><span class="mark">01</span><div class="eyebrow" data-en="Finance" data-ar="المالية">Finance</div><h3 data-en="Reconciliation & Control" data-ar="التسويات والرقابة">Reconciliation &amp; Control</h3><p data-en="Structured review of balances, expenses, suppliers and supporting documents." data-ar="مراجعة منظمة للأرصدة والمصروفات والموردين والمستندات المؤيدة.">Structured review of balances, expenses, suppliers and supporting documents.</p></article>
                <article class="premium-card"><span class="mark">02</span><div class="eyebrow" data-en="Inventory" data-ar="المخزون">Inventory</div><h3 data-en="Stock & Operations" data-ar="المخزون والتشغيل">Stock &amp; Operations</h3><p data-en="Practical inventory control, movement review and variance follow-up." data-ar="رقابة عملية على المخزون ومراجعة الحركات ومتابعة الفروقات.">Practical inventory control, movement review and variance follow-up.</p></article>
                <article class="premium-card"><span class="mark">03</span><div class="eyebrow" data-en="Data" data-ar="البيانات">Data</div><h3 data-en="Excel & SQL" data-ar="Excel و SQL">Excel &amp; SQL</h3><p data-en="Turning operational data into clean, reviewable information and useful reports." data-ar="تحويل البيانات التشغيلية إلى معلومات نظيفة قابلة للمراجعة وتقارير مفيدة.">Turning operational data into clean, reviewable information and useful reports.</p></article>
                <article class="premium-card"><span class="mark">04</span><div class="eyebrow" data-en="Automation" data-ar="الأتمتة">Automation</div><h3 data-en="Process Improvement" data-ar="تطوير الإجراءات">Process Improvement</h3><p data-en="Reducing repetitive work through structured templates, checks and lightweight automation." data-ar="تقليل العمل المتكرر من خلال القوالب المنظمة والفحوصات والأتمتة الخفيفة.">Reducing repetitive work through structured templates, checks and lightweight automation.</p></article>
            </div>
        </section>

        <section class="premium-section" id="what-i-do" aria-label="What I do">
            <div class="section-label" data-en="What I do" data-ar="ماذا أقدم">What I do</div>
            <div class="work-list">
                <div class="work-item"><strong data-en="Financial Reconciliation" data-ar="التسويات المالية">Financial Reconciliation</strong><span data-en="Balances · suppliers · expenses · supporting documents" data-ar="أرصدة · موردون · مصروفات · مستندات مؤيدة">Balances · suppliers · expenses · supporting documents</span></div>
                <div class="work-item"><strong data-en="Inventory Management" data-ar="إدارة المخزون">Inventory Management</strong><span data-en="Stock movement · counts · variances · controls" data-ar="حركة المخزون · الجرد · الفروقات · الرقابة">Stock movement · counts · variances · controls</span></div>
                <div class="work-item"><strong data-en="Excel Reporting" data-ar="تقارير Excel">Excel Reporting</strong><span data-en="Templates · formulas · cleanup · review-ready reports" data-ar="قوالب · معادلات · تنظيف · تقارير جاهزة للمراجعة">Templates · formulas · cleanup · review-ready reports</span></div>
                <div class="work-item"><strong data-en="SQL & Data Review" data-ar="SQL ومراجعة البيانات">SQL &amp; Data Review</strong><span data-en="Read-only inspection · filtering · reconciliation support" data-ar="فحص للقراءة فقط · تصفية · دعم التسويات">Read-only inspection · filtering · reconciliation support</span></div>
            </div>
        </section>

        <div class="portfolio-actions" aria-label="Portfolio actions">
            <button class="portfolio-action" type="button" id="sharePortfolio" data-en="Share portfolio" data-ar="مشاركة الموقع">Share portfolio</button>
            <button class="portfolio-action" type="button" id="contactCardBtn" data-en="Contact card" data-ar="بطاقة التواصل">Contact card</button>
        </div>
'''
if 'id="professional-snapshot"' not in s:
    anchor = '<div class="section-label">'
    pos = s.find(anchor)
    if pos != -1:
        s = s[:pos] + html + '\n        ' + s[pos:]

js = r'''
        /* ===== PREMIUM INTERACTIONS ===== */
        (function(){
            const toast = document.createElement('div');
            toast.className = 'premium-toast';
            document.body.appendChild(toast);
            const showToast = (text) => { toast.textContent=text; toast.classList.add('show'); clearTimeout(window.__premiumToast); window.__premiumToast=setTimeout(()=>toast.classList.remove('show'),1800); };

            const shareBtn = document.getElementById('sharePortfolio');
            if (shareBtn) shareBtn.addEventListener('click', async () => {
                const url = 'https://evanjeery.github.io/Diaasanocy/';
                try {
                    if (navigator.share) await navigator.share({title:'Diaa Sanocy', text:'Diaa Sanocy — Accountant & Inventory Manager', url});
                    else { await navigator.clipboard.writeText(url); showToast(siteLang === 'ar' ? 'تم نسخ رابط الموقع' : 'Portfolio link copied'); }
                } catch(e){}
            });

            const modal = document.createElement('div');
            modal.className='contact-modal';
            modal.innerHTML='<div class="contact-box" role="dialog" aria-modal="true"><h3>Contact</h3><p>Choose a direct channel.</p><a class="contact-option" href="mailto:diaawork31@gmail.com">Email — diaawork31@gmail.com</a><a class="contact-option" href="https://t.me/DiaaSanocy" target="_blank" rel="noopener noreferrer">Telegram</a><a class="contact-option" href="https://discord.com/users/xx_evan_xx" target="_blank" rel="noopener noreferrer">Discord</a><button class="portfolio-action contact-close" type="button">Close</button></div>';
            document.body.appendChild(modal);
            const closeModal=()=>modal.classList.remove('show');
            const contactBtn=document.getElementById('contactCardBtn');
            if(contactBtn) contactBtn.addEventListener('click',()=>modal.classList.add('show'));
            modal.addEventListener('click',e=>{if(e.target===modal||e.target.classList.contains('contact-close')) closeModal();});

            // Turn CV sections into compact accordions without changing the printed layout.
            document.querySelectorAll('#cv-page .cv-section').forEach((section, i)=>{
                const title=section.querySelector('.cv-section-title');
                if(!title || section.classList.contains('cv-collapsible')) return;
                section.classList.add('cv-collapsible');
                const body=document.createElement('div'); body.className='cv-collapse-body';
                while(title.nextSibling) body.appendChild(title.nextSibling);
                section.appendChild(body);
                if(i===0) section.classList.add('open');
                title.addEventListener('click',()=>section.classList.toggle('open'));
            });

            // Small hidden easter egg: five taps/clicks on the name.
            const name=document.querySelector('.name');
            let taps=0, timer;
            if(name) name.addEventListener('click',()=>{
                taps++; clearTimeout(timer); timer=setTimeout(()=>taps=0,1500);
                if(taps>=5){ taps=0; name.classList.toggle('premium-secret'); showToast('✦ Sanocy mode'); }
            });

            // Ensure the premium layer follows the site's language state after toggling.
            const observer = new MutationObserver(()=>{});
            observer.observe(document.body,{subtree:true,childList:true});
        })();
'''
if 'PREMIUM INTERACTIONS' not in s:
    s = s.replace('</body>', '<script>\n' + js + '\n    </script>\n</body>', 1)

p.write_text(s, encoding='utf-8')
print('premium portfolio layer applied')
