# 💈 Salon L'Élégance — Site Vitrine One-Page

Site vitrine moderne, épuré et ultra-rapide (HTML5 & CSS3 pur, sans framework) conçu pour un salon de coiffure et barbier haut de gamme situé à **Béjaïa Ville** (Algérie).

---

## 📁 Arborescence du Projet

Le dossier est prêt à l'emploi et structuré comme suit :

```text
Site Web/
├── index.html                 # Page d'accueil principale (racine)
├── style.css                  # Feuille de styles CSS3 moderne
├── images/
│   ├── logo.png               # Logo du salon (doré sur fond transparent)
│   ├── photo1.jpg             # Photo Galerie : Coupe homme & dégradé
│   ├── photo2.jpg             # Photo Galerie : Intérieur du salon
│   └── photo3.jpg             # Photo Galerie : Coloration & coiffage
│
├── site-salon/                # Dossier dédié autonome
│   ├── index.html
│   ├── style.css
│   └── images/
│       ├── logo.png
│       ├── photo1.jpg
│       ├── photo2.jpg
│       └── photo3.jpg
│
└── README.md                  # Guide de démarrage et de déploiement
```

---

## 🌟 Contenu & Fonctionnalités Intégrées

1. **En-tête Sticky Glassmorphism** : Logo, liens fluides (*Accueil, Services, Galerie, Contact*) et bouton de réservation direct. Menu responsive (burger) sur mobile.
2. **Section Accueil (Hero)** : Phrase d'accroche valorisante et bouton d'action direct vers WhatsApp (`+213 550 00 00 00`).
3. **Section Services (4 cartes)** :
   - *Coupe & Coiffage Homme* (1 200 DA)
   - *Taille de Barbe & Soin serviette chaude* (800 DA)
   - *Coloration & Décoloration tendance* (3 500 DA)
   - *Soin Capillaire & Kératine* (2 500 DA)
4. **Galerie (3 photos)** : Grille responsive avec effet de zoom au survol, balises `alt` et attribut `loading="lazy"` pour des performances optimales.
5. **Horaires & Adresse avec Google Maps** :
   - Horaires détaillés (Samedi–Jeudi 09h-20h30 / Vendredi 14h30-21h).
   - Adresse au centre de Béjaïa Ville (Boulevard de la Liberté, proche Place Gueydon).
   - Carte Google Maps intégrée en iframe 100% responsive.
6. **Boutons Flottants Fixes** :
   - Bouton **Appeler** : lien direct `tel:0550000000`.
   - Bouton **WhatsApp** : ouverture immédiate d'une discussion pré-remplie avec le `0550 00 00 00`.
7. **Pied de page (Footer)** : Liens sociaux vers Facebook et Instagram, copyright et mentions légales.
8. **Optimisation SEO** : Balises `<title>`, `<meta description>`, balises OpenGraph et mots-clés ciblés (*coiffeur Béjaïa, salon coiffure Béjaïa ville, barbier, etc.*).

---

## 💻 1. Comment Tester le Site en Local

Vous avez trois méthodes très simples pour tester le site sur votre ordinateur :

### Méthode A : Double-clic direct (Le plus rapide)
1. Ouvrez le dossier `c:\Users\touat\Desktop\Site Web` dans l'explorateur Windows.
2. Double-cliquez simplement sur le fichier **`index.html`** (ou dans `site-salon/index.html`).
3. Votre navigateur par défaut (Chrome, Edge, Firefox) s'ouvrira immédiatement avec le site complet.

### Méthode B : Avec un serveur local Python
Ouvrez PowerShell dans le dossier et tapez :
```bash
python -m http.server 8000
```
Puis ouvrez votre navigateur à l'adresse : **`http://localhost:8000`**

### Méthode C : Avec l'extension VS Code (Live Server)
1. Ouvrez le dossier dans Visual Studio Code.
2. Installez l'extension **Live Server**.
3. Faites un clic droit sur `index.html` puis sélectionnez **"Open with Live Server"**.

---

## 🚀 2. Comment Publier Gratuitement sur GitHub Pages

GitHub Pages vous permet d'héberger ce site gratuitement avec une adresse sécurisée en `https://` (ex: `https://votre-pseudo.github.io/salon-elegance/`).

### Étape 1 : Créer un compte et un dépôt sur GitHub
1. Rendez-vous sur [github.com](https://github.com) et connectez-vous (ou créez un compte gratuit).
2. Cliquez sur le bouton **"+"** en haut à droite > **"New repository"**.
3. Donnez un nom à votre dépôt (par exemple : `salon-elegance` ou `site-salon`).
4. Laissez le dépôt en **Public** et ne cochez pas l'option "Add a README file" (car nous en avons déjà un).
5. Cliquez sur **"Create repository"**.

### Étape 2 : Envoyer vos fichiers vers GitHub
Dans votre terminal PowerShell ouvert dans le dossier `Site Web` :

```bash
# 1. Associer votre dépôt GitHub (remplacez par votre lien GitHub)
git remote add origin https://github.com/VOTRE_PSEUDO/salon-elegance.git

# 2. Renommer la branche principale en main
git branch -M main

# 3. Pousser vos fichiers vers GitHub
git push -u origin main
```
*(Si vous préférez ne pas utiliser la ligne de commande, vous pouvez aussi simplement glisser-déposer vos fichiers directement sur la page de votre dépôt GitHub).*

### Étape 3 : Activer GitHub Pages (en 3 clics)
1. Sur la page de votre dépôt GitHub, cliquez sur l'onglet **Settings** (Paramètres).
2. Dans le menu de gauche, cliquez sur la section **Pages**.
3. Dans la partie **"Build and deployment"** :
   - Source : sélectionnez **"Deploy from a branch"**.
   - Branch : sélectionnez **`main`** et laissez le dossier sur **`/(root)`**.
4. Cliquez sur **Save**.

🎉 **C'est tout !** En 1 à 2 minutes, GitHub Pages affichera en haut un encadré vert avec l'adresse publique de votre site :
👉 `https://VOTRE_PSEUDO.github.io/salon-elegance/`

---

## ✏️ Comment Personnaliser Votre Site

- **Modifier les tarifs ou services** : Ouvrez `index.html` et modifiez les textes dans la section `<section id="services">`.
- **Changer le numéro de téléphone** : Remplacez `0550000000` et `213550000000` par votre propre numéro dans `index.html`.
- **Remplacer les photos** : Déposez vos propres photos dans le dossier `images/` en conservant les mêmes noms (`photo1.jpg`, `photo2.jpg`, `photo3.jpg`, `logo.png`).
