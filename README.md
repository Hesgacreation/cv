# Dossier de Candidature Stage Suisse (ISMIN - 2A)
**Théodore Hesling — Mines Saint-Étienne (Campus Georges Charpak Provence)**

---

## 🎯 Objectif & Contexte Stratégique
* **Période cible :** Avril 2027 à Août/Septembre 2027 (durée de **4 à 5 mois**).
* **Quitus CTI :** Validation stricte de la mobilité internationale (**minimum 16 semaines consécutives**).
* **Zone prioritaire :** **Suisse romande** (Cantons de Genève, Vaud, Neuchâtel, Fribourg, Valais) pour établir un premier ancrage helvétique en prévision du stage de fin d'études (PFE / 3A) et d'un futur CDI.
* **Statut de travail :** Citoyen français / UE — dispense de visa, procédure accélérée de permis de travail frontalier (G) ou de séjour (L/B) sans blocage de contingent.

---

## 📁 Organisation du Répertoire

```text
/home/theodoreh/Documents/2A/cv/
│
├── README.md                           <- Guide complet du répertoire et synthèse
├── entreprises_suisse_ismin.md          <- Base prospective des 20 entreprises suisses cibles & kits associés
│
├── pdf/                                <- PDF FINAUX PRÊTS À L'ENVOI (1 page A4 chacun)
│   ├── [Versions Modernes avec QR Code LinkedIn en haut à droite]
│   │   ├── CV_1_Embedded_Hardware_Security_Theodore_Hesling_QRCode.pdf
│   │   ├── CV_2_Cybersecurity_Networks_Infra_Theodore_Hesling_QRCode.pdf
│   │   └── CV_3_Embedded_Robotics_Sensors_Theodore_Hesling_QRCode.pdf
│   ├── [Versions Classiques épurées sans QR Code]
│   │   ├── CV_1_Embedded_Hardware_Security_Theodore_Hesling.pdf
│   │   ├── CV_2_Cybersecurity_Networks_Infra_Theodore_Hesling.pdf
│   │   └── CV_3_Embedded_Robotics_Sensors_Theodore_Hesling.pdf
│   ├── [Lettres de Motivation Assorties]
│   │   ├── Cover_Letter_1_Embedded_Hardware_Security.pdf
│   │   ├── Cover_Letter_2_Cybersecurity_Infrastructure.pdf
│   │   └── Cover_Letter_3_Robotics_Embedded_Systems.pdf
│   └── QR_Codes_Theodore_Hesling_Sheet.pdf  <- Fiche récapitulative 4 QR codes à imprimer / garder sur smartphone
│
├── qrcodes/                            <- IMAGES DES QR CODES & FICHE IMPRIMABLE
│   ├── qrcode_linkedin.png (.svg)      <- QR code profil LinkedIn
│   ├── qrcode_cv1_embedded_security.png (.svg)
│   ├── qrcode_cv2_cybersecurity_infra.png (.svg)
│   ├── qrcode_cv3_robotics_sensors.png (.svg)
│   └── QR_Codes_Theodore_Hesling_Sheet.pdf (et .tex)
│
├── latex/                              <- SOURCES LATEX (Éditables dans TeXstudio)
│   ├── compile.sh                      <- Script bash pour tout recompiler et exporter dans pdf/ en 3s
│   ├── CV_*_QRCode.tex                 <- Sources des CV avec QR Code LinkedIn
│   ├── CV_*.tex                        <- Sources des CV classiques
│   └── Cover_Letter_*.tex              <- Sources des lettres de motivation
│
├── libreoffice/                        <- LETTRES ÉDITABLES (.odt) POUR LIBREOFFICE WRITER
│   ├── Cover_Letter_1_Embedded_Hardware_Security.odt
│   ├── Cover_Letter_2_Cybersecurity_Infrastructure.odt
│   └── Cover_Letter_3_Robotics_Embedded_Systems.odt
│
├── markdown/                           <- SOURCES TEXTUELLES BRUTES & APERÇUS WEB
│   ├── CV_*.md (et .html)
│   └── Cover_Letter_*.md (et .html)
│
├── original/                           <- CV DE RÉFÉRENCE ESTHÉTIQUE INITIAL
│   └── THEODORE_HESLING_FlowCV_Resume_2026-03-30.pdf
│
└── scripts/                            <- SCRIPTS PYTHON D'AUTOMATISATION & EXPORT
    ├── generate_latex_docs.py          <- Moteur de génération & compilation des 6 CV + 3 lettres
    ├── generate_qrcodes.py             <- Générateur des QR codes (PNG/SVG) et de la fiche récapitulative
    └── build_documents.py              <- Générateur Markdown -> HTML/ODT
```

---

## 🧭 Les 3 Kits de Candidature Spécialisés

Chaque kit associe un **CV sur-mesure (1 page A4)** et une **Lettre de motivation executive assortie (1 page A4)** reproduisant fidèlement la typographie et la mise en page de votre CV d'origine FlowCV (police *Bitstream Charter*, icônes vectorielles *TikZ*, séparateurs nets).

| Kit | Domaine & Cible | Entreprises Suisses Clés | Documents associés |
| :--- | :--- | :--- | :--- |
| **Kit 1** | **Systèmes Embarqués & Sécurité Matérielle**<br>*(Hardware Security, Firmware bas-niveau STM32/ARM, Cryptographie AES/ECC, Secure Boot)* | Kudelski Group, STMicroelectronics Genève, SICPA, Nagra DTV | • `pdf/CV_1_..._QRCode.pdf` (ou classique)<br>• `pdf/Cover_Letter_1_...pdf`<br>• Sources dans `latex/` |
| **Kit 2** | **Cybersécurité, Réseaux & Infrastructure**<br>*(Sécurité applicative & réseau, OpenSSL, Durcissement Linux, Détection d'intrusion, Confidentialité)* | Proton, ELCA / Senthorus, Kudelski Security, Swisscom, SCRT | • `pdf/CV_2_..._QRCode.pdf` (ou classique)<br>• `pdf/Cover_Letter_2_...pdf`<br>• Sources dans `latex/` |
| **Kit 3** | **Robotique, Capteurs & Systèmes Autonomes**<br>*(Firmware bare-metal C, capteurs capacitifs différentiels maison, régulation PID temps réel, CAO Inventor)* | Logitech, SenseFly (AgEagle), LEM, Sonceboz, Bobst, CSEM | • `pdf/CV_3_..._QRCode.pdf` (ou classique)<br>• `pdf/Cover_Letter_3_...pdf`<br>• Sources dans `latex/` |

---

## 📱 Utilisation des QR Codes

1. **Sur le CV (En-tête haut droit) :**
   Les fichiers `CV_*_QRCode.pdf` intègrent un QR code vectoriel natif de 18 mm pointant directement vers votre profil LinkedIn :
   `https://www.linkedin.com/in/théodore-hesling-a08316386`
   Le QR code est scannable instantanément par n'importe quel smartphone, et reste cliquable directement si le recruteur consulte le PDF sur écran.

2. **Fiche Récapitulative Imprimable (`pdf/QR_Codes_Theodore_Hesling_Sheet.pdf`) :**
   Idéale pour les forums d'entreprises, salons de recrutement ou à garder sur votre téléphone pour faire scanner vos CV à la volée. Elle regroupe sur 1 page les 4 QR codes (LinkedIn, CV 1, CV 2, CV 3).

3. **Mise à jour des liens des QR codes :**
   Lorsque vous aurez hébergé vos PDF en ligne (ex. Google Drive public, OneDrive ou dépôt GitHub), vous pouvez régénérer les images et la fiche en une seule commande :
   ```bash
   python3 scripts/generate_qrcodes.py --cv1 "VOTRE_LIEN_CV1" --cv2 "VOTRE_LIEN_CV2" --cv3 "VOTRE_LIEN_CV3"
   ```

---

## 🌐 Hébergement En Ligne & GitHub Pages

Le dossier de candidature dispose d'un site web vitrine responsive (`index.html`) et de liens directs pour les recruteurs :

* **Site vitrine :** [https://hesgacreation.github.io/cv/](https://hesgacreation.github.io/cv/)
* **CV 1 (Embarqué & Sécurité) :** [https://hesgacreation.github.io/cv/cv1.pdf](https://hesgacreation.github.io/cv/cv1.pdf)
* **CV 2 (Cyber & Infrastructure) :** [https://hesgacreation.github.io/cv/cv2.pdf](https://hesgacreation.github.io/cv/cv2.pdf)
* **CV 3 (Robotique & Capteurs) :** [https://hesgacreation.github.io/cv/cv3.pdf](https://hesgacreation.github.io/cv/cv3.pdf)
* **Fiche QR Codes complète :** [https://hesgacreation.github.io/cv/qrcodes.pdf](https://hesgacreation.github.io/cv/qrcodes.pdf)

### Déploiement sur GitHub :
```bash
git remote add origin https://github.com/Hesgacreation/cv.git
git branch -M main
git push -u origin main
```
Puis dans GitHub : **Settings > Pages > Branch: `main` / `root` > Save**.

---

## 🛠️ Comment recompiler et modifier les documents ?

* **Dans TeXstudio :** Ouvrez n'importe quel fichier `.tex` dans `latex/` et appuyez sur **F5** (Compiler).
* **En terminal :** Lancez `./latex/compile.sh` pour recompiler tous les CV et lettres d'un seul coup.
* **Génération des QR codes :** Lancez `python3 scripts/generate_qrcodes.py`.
