import re

file_path = r'c:\Users\pavel\Desktop\portfolio\main.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

def swap(orig, cs, en):
    # simple replace if exact match is found, else just return content
    return content.replace(orig, f'<span class="lang-cs">{cs}</span><span class="lang-en">{en}</span>')

# Hero
content = content.replace(
    '<div class="hero-greeting">Zdravím, jsem</div>',
    '<div class="hero-greeting"><span class="lang-cs">Zdravím, jsem</span><span class="lang-en">Hi, I\'m</span></div>'
)
content = content.replace(
    '<p class="hero-bio"> Absolvent magisterského studia Informačních technologií (specializace Strojové učení) na\n            FIT VUT Brno. Zaměřuji se na machine learning, počítačové vidění a praktické nasazení modelů. Rád pracuji na\n            projektech s reálným dopadem. </p>',
    '<p class="hero-bio">\n            <span class="lang-cs">Absolvent magisterského studia Informačních technologií (specializace Strojové učení) na FIT VUT Brno. Zaměřuji se na machine learning, počítačové vidění a praktické nasazení modelů. Rád pracuji na projektech s reálným dopadem.</span>\n            <span class="lang-en">Master\'s graduate in Information Technology (Machine Learning specialization) at FIT BUT. I focus on machine learning, computer vision, and practical model deployment. I enjoy working on projects with real-world impact.</span>\n          </p>'
)
content = content.replace(
    '</svg> Stáhnout životopis </a>',
    '</svg> <span class="lang-cs">Stáhnout životopis</span><span class="lang-en">Download CV</span> </a>'
)

# Skills
content = content.replace('<div class="section-label">Co umím</div>', '<div class="section-label"><span class="lang-cs">Co umím</span><span class="lang-en">What I do</span></div>')
content = content.replace('<h2 class="section-title">Dovednosti</h2>', '<h2 class="section-title"><span class="lang-cs">Dovednosti</span><span class="lang-en">Skills</span></h2>')
content = content.replace('<h3>Programovací jazyky</h3>', '<h3><span class="lang-cs">Programovací jazyky</span><span class="lang-en">Programming languages</span></h3>')
content = content.replace('<h3>Nástroje</h3>', '<h3><span class="lang-cs">Nástroje</span><span class="lang-en">Tools</span></h3>')
content = content.replace('<h3>Soft skills</h3>', '<h3><span class="lang-cs">Soft skills</span><span class="lang-en">Soft skills</span></h3>')
content = swap('Analytické myšlení', 'Analytické myšlení', 'Analytical thinking')
content = swap('Samostatnost', 'Samostatnost', 'Independence')
content = swap('Spolehlivost', 'Spolehlivost', 'Reliability')
content = swap('Týmová práce', 'Týmová práce', 'Teamwork')
content = content.replace('<h3>Jazyky</h3>', '<h3><span class="lang-cs">Jazyky</span><span class="lang-en">Languages</span></h3>')
content = swap('Čeština (rodilý)', 'Čeština (rodilý)', 'Czech (Native)')
content = swap('Angličtina (pokročilá)', 'Angličtina (pokročilá)', 'English (Advanced)')

# Projects
content = content.replace('<div class="section-label">Co jsem vytvořil</div>', '<div class="section-label"><span class="lang-cs">Co jsem vytvořil</span><span class="lang-en">What I\'ve built</span></div>')
content = content.replace('<h2 class="section-title">Vybrané projekty</h2>', '<h2 class="section-title"><span class="lang-cs">Vybrané projekty</span><span class="lang-en">Selected projects</span></h2>')
content = content.replace('<div class="project-title">LLM-řízené CGP pro symbolickou regresi</div>', '<div class="project-title"><span class="lang-cs">LLM-řízené CGP pro symbolickou regresi</span><span class="lang-en">LLM-guided CGP for symbolic regression</span></div>')
content = content.replace(
    '<div class="project-desc">Diplomová práce: integrace velkých jazykových modelů (Gemma 4, Phi 4) do evoluční\n            smyčky kartézského genetického programování. Výsledek: 48,1% redukce mediánu testovací chyby NMSE.</div>',
    '<div class="project-desc"><span class="lang-cs">Diplomová práce: integrace velkých jazykových modelů (Gemma 4, Phi 4) do evoluční smyčky kartézského genetického programování. Výsledek: 48,1% redukce mediánu testovací chyby NMSE.</span><span class="lang-en">Master\'s thesis: integration of large language models (Gemma 4, Phi 4) into the evolutionary loop of Cartesian Genetic Programming. Result: 48.1% reduction in median test NMSE error.</span></div>'
)
content = swap('Symbolická regrese', 'Symbolická regrese', 'Symbolic regression')

content = content.replace('<div class="project-title">LZW obrázkový kodek</div>', '<div class="project-title"><span class="lang-cs">LZW obrázkový kodek</span><span class="lang-en">LZW image codec</span></div>')
content = content.replace(
    '<div class="project-desc">C++ implementace obrazového kompresního kodeku postaveného na LZW algoritmu.\n            Obsahuje delta model, adaptivní scanning a variabilní šířku kódů (9–16 bitů). Nejlepší výkon ~1,22 bpp.\n          </div>',
    '<div class="project-desc"><span class="lang-cs">C++ implementace obrazového kompresního kodeku postaveného na LZW algoritmu. Obsahuje delta model, adaptivní scanning a variabilní šířku kódů (9–16 bitů). Nejlepší výkon ~1,22 bpp.</span><span class="lang-en">C++ implementation of an image compression codec based on the LZW algorithm. Features a delta model, adaptive scanning, and variable code width (9–16 bits). Best performance ~1.22 bpp.</span></div>'
)
content = swap('Komprese obrazu', 'Komprese obrazu', 'Image compression')
content = swap('Algoritmy', 'Algoritmy', 'Algorithms')

content = content.replace('<div class="project-title">Statistické modelování procesů</div>', '<div class="project-title"><span class="lang-cs">Statistické modelování procesů</span><span class="lang-en">Statistical process modeling</span></div>')
content = content.replace(
    '<div class="project-desc">Analýza přežití (Weibullovo rozdělení) a regresní modely s iterativní eliminací\n            prediktorů v Pythonu. Projekt v rámci předmětu MSP na FIT VUT Brno.</div>',
    '<div class="project-desc"><span class="lang-cs">Analýza přežití (Weibullovo rozdělení) a regresní modely s iterativní eliminací prediktorů v Pythonu. Projekt v rámci předmětu MSP na FIT VUT Brno.</span><span class="lang-en">Survival analysis (Weibull distribution) and regression models with iterative predictor elimination in Python. Project for the MSP course at FIT BUT.</span></div>'
)
content = swap('Statistika', 'Statistika', 'Statistics')

# Experience
content = content.replace('<div class="section-label">Kde jsem pracoval</div>', '<div class="section-label"><span class="lang-cs">Kde jsem pracoval</span><span class="lang-en">Where I\'ve worked</span></div>')
content = content.replace('<h2 class="section-title">Pracovní zkušenosti</h2>', '<h2 class="section-title"><span class="lang-cs">Pracovní zkušenosti</span><span class="lang-en">Experience</span></h2>')

content = content.replace('<div class="tl-role">Asistent prodeje / Závozník</div>', '<div class="tl-role"><span class="lang-cs">Asistent prodeje / Závozník</span><span class="lang-en">Sales Assistant / Co-driver</span></div>')
content = swap('Komunikace se zákazníky', 'Komunikace se zákazníky', 'Customer communication')
content = swap('Logistika', 'Logistika', 'Logistics')

content = content.replace('<div class="tl-role">Tester webových aplikací</div>', '<div class="tl-role"><span class="lang-cs">Tester webových aplikací</span><span class="lang-en">Web Application Tester</span></div>')
content = swap('Manuální testování', 'Manuální testování', 'Manual testing')
content = swap('Dokumentace chyb', 'Dokumentace chyb', 'Bug documentation')

content = content.replace('<div class="tl-role">IT Specialista (stáž)</div>', '<div class="tl-role"><span class="lang-cs">IT Specialista (stáž)</span><span class="lang-en">IT Specialist (Internship)</span></div>')
content = swap('Instalace HW/SW', 'Instalace HW/SW', 'HW/SW Installation')
content = swap('Technická podpora', 'Technická podpora', 'Technical support')
content = swap('Diagnostika', 'Diagnostika', 'Diagnostics')

content = content.replace('<div class="tl-role">Asistent logistiky</div>', '<div class="tl-role"><span class="lang-cs">Asistent logistiky</span><span class="lang-en">Logistics Assistant</span></div>')
content = swap('Administrativa', 'Administrativa', 'Administration')
content = swap('Evidence zásilek', 'Evidence zásilek', 'Shipment tracking')
content = swap('Expedice', 'Expedice', 'Dispatch')

# Education
content = content.replace('<div class="section-label">Kde jsem studoval</div>', '<div class="section-label"><span class="lang-cs">Kde jsem studoval</span><span class="lang-en">Where I\'ve studied</span></div>')
content = content.replace('<h2 class="section-title">Vzdělání</h2>', '<h2 class="section-title"><span class="lang-cs">Vzdělání</span><span class="lang-en">Education</span></h2>')
content = content.replace('<div class="edu-degree">Ing. - Strojové učení</div>', '<div class="edu-degree"><span class="lang-cs">Ing. – Strojové učení</span><span class="lang-en">Ing. (MSc) – Machine Learning</span></div>')
content = content.replace('<div class="edu-degree">Bc. - Informační technologie</div>', '<div class="edu-degree"><span class="lang-cs">Bc. – Informační technologie</span><span class="lang-en">Bc. (BSc) – Information Technology</span></div>')
content = content.replace('<div class="edu-degree">Informační technologie</div>', '<div class="edu-degree"><span class="lang-cs">Informační technologie</span><span class="lang-en">Information Technology</span></div>')


with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done")
