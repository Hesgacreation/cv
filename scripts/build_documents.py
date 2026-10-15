import subprocess
import os

CV_DIR = "/home/theodoreh/Documents/2A/cv"

# Common CSS for 1-page A4 CV
CV_CSS = """
@page {
    size: A4;
    margin: 8mm 12mm 8mm 12mm;
}
* {
    box-sizing: border-box;
}
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 8.7pt;
    line-height: 1.28;
    color: #1e293b;
    margin: 0;
    padding: 0;
}
.header {
    text-align: center;
    border-bottom: 2px solid #0284c7;
    padding-bottom: 4px;
    margin-bottom: 5px;
}
.name {
    font-size: 18pt;
    font-weight: 800;
    letter-spacing: 0.6px;
    color: #0f172a;
    text-transform: uppercase;
    margin: 0;
}
.title {
    font-size: 9.8pt;
    font-weight: 700;
    color: #0284c7;
    margin: 2px 0 3px 0;
    letter-spacing: 0.2px;
}
.contact-line {
    font-size: 8.2pt;
    color: #475569;
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
    margin-bottom: 2px;
}
.contact-line a {
    color: #0369a1;
    text-decoration: none;
}
.status-badge {
    font-size: 7.9pt;
    font-weight: 600;
    color: #0369a1;
    background-color: #f0f9ff;
    border: 1px solid #bae6fd;
    border-radius: 4px;
    padding: 1px 7px;
    display: inline-block;
    margin-top: 1px;
}
.section-title {
    font-size: 9.2pt;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #0369a1;
    border-bottom: 1px solid #cbd5e1;
    padding-bottom: 1px;
    margin: 5px 0 3px 0;
}
.summary-text {
    font-size: 8.4pt;
    color: #334155;
    text-align: justify;
    margin: 0 0 3px 0;
}
.item {
    margin-bottom: 3.5px;
}
.item-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
}
.item-title {
    font-size: 8.8pt;
    font-weight: 700;
    color: #0f172a;
}
.item-subtitle {
    font-size: 8.3pt;
    font-weight: 600;
    color: #0284c7;
}
.item-date {
    font-size: 8pt;
    font-weight: 500;
    color: #64748b;
    text-align: right;
    white-space: nowrap;
}
.item-location {
    font-size: 7.8pt;
    color: #64748b;
    font-style: italic;
}
ul {
    margin: 1.5px 0 2.5px 0;
    padding-left: 13px;
}
li {
    margin-bottom: 1.5px;
    font-size: 8.2pt;
    color: #334155;
    text-align: justify;
}
li strong {
    color: #0f172a;
}
.skills-table {
    display: table;
    width: 100%;
    margin-top: 2px;
}
.skills-row {
    display: table-row;
}
.skills-cat {
    display: table-cell;
    width: 23%;
    font-weight: 700;
    color: #0f172a;
    font-size: 8.2pt;
    padding-bottom: 1.5px;
}
.skills-val {
    display: table-cell;
    font-size: 8.2pt;
    color: #334155;
    padding-bottom: 1.5px;
}
.lang-row {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 6px;
    font-size: 8.2pt;
    margin-top: 1px;
}
.lang-item strong {
    color: #0f172a;
}
.lang-item span {
    color: #475569;
}
"""

# Common Letter CSS
LETTER_CSS = """
@page {
    size: A4;
    margin: 18mm 20mm 18mm 20mm;
}
body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    font-size: 10.2pt;
    line-height: 1.48;
    color: #1e293b;
    margin: 0;
    padding: 0;
}
.letter-header {
    border-bottom: 2px solid #0284c7;
    padding-bottom: 10px;
    margin-bottom: 16px;
}
.sender-name {
    font-size: 16pt;
    font-weight: 800;
    color: #0f172a;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin: 0;
}
.sender-contact {
    font-size: 9pt;
    color: #475569;
    margin-top: 3px;
}
.meta-info {
    display: flex;
    justify-content: space-between;
    margin-bottom: 14px;
    font-size: 9.5pt;
    color: #334155;
}
.recipient-box {
    margin-bottom: 14px;
    font-size: 9.5pt;
    color: #0f172a;
}
.subject-line {
    font-size: 10.5pt;
    font-weight: 700;
    color: #0369a1;
    background-color: #f0f9ff;
    border-left: 3.5px solid #0284c7;
    padding: 6px 12px;
    margin-bottom: 14px;
}
.salutation {
    font-weight: 600;
    margin-bottom: 10px;
}
p {
    margin: 0 0 10px 0;
    text-align: justify;
}
.signoff {
    margin-top: 14px;
}
.signature-name {
    font-size: 11pt;
    font-weight: 700;
    color: #0f172a;
    margin-top: 4px;
}
.signature-title {
    font-size: 9pt;
    color: #475569;
}
"""

def generate_cv1_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Theodore Hesling - CV Embedded Systems & Hardware Security</title>
<style>{CV_CSS}</style>
</head>
<body>
  <div class="header">
    <div class="name">Théodore Hesling</div>
    <div class="title">Engineering Student | Embedded Systems & Hardware Security Intern</div>
    <div class="contact-line">
      <span>theodore200531@outlook.com</span> • 
      <span>+33 6 75 49 33 72</span> • 
      <span>Gardanne / Aix-en-Provence, France</span> • 
      <span>French (EU Citizen – Simplified Swiss B/L Permit)</span>
    </div>
    <div class="status-badge">Available for 4 to 5-Month Internship (minimum 16 weeks – CTI requirement) starting April 2027 • Targeting Suisse Romande</div>
  </div>

  <div class="section-title">Professional Summary</div>
  <div class="summary-text">
    Second-year MSc engineering student at <strong>Mines Saint-Étienne (ISMIN)</strong> specializing in Embedded Systems, Hardware Security, and Microelectronics. Combining hands-on automotive cybersecurity architecture experience at <strong>Valeo</strong> with rigorous bare-metal <strong>STM32 (ARM Cortex-M)</strong> firmware engineering, custom analog capacitive sensor instrumentation, closed-loop PID control, and OpenSSL cryptography. Bilingual French/English (C2) with remarkable international mobility (Spanish C1, Chinese C1, learning German). Seeking a 4 to 5-month technical internship in Switzerland (focusing on Suisse Romande: Vaud, Geneva, Neuchâtel) starting April 2027.
  </div>

  <div class="section-title">Education</div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Mines Saint-Étienne (ISMIN Campus)</span> – <span class="item-subtitle">Master of Science in Engineering (Diplôme d'Ingénieur)</span></div>
      <div class="item-date">09/2025 – 07/2028 | Gardanne, France</div>
    </div>
    <ul>
      <li><strong>Specialization:</strong> Embedded Systems, Microelectronics Design, Hardware Security & IoT (Adjoined to Centre Microélectronique de Provence - CMP).</li>
      <li><strong>Core Modules:</strong> Microcontroller Architectures (ARM Cortex-M), Object-Oriented Design (C++, Java, Python), Enterprise Network & Infrastructure Security (SRIE: Firewalls, DMZ, Wireshark), Digital Systems (SystemVerilog), Signal Processing, Project Management.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Lycée Jeanne d’Albret</span> – <span class="item-subtitle">CPGE PC (Classes Préparatoires aux Grandes Écoles – Physics & Chemistry)</span></div>
      <div class="item-date">09/2023 – 07/2025 | St-Germain-en-Laye, France</div>
    </div>
    <ul>
      <li>Intensive two-year national curriculum in Advanced Mathematics, Physics, and Chemistry. Competitive national entrance exams.</li>
    </ul>
  </div>

  <div class="section-title">Engineering & Hardware Projects</div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Autonomous Self-Levelling Vessel Prototype</span> – <span class="item-subtitle">STM32 / Bare-Metal C / Custom Capacitive Sensors / CAD</span></div>
      <div class="item-date">01/2026 – 05/2026</div>
    </div>
    <ul>
      <li><strong>Custom Capacitive Liquid-Level Sensors:</strong> Designed and hand-fabricated custom differential capacitive sensors mounted on hull flanks; quantified water dielectric variations (&Delta;&epsilon;<sub>r</sub>) to accurately measure listing and differential water height in real time.</li>
      <li><strong>Firmware Signal Conditioning:</strong> Engineered bare-metal STM32 (ARM Cortex-M) C firmware executing high-speed timer-driven capacitive charge/discharge sampling, software digital filtering, and sensor calibration.</li>
      <li><strong>Closed-Loop PID Dynamic Stabilization:</strong> Formulated a real-time feedback PID control algorithm dynamically commanding high-torque PWM servomotors to modulate counter-balancing ballast and keep the vessel level under hydrodynamics perturbations.</li>
      <li><strong>Mechanical CAD Prototyping:</strong> Modeled all hull structures, sensor brackets, and watertight electronics compartments using Autodesk Inventor, followed by 3D printing and bench testing.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Secure IoT Connected Architecture (Security-by-Design)</span> – <span class="item-subtitle">C++ / OpenSSL / Wireless Telemetry</span></div>
      <div class="item-date">09/2026 – 01/2027</div>
    </div>
    <ul>
      <li>Architected an end-to-end low-power connected sensing node transmitting telemetry metrics over BLE / Wi-Fi.</li>
      <li>Integrated cryptographic mutual authentication and payload encryption leveraging OpenSSL primitives and TLS/DTLS to prevent replay and spoofing attacks.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Digital Inclusion & Tech Mentorship Initiative (Projet ISA)</span> – <span class="item-subtitle">Solidarity Engineering</span></div>
      <div class="item-date">10/2025 – 03/2026</div>
    </div>
    <ul>
      <li>Conducted interactive workshops for senior citizens on mastering connected devices and digital security fundamentals, proving strong pedagogy and communication.</li>
    </ul>
  </div>

  <div class="section-title">Professional Experience</div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Valeo</span> – <span class="item-subtitle">Cybersecurity Platform Architect Intern</span></div>
      <div class="item-date">01/2026 – 02/2026 | Créteil, France</div>
    </div>
    <ul>
      <li>Analyzed attack vectors across connected automotive electronic control units (ECUs) and gateway hardware architectures.</li>
      <li>Audited vehicular communication protocols (CAN-FD, Ethernet) and secure boot primitives against the ISO/SAE 21434 automotive standard.</li>
      <li>Collaborated with senior cybersecurity architects on hardware security module (HSM) deployment and hardware vulnerability mitigation.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Junior Mines Provence</span> – <span class="item-subtitle">Treasurer & Executive Board Member</span></div>
      <div class="item-date">01/2026 – 07/2026 | Gardanne, France</div>
    </div>
    <ul>
      <li>Directed the financial administration and budgeting for the school's commercial consulting branch; successfully passed national CNJE quality audit.</li>
      <li>Enforced strict internal compliance controls and automated financial reporting workflows using Google Apps Script and Python.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">BNP Paribas CIB</span> – <span class="item-subtitle">Observation Internship (High-Security Trading Floor)</span></div>
      <div class="item-date">04/2021 | Shanghai, China</div>
    </div>
    <ul>
      <li>Shadowed system reliability and network security engineers maintaining high-availability trading infrastructure and mission-critical data integrity.</li>
    </ul>
  </div>

  <div class="section-title">Technical Skills</div>
  <div class="skills-table">
    <div class="skills-row">
      <div class="skills-cat">Embedded & Hardware:</div>
      <div class="skills-val">STM32 (ARM Cortex-M), Custom Capacitive Sensors, I2C, SPI, UART, CAN, PWM, SystemVerilog (basics), Oscilloscopes, Autodesk Inventor.</div>
    </div>
    <div class="skills-row">
      <div class="skills-cat">Programming & Systems:</div>
      <div class="skills-val">Embedded C, C++, Python, Bash, Google Apps Script, Linux / POSIX, Git, Docker, STM32CubeIDE, Keil.</div>
    </div>
    <div class="skills-row">
      <div class="skills-cat">Security & Protocols:</div>
      <div class="skills-val">OpenSSL (TLS, AES, RSA, HMAC), Secure Boot concepts, Wireshark, ISO/SAE 21434, Hardware Attack Surface Analysis.</div>
    </div>
  </div>

  <div class="section-title">Languages</div>
  <div class="lang-row">
    <div class="lang-item"><strong>French:</strong> <span>Native</span></div>
    <div class="lang-item"><strong>English:</strong> <span>Bilingual (C2 – IGCSE & A-Levels)</span></div>
    <div class="lang-item"><strong>Spanish:</strong> <span>Advanced (C1 – DELE)</span></div>
    <div class="lang-item"><strong>Chinese:</strong> <span>Advanced (C1 – HSK 3)</span></div>
    <div class="lang-item"><strong>German:</strong> <span>Elementary (A1/A2 – Independent study, Nicos Weg)</span></div>
  </div>
</body>
</html>"""

def generate_cv2_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Theodore Hesling - CV Cybersecurity Networks & Infrastructure</title>
<style>{CV_CSS}</style>
</head>
<body>
  <div class="header">
    <div class="name">Théodore Hesling</div>
    <div class="title">Engineering Student | Cybersecurity, Network Infrastructure & Threat Resilience Intern</div>
    <div class="contact-line">
      <span>theodore200531@outlook.com</span> • 
      <span>+33 6 75 49 33 72</span> • 
      <span>Gardanne / Aix-en-Provence, France</span> • 
      <span>French (EU Citizen – Simplified Swiss B/L Permit)</span>
    </div>
    <div class="status-badge">Available for 4 to 5-Month Internship (minimum 16 weeks – CTI requirement) starting April 2027 • Targeting Suisse Romande</div>
  </div>

  <div class="section-title">Professional Summary</div>
  <div class="summary-text">
    Second-year Computer Science & Cybersecurity engineering student at <strong>Mines Saint-Étienne (ISMIN)</strong> with practical experience in threat modeling at <strong>Valeo</strong> and hands-on enterprise network defense labs (DMZ segmentation, MikroTik firewalls, Wireshark traffic auditing, OpenSSL). Complementing network defense with low-level sensor instrumentation (custom capacitive sensing, STM32 firmware), rigorous financial governance as Junior Enterprise Treasurer, and exposure to trading floor reliability at <strong>BNP Paribas CIB</strong>. Bilingual French/English (C2) with exceptional multilingual proficiency (Spanish C1, Chinese C1, learning German). Seeking a 4 to 5-month internship in Switzerland (focusing on Suisse Romande) starting April 2027.
  </div>

  <div class="section-title">Education</div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Mines Saint-Étienne (ISMIN Campus)</span> – <span class="item-subtitle">Master of Science in Engineering (Diplôme d'Ingénieur)</span></div>
      <div class="item-date">09/2025 – 07/2028 | Gardanne, France</div>
    </div>
    <ul>
      <li><strong>Curriculum Focus:</strong> Computer Science, Enterprise Network Architecture & Security, Cryptographic Protocols, Systems Integration.</li>
      <li><strong>Key Coursework:</strong> Network & Enterprise Infrastructure Security (SRIE: Routing, DMZ, Firewalling, IDS/IPS), Object-Oriented Software Engineering (C++, Python), Relational Databases & SQL, Operating Systems (Linux/Unix), IoT Architecture, Information Systems Management.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Lycée Jeanne d’Albret</span> – <span class="item-subtitle">CPGE PC (Classes Préparatoires aux Grandes Écoles – Physics & Chemistry)</span></div>
      <div class="item-date">09/2023 – 07/2025 | St-Germain-en-Laye, France</div>
    </div>
    <ul>
      <li>Intensive two-year national preparatory cycle in Advanced Mathematics, Physics, and Algorithmic Thinking.</li>
    </ul>
  </div>

  <div class="section-title">Technical & Security Projects</div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Enterprise Network Defense & Traffic Auditing Lab (VISMIN / SRIE)</span> – <span class="item-subtitle">MikroTik RouterOS / Wireshark / Docker</span></div>
      <div class="item-date">09/2026 – 01/2027</div>
    </div>
    <ul>
      <li><strong>Architecture Design:</strong> Built and audited multi-subnet corporate topologies containing perimeter firewalls (MikroTik RouterOS), transit routers, corporate DMZs, and dual-homed internal servers using containerized Docker testbeds.</li>
      <li><strong>Traffic Inspection & Hardening:</strong> Captured and analyzed live packet traces via Wireshark and tcpdump to detect half-open SYN port scans, unauthorized lateral movement, and unencrypted traffic flows.</li>
      <li><strong>Security Policies:</strong> Defined strict stateful packet filtering rules, NAT translation, and access control lists (ACLs) to enforce zero-trust segmentation between untrusted edge interfaces and core corporate databases.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Secure Encrypted Communication & IoT Pipeline</span> – <span class="item-subtitle">OpenSSL / Python / TLS</span></div>
      <div class="item-date">09/2026 – 01/2027</div>
    </div>
    <ul>
      <li>Designed a client-server telemetry architecture incorporating end-to-end transport layer security (TLS/SSL).</li>
      <li>Generated and managed cryptographic PKI certificates, public/private key pairs, and HMAC verification schemes with OpenSSL to guarantee data confidentiality and integrity across untrusted network hops.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Autonomous Self-Levelling Vessel Prototype</span> – <span class="item-subtitle">STM32 / Bare-Metal C / Custom Capacitive Sensors</span></div>
      <div class="item-date">01/2026 – 05/2026</div>
    </div>
    <ul>
      <li>Fabricated custom analog capacitive sensors to measure water permittivity variations (&Delta;&epsilon;<sub>r</sub>) on both flanks; engineered real-time closed-loop PID control firmware on an STM32 microcontroller driving servomotors for dynamic trim stabilization.</li>
    </ul>
  </div>

  <div class="section-title">Professional Experience</div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Valeo</span> – <span class="item-subtitle">Cybersecurity Platform Architect Intern</span></div>
      <div class="item-date">01/2026 – 02/2026 | Créteil, France</div>
    </div>
    <ul>
      <li>Evaluated vulnerability vectors across embedded automotive architectures and interconnected telematics units.</li>
      <li>Contributed to threat modeling matrices aligned with international automotive compliance frameworks (ISO/SAE 21434 and UNECE R155).</li>
      <li>Explored cryptographic countermeasures and integrity validation protocols for in-vehicle networked data exchanges.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Junior Mines Provence</span> – <span class="item-subtitle">Treasurer & Financial Officer</span></div>
      <div class="item-date">01/2026 – 07/2026 | Gardanne, France</div>
    </div>
    <ul>
      <li>Managed financial governance, regulatory compliance, and treasury operations for the school's commercial consulting branch.</li>
      <li>Enforced stringent transaction audit trails and internal control processes, achieving full validation during the national CNJE audit.</li>
      <li>Automated financial reporting workflows and budget tracking dashboards utilizing Google Apps Script and Python.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">BNP Paribas CIB</span> – <span class="item-subtitle">Observation Internship (Trading Infrastructure)</span></div>
      <div class="item-date">04/2021 | Shanghai, China</div>
    </div>
    <ul>
      <li>Observed high-availability network architectures, cyber resilience measures, and real-time data integrity protocols on an active trading floor.</li>
    </ul>
  </div>

  <div class="section-title">Technical Skills</div>
  <div class="skills-table">
    <div class="skills-row">
      <div class="skills-cat">Cybersecurity & Networks:</div>
      <div class="skills-val">Wireshark, TCP/IP, MikroTik RouterOS, DMZ & VLAN segmentation, Firewalls & ACLs, VPN, Port Scanning (Nmap), ISO 21434.</div>
    </div>
    <div class="skills-row">
      <div class="skills-cat">Cryptography & Systems:</div>
      <div class="skills-val">OpenSSL (RSA, AES, ECC, TLS, PKI), Cryptographic Hash Functions, Linux Administration (Debian/Ubuntu, CLI, Bash), Docker.</div>
    </div>
    <div class="skills-row">
      <div class="skills-cat">Programming & Tools:</div>
      <div class="skills-val">Python, C, C++, SQL (PostgreSQL/MySQL), Google Apps Script, Git, Docker Compose, Virtualization.</div>
    </div>
  </div>

  <div class="section-title">Languages</div>
  <div class="lang-row">
    <div class="lang-item"><strong>French:</strong> <span>Native</span></div>
    <div class="lang-item"><strong>English:</strong> <span>Bilingual (C2 – IGCSE & A-Levels)</span></div>
    <div class="lang-item"><strong>Spanish:</strong> <span>Advanced (C1 – DELE)</span></div>
    <div class="lang-item"><strong>Chinese:</strong> <span>Advanced (C1 – HSK 3)</span></div>
    <div class="lang-item"><strong>German:</strong> <span>Elementary (A1/A2 – Independent study, Nicos Weg)</span></div>
  </div>
</body>
</html>"""

def generate_cv3_html():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Theodore Hesling - CV Embedded Software Robotics & Sensors</title>
<style>{CV_CSS}</style>
</head>
<body>
  <div class="header">
    <div class="name">Théodore Hesling</div>
    <div class="title">Engineering Student | Embedded Software, Robotics & Sensor Systems Intern</div>
    <div class="contact-line">
      <span>theodore200531@outlook.com</span> • 
      <span>+33 6 75 49 33 72</span> • 
      <span>Gardanne / Aix-en-Provence, France</span> • 
      <span>French (EU Citizen – Simplified Swiss B/L Permit)</span>
    </div>
    <div class="status-badge">Available for 4 to 5-Month Internship (minimum 16 weeks – CTI requirement) starting April 2027 • Targeting Suisse Romande</div>
  </div>

  <div class="section-title">Professional Summary</div>
  <div class="summary-text">
    Second-year MSc Engineering student at <strong>Mines Saint-Étienne (ISMIN)</strong> with proven expertise in bare-metal embedded C programming (<strong>STM32 / ARM Cortex-M</strong>), custom analog sensor instrumentation, and dynamic closed-loop control algorithms (PID). Proven mechatronic integration skills through the end-to-end prototyping of an autonomous self-levelling vessel with custom capacitive liquid-level sensing and Autodesk Inventor CAD modeling. Bilingual French/English (C2) with exceptional multilingual communication (Spanish C1, Chinese C1, learning German). Seeking a 4 to 5-month internship in Switzerland (focusing on Suisse Romande) in Embedded Software, Robotics, or Smart Sensors starting April 2027.
  </div>

  <div class="section-title">Education</div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Mines Saint-Étienne (ISMIN Campus)</span> – <span class="item-subtitle">Master of Science in Engineering (Diplôme d'Ingénieur)</span></div>
      <div class="item-date">09/2025 – 07/2028 | Gardanne, France</div>
    </div>
    <ul>
      <li><strong>Curriculum Focus:</strong> Embedded Systems, Microelectronics, Sensor Interfacing, Real-Time Software, Hardware-Software Integration.</li>
      <li><strong>Key Coursework:</strong> Microcontroller Architectures (ARM Cortex-M), Object-Oriented Software Design (C++, Python), Digital Electronics & Logic Design (SystemVerilog), Signal Acquisition & Filtering, Feedback Control Systems, CAD & Prototyping.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Lycée Jeanne d’Albret</span> – <span class="item-subtitle">CPGE PC (Classes Préparatoires aux Grandes Écoles – Physics & Chemistry)</span></div>
      <div class="item-date">09/2023 – 07/2025 | St-Germain-en-Laye, France</div>
    </div>
    <ul>
      <li>Rigorous two-year intensive mathematics and physics curriculum with competitive national engineering school examinations.</li>
    </ul>
  </div>

  <div class="section-title">Robotics & Embedded Projects</div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Autonomous Self-Levelling Vessel Prototype</span> – <span class="item-subtitle">STM32 / Bare-Metal C / Custom Capacitive Sensors / CAD</span></div>
      <div class="item-date">01/2026 – 05/2026</div>
    </div>
    <ul>
      <li><strong>Custom Capacitive Water-Level Instrumentation:</strong> Conceived and hand-fabricated custom differential capacitive sensors mounted on port and starboard flanks; quantified liquid dielectric displacement (&Delta;&epsilon;<sub>r</sub>) to accurately gauge real-time water level and hull listing.</li>
      <li><strong>Firmware Signal Conditioning:</strong> Engineered bare-metal STM32 (ARM Cortex-M) C firmware executing high-speed timer-driven capacitive charge/discharge sampling, software digital filtering, and sensor calibration.</li>
      <li><strong>Closed-Loop PID Dynamic Stabilization:</strong> Implemented a real-time feedback PID control algorithm dynamically commanding high-torque PWM servomotors to modulate counter-balancing ballast and keep the vessel level under hydrodynamics perturbations.</li>
      <li><strong>Mechanical CAD Design:</strong> Modeled all hull structures, sensor brackets, and watertight electronics compartments using Autodesk Inventor, followed by 3D printing and bench testing.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Autonomous Obstacle-Avoidance Mobile Robot</span> – <span class="item-subtitle">STM32 / C / Sensor Fusion</span></div>
      <div class="item-date">10/2025 – 01/2026</div>
    </div>
    <ul>
      <li>Built an autonomous wheeled rover utilizing ultrasonic range sensors, analog infrared detectors, and differential motor control.</li>
      <li>Programmed low-level hardware abstraction layers (HAL) and interrupt service routines (ISR) for collision detection and navigation.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Connected Sensing Node & IoT Architecture</span> – <span class="item-subtitle">C++ / Wireless Telemetry</span></div>
      <div class="item-date">09/2026 – 01/2027</div>
    </div>
    <ul>
      <li>Developed an energy-efficient sensing device reading environmental telemetry and streaming metrics via wireless protocols (BLE / Wi-Fi) to a localized data aggregation dashboard.</li>
    </ul>
  </div>

  <div class="section-title">Professional Experience</div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Valeo</span> – <span class="item-subtitle">Cybersecurity Platform Architect Intern</span></div>
      <div class="item-date">01/2026 – 02/2026 | Créteil, France</div>
    </div>
    <ul>
      <li>Analyzed bus communication protocols (CAN, Ethernet) and hardware attack vectors across next-generation vehicular platforms.</li>
      <li>Enhanced understanding of mission-critical automotive reliability, hardware-in-the-loop validation, and secure firmware standards.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">Junior Mines Provence</span> – <span class="item-subtitle">Treasurer & Project Coordinator</span></div>
      <div class="item-date">01/2026 – 07/2026 | Gardanne, France</div>
    </div>
    <ul>
      <li>Managed financial planning and budgetary allocations for technical student engineering missions, demonstrating project delivery discipline and CNJE audit compliance.</li>
    </ul>
  </div>
  <div class="item">
    <div class="item-header">
      <div><span class="item-title">BNP Paribas CIB</span> – <span class="item-subtitle">Observation Internship</span></div>
      <div class="item-date">04/2021 | Shanghai, China</div>
    </div>
    <ul>
      <li>Acquired insights into mission-critical hardware reliability, real-time data flows, and infrastructure redundancy.</li>
    </ul>
  </div>

  <div class="section-title">Technical Skills</div>
  <div class="skills-table">
    <div class="skills-row">
      <div class="skills-cat">Microcontrollers & Hardware:</div>
      <div class="skills-val">STM32 (ARM Cortex-M), Custom Capacitive Sensors, IMU, Actuators (Servomotors, DC motors, PWM), SystemVerilog (basics).</div>
    </div>
    <div class="skills-row">
      <div class="skills-cat">Communication Protocols:</div>
      <div class="skills-val">I2C, SPI, UART, CAN, BLE, USB.</div>
    </div>
    <div class="skills-row">
      <div class="skills-cat">Programming & Control:</div>
      <div class="skills-val">Embedded C, C++, Python, PID feedback control, digital filtering, state machines, Assembly (ARM basics).</div>
    </div>
    <div class="skills-row">
      <div class="skills-cat">CAD & Lab Instrumentation:</div>
      <div class="skills-val">Autodesk Inventor, 3D Printing, Electronics Soldering, Oscilloscopes & Logic Analyzers, STM32CubeIDE, Git.</div>
    </div>
  </div>

  <div class="section-title">Languages</div>
  <div class="lang-row">
    <div class="lang-item"><strong>French:</strong> <span>Native</span></div>
    <div class="lang-item"><strong>English:</strong> <span>Bilingual (C2 – IGCSE & A-Levels)</span></div>
    <div class="lang-item"><strong>Spanish:</strong> <span>Advanced (C1 – DELE)</span></div>
    <div class="lang-item"><strong>Chinese:</strong> <span>Advanced (C1 – HSK 3)</span></div>
    <div class="lang-item"><strong>German:</strong> <span>Elementary (A1/A2 – Independent study, Nicos Weg)</span></div>
  </div>
</body>
</html>"""

def generate_letter_html(number, title, target_companies, company_pitch, tech_points):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Cover Letter {number} - {title} - Theodore Hesling</title>
<style>{LETTER_CSS}</style>
</head>
<body>
  <div class="letter-header">
    <div class="sender-name">Théodore Hesling</div>
    <div class="sender-contact">
      Gardanne / Aix-en-Provence, France • theodore200531@outlook.com • +33 6 75 49 33 72<br>
      <strong>Nationality:</strong> French (EU Citizen – Eligible for Swiss Work Permit B/L without quota delay)
    </div>
  </div>

  <div class="meta-info">
    <div><strong>Date:</strong> [Date of Application]</div>
    <div><strong>Location:</strong> Vaud / Geneva / Neuchâtel, Switzerland</div>
  </div>

  <div class="recipient-box">
    <strong>To:</strong> The Engineering Recruitment Team<br>
    <strong>Company:</strong> [Target Company, e.g. {target_companies}]<br>
    <strong>Location:</strong> [Company Swiss Office / Canton]
  </div>

  <div class="subject-line">
    Subject: Application for {title} – 4 to 5-Month Internship (minimum 16 weeks – CTI requirement) starting April 2027 (Suisse Romande)
  </div>

  <div class="salutation">Dear Hiring Team,</div>

  <p>
    I am writing to express my strong enthusiasm for joining <strong>[Company Name]</strong> as an intern in your engineering division. Currently in my second year of the Master of Science in Engineering at <strong>Mines Saint-Étienne (ISMIN)</strong>, I have dedicated my studies to the synergy between hardware architectures, low-level software, and robust system engineering.
  </p>

  <p>
    {tech_points}
  </p>

  <p>
    Switzerland represents the pinnacle of precision, technological rigor, and innovation. <strong>[Company Name]</strong>'s leadership in {company_pitch} makes your team the ideal environment where I wish to contribute my technical foundation, curiosity, and high standards of execution.
  </p>

  <p>
    In addition to technical competence, I bring an adaptable and multicultural perspective: native French, bilingual English (C2 – IGCSE & A-Levels), certified Spanish (C1), certified Chinese (C1 – HSK 3), and ongoing self-directed study of German (<em>Nicos Weg</em>). My service as Treasurer of Junior Mines Provence cultivated acute accountability, financial governance, and strict compliance with national quality audits. Holding French/EU citizenship ensures a straightforward, quota-free Swiss B/L work authorization process.
  </p>

  <p>
    Available starting <strong>April 2027 for a duration of 4 to 5 months</strong> (fully fulfilling the 16-week French CTI accreditation requirement), I would welcome the opportunity to discuss how my proactive mindset and skills can support <strong>[Company Name]</strong>'s ongoing projects. Thank you for your time and consideration.
  </p>

  <div class="signoff">
    Sincerely,<br><br>
    <div class="signature-name">Théodore Hesling</div>
    <div class="signature-title">MSc Engineering Student – Mines Saint-Étienne (ISMIN)<br>theodore200531@outlook.com | +33 6 75 49 33 72</div>
  </div>
</body>
</html>"""

# Generate CV HTMLs
print("Generating CV HTML files...")
with open(f"{CV_DIR}/CV_1_Embedded_Hardware_Security_Theodore_Hesling.html", "w") as f:
    f.write(generate_cv1_html())
with open(f"{CV_DIR}/CV_2_Cybersecurity_Networks_Infra_Theodore_Hesling.html", "w") as f:
    f.write(generate_cv2_html())
with open(f"{CV_DIR}/CV_3_Embedded_Robotics_Sensors_Theodore_Hesling.html", "w") as f:
    f.write(generate_cv3_html())

# Compile CV PDFs
for i in [1, 2, 3]:
    name = ["Embedded_Hardware_Security", "Cybersecurity_Networks_Infra", "Embedded_Robotics_Sensors"][i-1]
    html_file = f"{CV_DIR}/CV_{i}_{name}_Theodore_Hesling.html"
    pdf_file = f"{CV_DIR}/CV_{i}_{name}_Theodore_Hesling.pdf"
    print(f"Compiling CV {i} to PDF...")
    subprocess.run([
        "google-chrome", "--headless=new", "--disable-gpu", 
        "--no-pdf-header-footer", f"--print-to-pdf={pdf_file}", html_file
    ], check=True)
    # Check page count
    res = subprocess.run(["pdfinfo", pdf_file], capture_output=True, text=True)
    for line in res.stdout.splitlines():
        if "Pages:" in line:
            print(f"  -> CV {i} Page count: {line.strip()}")

# Generate Letters
letter1_tech = """During my previous cybersecurity internship at <strong>Valeo</strong>, I investigated attack surfaces across automotive electronic control units (ECUs) and analyzed secure communication protocols (CAN-FD, secure boot primitives) against ISO/SAE 21434 standards. In parallel, my academic engineering projects have grounded my skills in physical hardware: I designed an autonomous self-levelling vessel driven by an <strong>STM32 (ARM Cortex-M)</strong> running bare-metal C to execute real-time closed-loop PID control over <strong>custom-built differential capacitive water-level sensors</strong> measuring liquid permittivity variations. Furthermore, my current flagship IoT project incorporates <strong>OpenSSL cryptographic primitives</strong> and TLS/DTLS mutual authentication to secure embedded telemetry data against replay and tampering."""
letter1_pitch = "hardware-rooted trust, secure microcontrollers, and resilient embedded architectures"

letter2_tech = """My academic training at Mines Saint-Étienne emphasizes rigorous hands-on defense engineering. In our enterprise network security labs (SRIE), I configured and audited multi-tiered topologies featuring <strong>MikroTik RouterOS firewalls, demilitarized zones (DMZs), and dual-homed servers</strong>, conducting deep packet inspections with <strong>Wireshark</strong> to uncover port scanning and lateral intrusion tactics. On the offensive and compliance side, my internship at <strong>Valeo</strong> provided me with direct exposure to threat analysis across interconnected automotive platforms, while my observation internship at <strong>BNP Paribas CIB</strong> in Shanghai gave me first-hand insight into the non-negotiable uptime and data integrity protocols governing high-frequency trading floors."""
letter2_pitch = "sovereign digital resilience, advanced network defense, and high-assurance security operations"

letter3_tech = """During my engineering studies, I directed and developed the embedded architecture for an <strong>autonomous self-levelling scale vessel</strong>. Programmed in bare-metal C on an <strong>STM32 (ARM Cortex-M)</strong> microcontroller, the platform executes a real-time <strong>closed-loop PID control algorithm</strong> that samples <strong>custom-fabricated differential capacitive sensors</strong> measuring liquid permittivity variations on each side of the hull to dynamically modulate PWM servomotors and counteract hydrodynamic disturbances. Complementing the firmware, I designed the structural hull components and sensor mounts using <strong>Autodesk Inventor CAD</strong>, giving me a complete perspective on electromechanical co-design and physical prototyping."""
letter3_pitch = "ultra-responsive embedded devices, high-precision actuation, and intelligent sensor architectures"

letters = [
    (1, "Embedded Security Engineering Intern / Firmware Security Intern", "Kudelski Group / STMicroelectronics / SICPA", letter1_pitch, letter1_tech, "Cover_Letter_1_Embedded_Hardware_Security"),
    (2, "Cyber Defense Intern / Network Security Intern / SOC Analyst Intern", "Swisscom / ELCA Security / Proton / Swiss Private Banks", letter2_pitch, letter2_tech, "Cover_Letter_2_Cybersecurity_Infrastructure"),
    (3, "Embedded Software Intern / Robotics Firmware Intern / Sensor Systems Intern", "Logitech / Sensirion / Maxon Motor / Flyability / CSEM", letter3_pitch, letter3_tech, "Cover_Letter_3_Robotics_Embedded_Systems")
]

for num, title, targets, pitch, tech, base_name in letters:
    html_content = generate_letter_html(num, title, targets, pitch, tech)
    html_file = f"{CV_DIR}/{base_name}.html"
    odt_file = f"{CV_DIR}/{base_name}.odt"
    pdf_file = f"{CV_DIR}/{base_name}.pdf"
    
    with open(html_file, "w") as f:
        f.write(html_content)
    
    print(f"Converting {base_name} to ODT for LibreOffice...")
    subprocess.run([
        "libreoffice", "--headless", "--convert-to", "odt:writer8", html_file
    ], cwd=CV_DIR, check=True)
    
    print(f"Compiling {base_name} to PDF...")
    subprocess.run([
        "google-chrome", "--headless=new", "--disable-gpu", 
        "--no-pdf-header-footer", f"--print-to-pdf={pdf_file}", html_file
    ], check=True)

print("ALL BUILDS COMPLETED SUCCESSFULLY!")
