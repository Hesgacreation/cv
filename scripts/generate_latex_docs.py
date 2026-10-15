import subprocess
import os
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LATEX_DIR = os.path.join(BASE_DIR, "latex")
PDF_DIR = os.path.join(BASE_DIR, "pdf")

# Shared FlowCV-identical preamble
PREAMBLE_CV = r"""\documentclass[10pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{charter}
\usepackage{geometry}
\geometry{
  a4paper,
  left=18mm,
  right=18mm,
  top=14mm,
  bottom=14mm
}
\usepackage{tikz}
\usepackage{tabularx}
\usepackage{qrcode}
\usepackage{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor=black,
  urlcolor=black
}

\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\linespread{1.04}

% Custom vector icons matching FlowCV
\newcommand{\iconEnvelope}{%
\begin{tikzpicture}[x=0.075em, y=0.075em, baseline=-0.22em]
  \draw[line width=0.55pt, rounded corners=0.4pt, fill=black] (0,0) rectangle (12,8.2);
  \draw[line width=0.5pt, color=white] (0.8,7.5) -- (6,3.5) -- (11.2,7.5);
\end{tikzpicture}%
}

\newcommand{\iconPhone}{%
\begin{tikzpicture}[x=0.065em, y=0.065em, baseline=-0.22em]
  \draw[line width=1.0pt, line cap=round, line join=round, fill=black] 
    (2,8.5) .. controls (1.5,9.5) and (3,10.5) .. (4.2,10.2)
    -- (5.3,8.5) .. controls (5.6,8) and (5.2,7.3) .. (4.6,7.1)
    -- (4.1,7) .. controls (4.4,5.4) and (5.4,4.4) .. (7,4.1)
    -- (7.1,4.6) .. controls (7.3,5.2) and (8,5.6) .. (8.5,5.3)
    -- (10.2,4.2) .. controls (10.5,3) and (9.5,1.5) .. (8.5,2)
    .. controls (5,2) and (2,5) .. (2,8.5) -- cycle;
\end{tikzpicture}%
}

\newcommand{\iconLocation}{%
\begin{tikzpicture}[x=0.075em, y=0.075em, baseline=-0.22em]
  \path[fill=black] (5,10) .. controls (2.2,10) and (0,7.8) .. (0,5)
    .. controls (0,1.8) and (5,-2) .. (5,-2)
    .. controls (5,-2) and (10,1.8) .. (10,5)
    .. controls (10,7.8) and (7.8,10) .. (5,10) -- cycle;
  \fill[white] (5,5.2) circle (1.8);
\end{tikzpicture}%
}

\newcommand{\iconLinkedIn}{%
\begin{tikzpicture}[x=0.075em, y=0.075em, baseline=-0.22em]
  \fill[black, rounded corners=1.2pt] (0,0) rectangle (11,11);
  \fill[white] (2.2,2.2) rectangle (4.2,7.2);
  \fill[white] (3.2,9.2) circle (1.1);
  \fill[white] (5.5,2.2) rectangle (7.5,7.2);
  \fill[white] (5.5,5.5) arc (180:0:1.7) -- (8.9,2.2) -- (7.5,2.2) -- (7.5,5.2) arc (0:180:0.7) -- (6.1,2.2) -- cycle;
\end{tikzpicture}%
}

% Section Header matching FlowCV: Bold uppercase title + thin full-width line
\newcommand{\cvSection}[1]{%
  \vspace{6.5pt}%
  {\fontsize{10.5}{12}\selectfont \textbf{#1}}\par\vspace{1.5pt}%
  \rule{\textwidth}{0.75pt}\par\vspace{4.5pt}%
}

% Item for Education / Experience matching FlowCV two-column row
\newcommand{\cvItem}[4]{%
  \noindent
  \parbox[t]{0.75\textwidth}{\raggedright \textbf{#1}}\hfill
  \parbox[t]{0.24\textwidth}{\raggedleft \fontsize{8.5}{10.5}\selectfont #2}\par
  \vspace{1.5pt}
  \noindent
  \parbox[t]{0.75\textwidth}{\fontsize{8.7}{11.2}\selectfont #4}\hfill
  \parbox[t]{0.24\textwidth}{\raggedleft \fontsize{8.5}{10.5}\selectfont #3}\par
  \vspace{5pt}
}
"""

PREAMBLE_LETTER = r"""\documentclass[10.5pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{charter}
\usepackage{geometry}
\geometry{
  a4paper,
  left=20mm,
  right=20mm,
  top=18mm,
  bottom=18mm
}
\usepackage{tikz}
\usepackage{hyperref}
\hypersetup{
  colorlinks=true,
  linkcolor=black,
  urlcolor=black
}

\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{7pt}
\linespread{1.12}

% Custom vector icons matching FlowCV
\newcommand{\iconEnvelope}{%
\begin{tikzpicture}[x=0.075em, y=0.075em, baseline=-0.22em]
  \draw[line width=0.55pt, rounded corners=0.4pt, fill=black] (0,0) rectangle (12,8.2);
  \draw[line width=0.5pt, color=white] (0.8,7.5) -- (6,3.5) -- (11.2,7.5);
\end{tikzpicture}%
}

\newcommand{\iconPhone}{%
\begin{tikzpicture}[x=0.065em, y=0.065em, baseline=-0.22em]
  \draw[line width=1.0pt, line cap=round, line join=round, fill=black] 
    (2,8.5) .. controls (1.5,9.5) and (3,10.5) .. (4.2,10.2)
    -- (5.3,8.5) .. controls (5.6,8) and (5.2,7.3) .. (4.6,7.1)
    -- (4.1,7) .. controls (4.4,5.4) and (5.4,4.4) .. (7,4.1)
    -- (7.1,4.6) .. controls (7.3,5.2) and (8,5.6) .. (8.5,5.3)
    -- (10.2,4.2) .. controls (10.5,3) and (9.5,1.5) .. (8.5,2)
    .. controls (5,2) and (2,5) .. (2,8.5) -- cycle;
\end{tikzpicture}%
}

\newcommand{\iconLocation}{%
\begin{tikzpicture}[x=0.075em, y=0.075em, baseline=-0.22em]
  \path[fill=black] (5,10) .. controls (2.2,10) and (0,7.8) .. (0,5)
    .. controls (0,1.8) and (5,-2) .. (5,-2)
    .. controls (5,-2) and (10,1.8) .. (10,5)
    .. controls (10,7.8) and (7.8,10) .. (5,10) -- cycle;
  \fill[white] (5,5.2) circle (1.8);
\end{tikzpicture}%
}
"""

def get_header(subtitle, with_qr=False):
    if not with_qr:
        return r"""
\begin{center}
  {\fontsize{20}{24}\selectfont \textbf{THEODORE HESLING}}\\[3pt]
  {\fontsize{10}{12}\selectfont \textit{""" + subtitle + r"""}}\\[5pt]
  {\fontsize{8.5}{10}\selectfont 
    \iconEnvelope~theodore200531@outlook.com \quad
    \iconPhone~0675493372 \quad
    \iconLocation~Gardanne 13120, France
  }
\end{center}
\vspace{-4pt}
"""
    else:
        return r"""
\noindent
\begin{minipage}[c]{0.81\textwidth}
  {\fontsize{20}{24}\selectfont \textbf{THEODORE HESLING}}\\[3pt]
  {\fontsize{9.6}{11.8}\selectfont \textit{""" + subtitle + r"""}}\\[5pt]
  {\fontsize{8.5}{10}\selectfont 
    \iconEnvelope~theodore200531@outlook.com \quad
    \iconPhone~0675493372 \quad
    \iconLocation~Gardanne 13120, France\\[2pt]
    \iconLinkedIn~\href{https://www.linkedin.com/in/théodore-hesling-a08316386}{linkedin.com/in/théodore-hesling-a08316386}
  }
\end{minipage}\hfill
\begin{minipage}[c]{0.17\textwidth}
  \centering
  \qrcode[height=18mm]{https://www.linkedin.com/in/th%C3%A9odore-hesling-a08316386}\\[2pt]
  {\fontsize{7}{8.5}\selectfont \textbf{LinkedIn Profile}}
\end{minipage}
\vspace{3pt}
"""

BODY_CV1 = r"""
% PROFILE
\cvSection{PROFILE}
{\fontsize{8.8}{11.5}\selectfont Cybersecurity and Embedded Systems Engineering candidate at Mines Saint-Étienne (ISMIN), combining hands-on practice in hardware security at Valeo and financial infrastructure exposure at BNP Paribas. Proficient in bare-metal C (STM32), applied cryptography, and hardware design. Motivated to contribute to Swiss innovation in embedded hardware security, IoT platforms, and secure firmware development. EU citizen eligible for simplified Swiss L/B work permits.\par}

% EDUCATION
\cvSection{EDUCATION}
\cvItem{Engineer Degree (M.Sc) - Mines de Saint Etienne}{09/2025 -- 07/2028}{Gardanne}{Engineering Degree candidate at Mines Saint-Étienne (ISMIN cycle). Double specialization in Microelectronics and Embedded Systems. Core coursework: Hardware Security, Cryptography (AES, RSA, ECC), Microcontroller Architectures (ARM Cortex-M), RTOS, VHDL/SystemVerilog, and IoT Networks.}

\cvItem{CPGE PC - Lycée Jeanne d'Albret}{09/2023 -- 07/2025}{SAINT GERMAIN EN LAYE}{Intensive two-year undergraduate program in Advanced Physics, Chemistry, and Mathematics preparing for competitive nationwide entrance exams to French Engineering Grandes Écoles.}

% EXPERIENCE
\cvSection{EXPERIENCE}
\cvItem{Treasurer - Junior Mines Provence}{01/2026 -- 07/2026}{Gardanne}{Managing the student engineering consulting firm's financial operations, overseeing budgets, financial reporting, and ensuring rigorous tax compliance and national CNJE audit standards.}

\cvItem{Cybersecurity Platform Architect Intern - Valeo}{01/2026 -- 02/2026}{Créteil}{Conducted risk assessments and evaluated secure communication protocols for connected automotive architectures. Investigated threat models and hardware-assisted cryptographic primitives to prevent unauthorized firmware modification.}

\cvItem{Autonomous Boat Prototype (Self-Levelling) - Mines Saint-Étienne}{10/2025 -- 03/2026}{Gardanne}{Engineered a closed-loop trim-stabilized boat using STM32 bare-metal C. Designed custom differential capacitive liquid level sensors measuring water-column permittivity shifts, interfaced via ADC to a real-time PID controller driving ballast servomotors. Modelled hull in Autodesk Inventor.}

\cvItem{Observation Internship - BNP Paribas CIB}{04/2021 -- 04/2021}{Shanghai}{Gained early exposure to the mission-critical digital infrastructure of a global trading floor, observing network resilience protocols, operational security constraints, and data integrity safeguards.}

% SKILLS
\cvSection{SKILLS}
\begin{tabularx}{\textwidth}{@{}X X@{}}
  \textbf{C / Embedded C} \newline
  {\fontsize{8.5}{10.5}\selectfont Skillful (STM32, ARM Cortex-M, Bare-metal, FreeRTOS)} &
  \textbf{Hardware Security \& Cryptography} \newline
  {\fontsize{8.5}{10.5}\selectfont Skillful (AES, ECC, SHA, OpenSSL, Secure Boot)} \\[4.5pt]
  
  \textbf{Python} \newline
  {\fontsize{8.5}{10.5}\selectfont Experienced (Automation, Scripting, NumPy)} &
  \textbf{CAD \& Prototyping} \newline
  {\fontsize{8.5}{10.5}\selectfont Skillful (Autodesk Inventor, PCB Prototyping)} \\[4.5pt]
  
  \textbf{Hardware Description} \newline
  {\fontsize{8.5}{10.5}\selectfont Intermediate (SystemVerilog, VHDL, FPGA)} &
  \textbf{Protocols \& Tooling} \newline
  {\fontsize{8.5}{10.5}\selectfont Intermediate (SPI, I2C, UART, CAN, Git, Linux, GDB)}
\end{tabularx}

% LANGUAGES
\cvSection{LANGUAGES}
\begin{tabularx}{\textwidth}{@{}X X@{}}
  \textbf{French} \newline
  {\fontsize{8.5}{10.5}\selectfont Native speaker} &
  \textbf{English} \newline
  {\fontsize{8.5}{10.5}\selectfont C2 -- Bilingual (IGCSE \& A-Levels)} \\[4.5pt]
  
  \textbf{Spanish} \newline
  {\fontsize{8.5}{10.5}\selectfont C1 -- Fluent (DELE Diploma)} &
  \textbf{Chinese (Mandarin)} \newline
  {\fontsize{8.5}{10.5}\selectfont C1 -- Fluent (HSK 3)} \\[4.5pt]
  
  \textbf{German} \newline
  {\fontsize{8.5}{10.5}\selectfont Elementary (A1/A2, self-study with Nicos Weg)} &
  \textbf{Swiss Work Authorization} \newline
  {\fontsize{8.5}{10.5}\selectfont French / EU Citizen (Fast-track L/B Permit)}
\end{tabularx}
"""

BODY_CV2 = r"""
% PROFILE
\cvSection{PROFILE}
{\fontsize{8.8}{11.5}\selectfont Cybersecurity-focused Engineering candidate at Mines Saint-Étienne (ISMIN) with hands-on experience in securing automotive architectures at Valeo and financial infrastructure exposure at BNP Paribas CIB. Combining deep expertise in OpenSSL, network security protocols, system hardening, and automation with multilingual fluency. Motivated to safeguard critical Swiss enterprise, financial, and cloud environments. EU citizen eligible for simplified Swiss L/B work permits.\par}

% EDUCATION
\cvSection{EDUCATION}
\cvItem{Engineer Degree (M.Sc) - Mines de Saint Etienne}{09/2025 -- 07/2028}{Gardanne}{Engineering Degree candidate at Mines Saint-Étienne (ISMIN cycle). Specialization in Computer Science, Distributed Systems, and Cybersecurity. Core coursework: Network Security, Applied Cryptography, Linux Kernel \& OS Security, Cloud Infrastructure, and Threat Modeling.}

\cvItem{CPGE PC - Lycée Jeanne d'Albret}{09/2023 -- 07/2025}{SAINT GERMAIN EN LAYE}{Intensive two-year undergraduate program in Advanced Physics, Chemistry, and Mathematics preparing for competitive nationwide entrance exams to French Engineering Grandes Écoles.}

% EXPERIENCE
\cvSection{EXPERIENCE}
\cvItem{Treasurer - Junior Mines Provence}{01/2026 -- 07/2026}{Gardanne}{Overseeing treasury and fiscal governance for the student engineering consulting firm, enforcing budgetary compliance, internal risk controls, and passing national audits conducted by the CNJE.}

\cvItem{Cybersecurity Platform Architect Intern - Valeo}{01/2026 -- 02/2026}{Créteil}{Conducted cybersecurity threat analysis, vulnerability assessments, and risk remediation on vehicle software platforms. Audited cryptographic key management and secure diagnostic communication channels against UNECE R155/156 standards.}

\cvItem{Secure IoT Telemetry Infrastructure - Mines Saint-Étienne}{10/2025 -- 03/2026}{Gardanne}{Implemented an end-to-end authenticated IoT data pipeline utilizing OpenSSL for TLS/DTLS mutual authentication, symmetric stream encryption, and cryptographic integrity verification on connected sensor nodes.}

\cvItem{Observation Internship - BNP Paribas CIB}{04/2021 -- 04/2021}{Shanghai}{Immersed in the digital infrastructure of a high-frequency trading floor, studying low-latency network topologies, disaster recovery configurations, and cybersecurity defense-in-depth measures.}

% SKILLS
\cvSection{SKILLS}
\begin{tabularx}{\textwidth}{@{}X X@{}}
  \textbf{Cybersecurity \& Cryptography} \newline
  {\fontsize{8.5}{10.5}\selectfont Skillful (OpenSSL, TLS/SSL, PKI, AES/RSA/ECC, Threat Analysis)} &
  \textbf{System Security \& Networks} \newline
  {\fontsize{8.5}{10.5}\selectfont Experienced (TCP/IP, Wireshark, Linux Hardening, Firewalls, SSH)} \\[4.5pt]
  
  \textbf{Python \& Automation} \newline
  {\fontsize{8.5}{10.5}\selectfont Experienced (Python Scripting, Bash, Google Apps Script, APIs)} &
  \textbf{Low-Level Systems} \newline
  {\fontsize{8.5}{10.5}\selectfont Intermediate (C, Memory Safety, Reverse Engineering Basics)} \\[4.5pt]
  
  \textbf{Cloud \& DevOps Basics} \newline
  {\fontsize{8.5}{10.5}\selectfont Intermediate (Docker, Linux Administration, Git, CI/CD)} &
  \textbf{Compliance \& Risk} \newline
  {\fontsize{8.5}{10.5}\selectfont Intermediate (ISO 27001, UNECE R155, Risk Assessment)}
\end{tabularx}

% LANGUAGES
\cvSection{LANGUAGES}
\begin{tabularx}{\textwidth}{@{}X X@{}}
  \textbf{French} \newline
  {\fontsize{8.5}{10.5}\selectfont Native speaker} &
  \textbf{English} \newline
  {\fontsize{8.5}{10.5}\selectfont C2 -- Bilingual (IGCSE \& A-Levels)} \\[4.5pt]
  
  \textbf{Spanish} \newline
  {\fontsize{8.5}{10.5}\selectfont C1 -- Fluent (DELE Diploma)} &
  \textbf{Chinese (Mandarin)} \newline
  {\fontsize{8.5}{10.5}\selectfont C1 -- Fluent (HSK 3)} \\[4.5pt]
  
  \textbf{German} \newline
  {\fontsize{8.5}{10.5}\selectfont Elementary (A1/A2, self-study with Nicos Weg)} &
  \textbf{Swiss Work Authorization} \newline
  {\fontsize{8.5}{10.5}\selectfont French / EU Citizen (Fast-track L/B Permit)}
\end{tabularx}
"""

BODY_CV3 = r"""
% PROFILE
\cvSection{PROFILE}
{\fontsize{8.8}{11.5}\selectfont Systems Engineering candidate at Mines Saint-Étienne (ISMIN) specializing in embedded architectures, autonomous robotics, and sensor physics. Proven track record in prototyping complex mechatronic systems, bare-metal C programming on ARM Cortex-M, and designing custom capacitive sensors. Motivated to contribute to Swiss robotics, medical instrumentation, and precision industrial automation. EU citizen eligible for simplified Swiss L/B work permits.\par}

% EDUCATION
\cvSection{EDUCATION}
\cvItem{Engineer Degree (M.Sc) - Mines de Saint Etienne}{09/2025 -- 07/2028}{Gardanne}{Engineering Degree candidate at Mines Saint-Étienne (ISMIN cycle). Specialization in Embedded Systems and Autonomous Mechatronics. Core coursework: Microcontroller Architectures (STM32), Real-Time Operating Systems (FreeRTOS), Sensor Acquisition \& Signal Processing, Feedback Control (PID), and 3D CAD.}

\cvItem{CPGE PC - Lycée Jeanne d'Albret}{09/2023 -- 07/2025}{SAINT GERMAIN EN LAYE}{Intensive two-year undergraduate program in Advanced Physics, Chemistry, and Mathematics preparing for competitive nationwide entrance exams to French Engineering Grandes Écoles.}

% EXPERIENCE
\cvSection{EXPERIENCE}
\cvItem{Autonomous Boat Prototype (Self-Levelling) - Mines Saint-Étienne}{10/2025 -- 03/2026}{Gardanne}{Engineered a self-levelling catamaran using STM32 bare-metal C. Developed custom differential capacitive liquid level sensors measuring water-column dielectric variation ($\Delta\epsilon_r$), processed via ADC into a real-time PID stabilization loop driving ballast servomotors. Modelled mechanical chassis in Autodesk Inventor.}

\cvItem{Treasurer - Junior Mines Provence}{01/2026 -- 07/2026}{Gardanne}{Managing financial operations and budget allocations for engineering projects, tracking procurement for technical prototyping, and ensuring strict compliance with CNJE audit guidelines.}

\cvItem{Cybersecurity Platform Architect Intern - Valeo}{01/2026 -- 02/2026}{Créteil}{Analyzed embedded bus communications (CAN/LIN) and evaluated real-time sensor data integrity in safety-critical electronic control units.}

\cvItem{Observation Internship - BNP Paribas CIB}{04/2021 -- 04/2021}{Shanghai}{Observed mission-critical automated infrastructure, fault-tolerant system monitoring, and low-latency data telemetry in a global financial institution.}

% SKILLS
\cvSection{SKILLS}
\begin{tabularx}{\textwidth}{@{}X X@{}}
  \textbf{Embedded Software} \newline
  {\fontsize{8.5}{10.5}\selectfont Skillful (C, Bare-metal STM32, ARM Cortex-M, FreeRTOS, HAL)} &
  \textbf{Sensor Design \& Physics} \newline
  {\fontsize{8.5}{10.5}\selectfont Skillful (Capacitive Sensing, Dielectric $\Delta\epsilon_r$, Signal Conditioning)} \\[4.5pt]
  
  \textbf{Control Systems \& CAD} \newline
  {\fontsize{8.5}{10.5}\selectfont Skillful (PID Closed-Loop, Autodesk Inventor, Prototyping)} &
  \textbf{Hardware Interfaces} \newline
  {\fontsize{8.5}{10.5}\selectfont Experienced (ADC, PWM, Timers, SPI, I2C, UART, CAN Bus)} \\[4.5pt]
  
  \textbf{Python \& Data Processing} \newline
  {\fontsize{8.5}{10.5}\selectfont Experienced (Python, NumPy, Matplotlib, Data Acquisition)} &
  \textbf{Lab Equipment \& Tooling} \newline
  {\fontsize{8.5}{10.5}\selectfont Intermediate (Oscilloscopes, Logic Analyzers, Multimeters, Soldering, Git)}
\end{tabularx}

% LANGUAGES
\cvSection{LANGUAGES}
\begin{tabularx}{\textwidth}{@{}X X@{}}
  \textbf{French} \newline
  {\fontsize{8.5}{10.5}\selectfont Native speaker} &
  \textbf{English} \newline
  {\fontsize{8.5}{10.5}\selectfont C2 -- Bilingual (IGCSE \& A-Levels)} \\[4.5pt]
  
  \textbf{Spanish} \newline
  {\fontsize{8.5}{10.5}\selectfont C1 -- Fluent (DELE Diploma)} &
  \textbf{Chinese (Mandarin)} \newline
  {\fontsize{8.5}{10.5}\selectfont C1 -- Fluent (HSK 3)} \\[4.5pt]
  
  \textbf{German} \newline
  {\fontsize{8.5}{10.5}\selectfont Elementary (A1/A2, self-study with Nicos Weg)} &
  \textbf{Swiss Work Authorization} \newline
  {\fontsize{8.5}{10.5}\selectfont French / EU Citizen (Fast-track L/B Permit)}
\end{tabularx}
"""

# ==================== COVER LETTERS ====================
COVER_LETTER_1_TEX = PREAMBLE_LETTER + r"""
\begin{document}

% HEADER
\begin{center}
  {\fontsize{20}{24}\selectfont \textbf{THÉODORE HESLING}}\\[4pt]
  {\fontsize{9}{11}\selectfont 
    \iconEnvelope~theodore200531@outlook.com \quad
    \iconPhone~+33 6 75 49 33 72 \quad
    \iconLocation~Gardanne / Aix-en-Provence, France
  }\\[3pt]
  {\fontsize{8.5}{10.5}\selectfont \textit{Nationality: French (EU Citizen -- Eligible for Swiss Work Permit B/L without quota delay)}}\par
  \vspace{4pt}
  \rule{\textwidth}{0.8pt}
\end{center}
\vspace{2pt}

% RECIPIENT & DATE
\noindent
\begin{minipage}[t]{0.65\textwidth}
  \textbf{To:} The Engineering Recruitment Team\\
  \textbf{Company:} [Target Company, e.g., Kudelski Group / STMicroelectronics / SICPA]\\
  \textbf{Location:} Vaud / Geneva / Neuchâtel, Switzerland
\end{minipage}\hfill
\begin{minipage}[t]{0.32\textwidth}
  \raggedleft
  \textbf{Date:} [Date of Application]
\end{minipage}

\vspace{10pt}
\noindent \textbf{Subject: Application for Embedded Security Engineering Intern (4 to 5 Months -- from April 2027)}\par
\vspace{4pt}

Dear Hiring Team,

I am writing to express my strong enthusiasm for joining \textbf{[Company Name]} as an intern in your engineering division. Currently in my second year of the Master of Science in Engineering at \textbf{Mines Saint-Étienne (ISMIN)}, I have focused my studies on the synergy between microcontroller architectures, low-level software, and robust hardware security.

During my cybersecurity internship at \textbf{Valeo}, I evaluated attack surfaces across electronic control units (ECUs) and analyzed secure communication protocols against automotive security standards. In parallel, my academic engineering projects have grounded my skills in physical hardware: I designed an autonomous self-levelling vessel driven by an \textbf{STM32 (ARM Cortex-M)} running bare-metal C to execute real-time closed-loop PID control over \textbf{custom-built differential capacitive water-level sensors} measuring liquid permittivity variations. Furthermore, my current coursework and projects incorporate \textbf{OpenSSL cryptographic primitives}, secure boot architectures, and mutual authentication to safeguard embedded endpoints.

Switzerland represents the pinnacle of precision, technological rigor, and innovation. \textbf{[Company Name]}'s leadership in hardware-rooted trust, secure silicon, and resilient embedded architectures makes your team the ideal environment where I wish to contribute my technical foundation, curiosity, and high standards of execution.

In addition to technical competence, I bring an adaptable and multicultural perspective: native French, bilingual English (C2 -- IGCSE \& A-Levels), certified Spanish (C1), certified Chinese (C1 -- HSK 3), and ongoing self-directed study of German (\textit{Nicos Weg}). My service as Treasurer of Junior Mines Provence cultivated acute accountability, financial governance, and strict compliance with national quality audits. Holding French/EU citizenship ensures a straightforward, quota-free Swiss B/L work authorization process.

Available starting \textbf{April 2027 for a duration of 4 to 5 months} (fully fulfilling the 16-week French CTI accreditation requirement), I would welcome the opportunity to discuss how my proactive mindset and skills can support \textbf{[Company Name]}'s ongoing projects. Thank you for your time and consideration.

\vspace{14pt}
\noindent Sincerely,\\[18pt]
\textbf{Théodore Hesling}\\[2pt]
{\small MSc Engineering Student -- Mines Saint-Étienne (ISMIN)\\
theodore200531@outlook.com \quad +33 6 75 49 33 72}

\end{document}
"""

COVER_LETTER_2_TEX = PREAMBLE_LETTER + r"""
\begin{document}

% HEADER
\begin{center}
  {\fontsize{20}{24}\selectfont \textbf{THÉODORE HESLING}}\\[4pt]
  {\fontsize{9}{11}\selectfont 
    \iconEnvelope~theodore200531@outlook.com \quad
    \iconPhone~+33 6 75 49 33 72 \quad
    \iconLocation~Gardanne / Aix-en-Provence, France
  }\\[3pt]
  {\fontsize{8.5}{10.5}\selectfont \textit{Nationality: French (EU Citizen -- Eligible for Swiss Work Permit B/L without quota delay)}}\par
  \vspace{4pt}
  \rule{\textwidth}{0.8pt}
\end{center}
\vspace{2pt}

% RECIPIENT & DATE
\noindent
\begin{minipage}[t]{0.65\textwidth}
  \textbf{To:} The Information Security \& Infrastructure Recruitment Team\\
  \textbf{Company:} [Target Company, e.g., Proton / ELCA / Kudelski Security / Swisscom]\\
  \textbf{Location:} Geneva / Lausanne / Vaud, Switzerland
\end{minipage}\hfill
\begin{minipage}[t]{0.32\textwidth}
  \raggedleft
  \textbf{Date:} [Date of Application]
\end{minipage}

\vspace{10pt}
\noindent \textbf{Subject: Application for Cybersecurity \& Cloud Infrastructure Intern (4 to 5 Months -- from April 2027)}\par
\vspace{4pt}

Dear Hiring Team,

I am writing to express my eager interest in joining \textbf{[Company Name]}'s cybersecurity and digital trust engineering division. Currently enrolled in the second year of the Master of Science in Engineering at \textbf{Mines Saint-Étienne (ISMIN)}, I have developed a strong specialization in computer systems security, applied cryptography, and network resilience.

My professional experience at \textbf{Valeo} immersed me in cybersecurity risk analysis, threat modeling, and protocol auditing, where I identified vulnerability vectors and evaluated mitigation strategies against international regulations. This experience was further informed by early observation of the high-security infrastructure of \textbf{BNP Paribas CIB}'s global trading floor in Shanghai, exposing me to high-availability network topologies and zero-trust paradigms. In my engineering curriculum, I engineered an end-to-end secure IoT telemetry pipeline using \textbf{OpenSSL} for mutual TLS authentication and cryptographic message integrity.

Switzerland is recognized worldwide as a premier hub for data privacy, cryptographic excellence, and secure infrastructure. \textbf{[Company Name]}'s unwavering commitment to privacy, sovereignty, and state-of-the-art defense makes your engineering team the benchmark for my professional aspirations.

Beyond technical expertise, I offer an international background and versatile communication skills: native French, bilingual English (C2 -- Cambridge/IGCSE), certified Spanish (C1), certified Chinese (C1 -- HSK 3), and actively progressing in German (\textit{Nicos Weg}). Serving as Treasurer of Junior Mines Provence honed my discipline in regulatory audits, budget control, and organizational risk management. As an EU citizen, I benefit from simplified, quota-exempt Swiss B/L work authorization.

Available starting \textbf{April 2027 for a duration of 4 to 5 months} (minimum 16 weeks to validate my French CTI degree requirements), I am eager to contribute my energy, rigor, and technical dedication to \textbf{[Company Name]}'s mission. Thank you for considering my application.

\vspace{14pt}
\noindent Sincerely,\\[18pt]
\textbf{Théodore Hesling}\\[2pt]
{\small MSc Engineering Student -- Mines Saint-Étienne (ISMIN)\\
theodore200531@outlook.com \quad +33 6 75 49 33 72}

\end{document}
"""

COVER_LETTER_3_TEX = PREAMBLE_LETTER + r"""
\begin{document}

% HEADER
\begin{center}
  {\fontsize{20}{24}\selectfont \textbf{THÉODORE HESLING}}\\[4pt]
  {\fontsize{9}{11}\selectfont 
    \iconEnvelope~theodore200531@outlook.com \quad
    \iconPhone~+33 6 75 49 33 72 \quad
    \iconLocation~Gardanne / Aix-en-Provence, France
  }\\[3pt]
  {\fontsize{8.5}{10.5}\selectfont \textit{Nationality: French (EU Citizen -- Eligible for Swiss Work Permit B/L without quota delay)}}\par
  \vspace{4pt}
  \rule{\textwidth}{0.8pt}
\end{center}
\vspace{2pt}

% RECIPIENT & DATE
\noindent
\begin{minipage}[t]{0.65\textwidth}
  \textbf{To:} The Robotics \& Systems Engineering Recruitment Team\\
  \textbf{Company:} [Target Company, e.g., Logitech / SenseFly / LEM / Sonceboz]\\
  \textbf{Location:} Vaud / Geneva / Neuchâtel, Switzerland
\end{minipage}\hfill
\begin{minipage}[t]{0.32\textwidth}
  \raggedleft
  \textbf{Date:} [Date of Application]
\end{minipage}

\vspace{10pt}
\noindent \textbf{Subject: Application for Embedded Systems \& Robotics Engineering Intern (4 to 5 Months -- from April 2027)}\par
\vspace{4pt}

Dear Hiring Team,

I am writing to express my strong motivation to join \textbf{[Company Name]} as an Embedded Systems and Robotics Engineering Intern. Currently completing my second year of Master of Science in Engineering at \textbf{Mines Saint-Étienne (ISMIN)}, I specialize in autonomous systems, microcontroller architectures, and smart sensor integration.

My academic journey is centered on hands-on physical prototyping. Most recently, I led the development of an autonomous self-levelling catamaran. I authored bare-metal C firmware for an \textbf{STM32 (ARM Cortex-M)} to run a real-time closed-loop PID control algorithm, designed \textbf{custom differential capacitive level sensors} measuring liquid dielectric shifts ($\Delta\epsilon_r$), and modeled the mechanical hull in \textbf{Autodesk Inventor}. In parallel, my cybersecurity internship at \textbf{Valeo} gave me deep insight into communication bus robustness (CAN, LIN) and sensor data integrity in safety-critical electronic control units.

Switzerland's global leadership in microtechnology, advanced robotics, and precision instruments represents the exact environment where I wish to build my career. \textbf{[Company Name]}'s reputation for engineering elegance and mechatronic excellence makes this opportunity the ideal place to apply my skills.

In addition to technical competencies, I offer multilingual fluency: native French, bilingual English (C2 -- IGCSE \& A-Levels), certified Spanish (C1), certified Chinese (C1 -- HSK 3), and beginner German (\textit{Nicos Weg}). As Treasurer of Junior Mines Provence, I successfully managed project budgeting and fiscal audits with high accountability. As an EU citizen, my Swiss B/L work authorization involves a streamlined, quota-free process.

Available starting \textbf{April 2027 for a duration of 4 to 5 months} (fully fulfilling the 16-week French CTI accreditation requirement), I would be delighted to discuss how my hands-on prototyping skills can contribute to \textbf{[Company Name]}'s engineering projects. Thank you for your time and consideration.

\vspace{14pt}
\noindent Sincerely,\\[18pt]
\textbf{Théodore Hesling}\\[2pt]
{\small MSc Engineering Student -- Mines Saint-Étienne (ISMIN)\\
theodore200531@outlook.com \quad +33 6 75 49 33 72}

\end{document}
"""

# Define all documents to generate
SUBTITLE_1 = "Engineering student seeking a 4-to-5-month internship in Embedded Systems \\& Hardware Security"
SUBTITLE_2 = "Engineering student seeking a 4-to-5-month internship in Cybersecurity, Networks \\& Infrastructure"
SUBTITLE_3 = "Engineering student seeking a 4-to-5-month internship in Embedded Systems, Robotics \\& Smart Sensors"

docs = [
    # Standard CVs (centered header without QR code)
    ("CV_1_Embedded_Hardware_Security_Theodore_Hesling.tex", PREAMBLE_CV + "\\begin{document}\n" + get_header(SUBTITLE_1, with_qr=False) + BODY_CV1 + "\n\\end{document}"),
    ("CV_2_Cybersecurity_Networks_Infra_Theodore_Hesling.tex", PREAMBLE_CV + "\\begin{document}\n" + get_header(SUBTITLE_2, with_qr=False) + BODY_CV2 + "\n\\end{document}"),
    ("CV_3_Embedded_Robotics_Sensors_Theodore_Hesling.tex", PREAMBLE_CV + "\\begin{document}\n" + get_header(SUBTITLE_3, with_qr=False) + BODY_CV3 + "\n\\end{document}"),
    
    # CVs WITH LINKEDIN QR CODE
    ("CV_1_Embedded_Hardware_Security_Theodore_Hesling_QRCode.tex", PREAMBLE_CV + "\\begin{document}\n" + get_header(SUBTITLE_1, with_qr=True) + BODY_CV1 + "\n\\end{document}"),
    ("CV_2_Cybersecurity_Networks_Infra_Theodore_Hesling_QRCode.tex", PREAMBLE_CV + "\\begin{document}\n" + get_header(SUBTITLE_2, with_qr=True) + BODY_CV2 + "\n\\end{document}"),
    ("CV_3_Embedded_Robotics_Sensors_Theodore_Hesling_QRCode.tex", PREAMBLE_CV + "\\begin{document}\n" + get_header(SUBTITLE_3, with_qr=True) + BODY_CV3 + "\n\\end{document}"),

    # Cover Letters
    ("Cover_Letter_1_Embedded_Hardware_Security.tex", COVER_LETTER_1_TEX),
    ("Cover_Letter_2_Cybersecurity_Infrastructure.tex", COVER_LETTER_2_TEX),
    ("Cover_Letter_3_Robotics_Embedded_Systems.tex", COVER_LETTER_3_TEX),
]

print("=== Compilation de tous les documents LaTeX ===")
for filename, content in docs:
    filepath = os.path.join(LATEX_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    # Compile with pdflatex
    res = subprocess.run(["pdflatex", "-interaction=nonstopmode", filename], cwd=LATEX_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pdf_filename = filename.replace(".tex", ".pdf")
    src_pdf = os.path.join(LATEX_DIR, pdf_filename)
    dst_pdf = os.path.join(PDF_DIR, pdf_filename)
    if os.path.exists(src_pdf):
        shutil.copy2(src_pdf, dst_pdf)
    
    # Check page count
    info_res = subprocess.run(["pdfinfo", dst_pdf], cwd=PDF_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    pages = [line for line in info_res.stdout.split("\n") if "Pages:" in line]
    page_str = pages[0] if pages else "Pages: Unknown"
    print(f"{filename:<60} -> {page_str} (Code: {res.returncode})")

# Clean temp files
for ext in [".aux", ".log", ".out", ".synctex.gz"]:
    for f in os.listdir(LATEX_DIR):
        if f.endswith(ext):
            try:
                os.remove(os.path.join(LATEX_DIR, f))
            except Exception:
                pass
print("=== Compilation terminée avec succès ! ===")
