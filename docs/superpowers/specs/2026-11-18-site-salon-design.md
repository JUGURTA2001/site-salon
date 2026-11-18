# Spécification de Conception : Site Vitrine Salon L'Élégance Béjaïa

## 1. Contexte & Objectifs
Création d'un site vitrine moderne d'une seule page (One-Page) en HTML5 et CSS3 pur (sans framework externe, sans dépendance lourde) pour le **Salon L'Élégance**, situé à Béjaïa Ville (Algérie).

Le site vise à :
- Présenter les services de coiffure et barbiers avec tarifs clairs en Dinars Algériens (DA).
- Offrir une prise de rendez-vous et un contact instantanés via WhatsApp et appel téléphonique direct.
- Valoriser le travail du salon via une galerie photo soignée.
- Faciliter l'accès physique grâce aux horaires et à une carte Google Maps intégrée.
- Assurer un référencement local optimal (SEO) sur "coiffeur Béjaïa", "salon de coiffure Béjaïa ville".

## 2. Arborescence du Projet
Le projet sera structuré ainsi :
```text
site-salon/
├── index.html
├── style.css
└── images/
    ├── logo.png       (Logo doré sur fond transparent/sombre)
    ├── photo1.jpg     (Coupe homme moderne)
    ├── photo2.jpg     (Intérieur chaleureux et raffiné du salon)
    └── photo3.jpg     (Coloration & coiffage professionnel)
```
*(Une copie à la racine de l'espace de travail sera également présente pour faciliter l'accès direct et la publication GitHub Pages depuis la racine).*

## 3. Architecture des Composants & Contenu

### 3.1 Balisage SEO & En-tête HTML
- `<!DOCTYPE html>` avec attribut `<html lang="fr">`.
- `<meta charset="UTF-8">` et `<meta name="viewport" content="width=device-width, initial-scale=1.0">`.
- Balises SEO :
  - Title : `Salon L'Élégance | Coiffeur & Barbier à Béjaïa Ville`
  - Meta Description : `Salon de coiffure et barbier haut de gamme à Béjaïa Ville. Coupe homme, taille de barbe, coloration et soins capillaires. Rendez-vous direct au 0550 00 00 00.`
  - Meta Keywords : `coiffeur Béjaïa, salon coiffure Béjaïa ville, barbier Béjaïa, coupe homme Béjaïa, coloration Béjaïa`
  - OpenGraph tags (title, description, image, type).

### 3.2 Navigation & En-tête (`<header>`)
- Logo cliquable : `<img src="images/logo.png" alt="Logo Salon L'Élégance Béjaïa" class="logo">`.
- Barre de navigation responsive avec liens d'ancrage doux :
  - Accueil (`#accueil`)
  - Services & Tarifs (`#services`)
  - Galerie (`#galerie`)
  - Contact & Accès (`#contact`)
- Bouton d'action rapide dans le menu pour réserver sur WhatsApp.
- Menu burger accessible pour écrans mobiles.

### 3.3 Section Accueil / Hero (`<section id="accueil">`)
- Slogan percutant : *"L'Excellence & Le Style au Cœur de Béjaïa"*.
- Sous-titre : *"Votre salon de coiffure & barbier de référence à Béjaïa Ville. Une expertise sur-mesure pour sublimer votre look."*
- Boutons d'action :
  - CTA principal WhatsApp : lien vers `https://wa.me/213550000000?text=Bonjour%2C%20je%20souhaite%20prendre%20un%20rendez-vous%20au%20Salon%20L'Élégance%20Béjaïa`
  - CTA secondaire : Découvrir nos services (`#services`).

### 3.4 Section Services (`<section id="services">`)
4 cartes interactives avec icônes / badges, description et prix :
1. **Coupe & Coiffage Homme** — Shampoing traitant, coupe sur-mesure, dégradé de précision & coiffage : `1 200 DA`
2. **Taille de Barbe & Serviette Chaude** — Traçage soigné, rasage traditionnel, serviette chaude & huile nourrissante : `800 DA`
3. **Coloration & Décoloration** — Teinture barbe/cheveux, mèches et patine sur-mesure : `3 500 DA`
4. **Soin Capillaire Profond & Kératine** — Soin réparateur revitalisant, botox capillaire & massage du cuir chevelu : `2 500 DA`

### 3.5 Galerie Photos (`<section id="galerie">`)
Grille responsive élégante avec zoom progressif :
- `photo1.jpg` : `alt="Coupe homme moderne dégradé soigné"` avec `loading="lazy"`
- `photo2.jpg` : `alt="Intérieur du salon de coiffure à Béjaïa"` avec `loading="lazy"`
- `photo3.jpg` : `alt="Coloration et coiffage professionnel"` avec `loading="lazy"`

### 3.6 Contact, Horaires & Google Maps (`<section id="contact">`)
- Coordonnées :
  - Adresse : *Boulevard de la Liberté, Béjaïa Ville (06000), Algérie*
  - Téléphone : `+213 (0) 550 00 00 00`
  - WhatsApp : `+213 550 00 00 00`
- Horaires d'ouverture :
  - Samedi – Jeudi : `09h00 – 20h30`
  - Vendredi : `14h30 – 21h00`
- Carte interactive Google Maps intégrée via un iframe sécurisé, responsive et centré sur Béjaïa Ville.

### 3.7 Boutons Flottants d'Action Rapide (Sticky CTA)
En bas de l'écran (particulièrement adapté sur mobile) :
- Bouton Appel : lien `tel:0550000000` avec icône téléphone.
- Bouton WhatsApp : lien `https://wa.me/213550000000` avec icône WhatsApp et badge "En ligne".

### 3.8 Pied de Page (`<footer>`)
- Liens vers les réseaux sociaux : Facebook et Instagram du salon.
- Mentions légales simplifiées et copyright `© 2026 Salon L'Élégance Béjaïa - Tous droits réservés`.

## 4. Charte Graphique & Design CSS
- **Typographie** : Police système moderne et fluide (`system-ui`, `-apple-system`, `Segoe UI`, `Roboto`, sans-serif) avec police d'accent élégante pour les titres.
- **Palette de couleurs** :
  - Primaire (Noir profond de fond) : `#121212` / `#1a1a1a`
  - Secondaire (Carte & surfaces) : `#222222`
  - Accent Doré brossé (Logo & détails) : `#D4AF37` / `#E5C158`
  - Texte principal : `#F5F5F5`
  - Texte atténué : `#A0A0A0`
  - Couleur WhatsApp : `#25D366`
- **Responsive & Mobile First** :
  - Media queries adaptées (`@media (min-width: 768px)` et `@media (min-width: 1024px)`).
  - Flexbox et CSS Grid pour un alignement fluide.
  - Boutons tactiles généreux (minimum 44px de hauteur).

## 5. Assets Graphiques Réels
- Génération programmatique de haute qualité pour les 4 images :
  - `logo.png` : PNG haute résolution avec emblème doré de coiffeur/barbier et typographie dorée.
  - `photo1.jpg` : Visuel réaliste et esthétique illustrant la coupe homme.
  - `photo2.jpg` : Visuel réaliste illustrant l'intérieur contemporain du salon.
  - `photo3.jpg` : Visuel réaliste illustrant une coloration/coiffure réussie.

## 6. Guide de Test et Déploiement GitHub Pages
Documentation détaillée fournie à la fin :
- Comment ouvrir et tester en local (dans n'importe quel navigateur).
- Comment créer un dépôt GitHub, y déposer les fichiers et activer GitHub Pages en 3 clics.
