# Salon L'Élégance Béjaïa Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Créer un site vitrine d'une seule page en HTML5 et CSS3 pur pour un salon de coiffure de référence à Béjaïa Ville avec toutes les ressources graphiques (logo et 3 photos), les 7 sections requises, le SEO local et les boutons d'action flottants.

**Architecture:** Architecture statique pure (zéro framework, zéro dépendance externe lourde). Séparation propre en deux fichiers `index.html` et `style.css` avec dossier `images/` contenant le logo et les photos. Architecture mobile-first avec CSS Grid et Flexbox, accessibilité et optimisation SEO.

**Tech Stack:** HTML5 sémantique, CSS3 (variables, Flexbox, Grid, Media Queries), Python Pillow / scripts SVG pour génération d'images haute qualité.

**Spec:** `docs/superpowers/specs/2026-11-18-site-salon-design.md`

## Global Constraints

- Pas de framework JavaScript ou CSS (ni Bootstrap, ni Tailwind, ni React).
- Fichiers séparés : `index.html` et `style.css`.
- Structure de dossier : `site-salon/` avec `images/` (`logo.png`, `photo1.jpg`, `photo2.jpg`, `photo3.jpg`), ainsi qu'une réplication à la racine pour tester directement.
- Respecter le numéro de téléphone et WhatsApp : `0550 00 00 00` (format international `+213 550 00 00 00`).
- Textes intégralement en français, géolocalisés à Béjaïa Ville.
- Images avec attributs `alt` précis et `loading="lazy"`.
- Balises SEO complètes (title, meta description, meta keywords ciblant "coiffeur Béjaïa").

---

### Task 1: Génération et vérification des assets graphiques (Logo et Photos)

**Files:**
- Create: `site-salon/images/logo.png`
- Create: `site-salon/images/photo1.jpg`
- Create: `site-salon/images/photo2.jpg`
- Create: `site-salon/images/photo3.jpg`
- Test: Script de vérification de l'existence et des dimensions des images

**Interfaces:**
- Produces: Images prêtes à être chargées par le navigateur dans `site-salon/images/` et `images/`.

- [ ] **Step 1: Créer le script Python de génération des assets graphiques**
Écrire un script Python utilisant Pillow pour générer :
1. `logo.png` : Fond transparent, typographie dorée stylisée "L'Élégance" avec ciseaux et peigne en or brossé (#D4AF37).
2. `photo1.jpg` : Visuel 800x600 illustrant une coupe homme moderne avec dégradé soigné.
3. `photo2.jpg` : Visuel 800x600 illustrant l'intérieur haut de gamme du salon (fauteuils barbier, miroirs rétroéclairés).
4. `photo3.jpg` : Visuel 800x600 illustrant une coloration et coiffage professionnel.

- [ ] **Step 2: Exécuter le script de génération**
Exécuter le script et vérifier la présence des 4 fichiers dans `site-salon/images/` et `images/`.

- [ ] **Step 3: Vérifier l'intégrité et les dimensions des images**
Valider que chaque image est non vide et aux dimensions attendues.

- [ ] **Step 4: Commit**
`git add site-salon/images/ images/ && git commit -m "feat(assets): ajouter le logo et les 3 photos du salon"`

---

### Task 2: Intégration du balisage HTML5 sémantique (`index.html`)

**Files:**
- Create: `site-salon/index.html`
- Create: `index.html` (miroir à la racine)
- Test: Validation de la structure HTML et des attributs requis

**Interfaces:**
- Consumes: Assets graphiques de la Task 1.
- Produces: Structure DOM complète avec 7 sections, SEO, boutons flottants et formulaires d'action.

- [ ] **Step 1: Rédiger le code complet de `index.html`**
Inclure :
- Balises SEO (title, meta description, keywords coiffeur Béjaïa, Open Graph).
- Header avec logo et navigation (Accueil, Services, Galerie, Contact).
- Hero section avec phrase d'accroche et CTA WhatsApp direct.
- Section Services avec 4 cartes (titre, description détaillée, prix en DA).
- Section Galerie avec les 3 photos, attributs `alt` pertinents et `loading="lazy"`.
- Section Contact avec horaires, adresse à Béjaïa Ville et iframe Google Maps responsive.
- Boutons flottants "Appeler" (`tel:0550000000`) et "WhatsApp" (`https://wa.me/213550000000`).
- Footer avec mentions légales, réseaux sociaux (Facebook, Instagram) et copyright.

- [ ] **Step 2: Vérifier la présence de tous les sélecteurs, ID et balises exigés**
Vérifier l'absence de liens morts et la présence exacte des 7 composants.

- [ ] **Step 3: Commit**
`git add site-salon/index.html index.html && git commit -m "feat(html): ajouter la structure HTML5 complète et sémantique"`

---

### Task 3: Conception et stylisation CSS3 responsive (`style.css`)

**Files:**
- Create: `site-salon/style.css`
- Create: `style.css` (miroir à la racine)
- Test: Vérification de la cohérence visuelle, variables CSS, breakpoints responsive

**Interfaces:**
- Consumes: Structure DOM de `index.html`.
- Produces: Rendu graphique moderne, mobile first, palette Noir & Or, boutons flottants interactifs.

- [ ] **Step 1: Rédiger le fichier `style.css` complet**
Inclure :
- Reset moderne et variables CSS (`--bg-color`, `--card-bg`, `--gold-primary`, `--gold-hover`, `--text-main`, `--text-muted`, `--whatsapp-color`).
- Typographie soignée, smooth scroll (`scroll-behavior: smooth`).
- Styles du Header sticky avec effet glassmorphism (fond semi-transparent flouté).
- Styles Hero avec typographie percutante et boutons animés.
- Grille CSS pour les 4 cartes Services avec effets d'élévation au survol.
- Grille CSS pour la Galerie avec effet de zoom au survol (`scale(1.05)`).
- Styles de la section Contact et iframe Google Maps responsive (arrondis, bordures dorées subtiles).
- Boutons flottants fixés en bas d'écran avec animations de pulsation subtiles et disposition ergonomique sur mobile.
- Media queries pour adaptation parfaite smartphone (< 768px), tablette et desktop.

- [ ] **Step 2: Vérifier la syntaxe CSS et le responsive**
Vérifier qu'aucune règle n'est tronquée ou invalide.

- [ ] **Step 3: Commit**
`git add site-salon/style.css style.css && git commit -m "feat(css): ajouter les styles CSS3 complets et le responsive design"`

---

### Task 4: Tests de validation, rendu et contrôle qualité

**Files:**
- Test: Script de vérification automatisé de conformité (W3C checklist, balises SEO, attributs images, liens)

- [ ] **Step 1: Exécuter les tests automatisés de conformité**
Vérifier :
- Attributs `alt` présents sur toutes les balises `<img>`.
- Attributs `loading="lazy"` présents sur la galerie.
- Liens WhatsApp pointant vers le numéro `0550 00 00 00` (`213550000000`).
- Liens téléphoniques pointant vers `tel:0550000000`.
- Meta description et balise title valides.
- Validité des fichiers et chargement sans erreur.

- [ ] **Step 2: Commit des résultats de validation**
`git commit --allow-empty -m "test: valider la conformité SEO, accessibilité et responsive"`

---

### Task 5: Rédaction du guide de test local et de déploiement GitHub Pages

**Files:**
- Create: `README.md`
- Test: Vérification de la clarté et complétude des instructions

- [ ] **Step 1: Rédiger le guide détaillé dans `README.md`**
Expliquer pas à pas :
1. Comment tester le site en local (double-clic sur `index.html`, ou avec extension Live Server dans VS Code, ou avec `python -m http.server 8000`).
2. Comment publier le site gratuitement sur GitHub Pages en quelques étapes simples (création du dépôt, push git, activation dans Settings > Pages).
3. Comment personnaliser les informations (textes, prix, horaires, photos).

- [ ] **Step 2: Commit**
`git add README.md && git commit -m "docs: ajouter le guide de test local et de publication GitHub Pages"`
