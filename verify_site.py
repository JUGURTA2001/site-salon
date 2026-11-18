import os
import re

def test_all():
    errors = []

    # 1. Vérification des fichiers requis
    required_files = [
        "index.html",
        "style.css",
        "images/logo.png",
        "images/photo1.jpg",
        "images/photo2.jpg",
        "images/photo3.jpg",
        "site-salon/index.html",
        "site-salon/style.css",
        "site-salon/images/logo.png",
        "site-salon/images/photo1.jpg",
        "site-salon/images/photo2.jpg",
        "site-salon/images/photo3.jpg"
    ]
    for rf in required_files:
        if not os.path.exists(rf):
            errors.append(f"Fichier manquant : {rf}")
        elif os.path.getsize(rf) == 0:
            errors.append(f"Fichier vide : {rf}")

    # 2. Vérification du contenu HTML
    with open("site-salon/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Balises SEO
    if "<title>" not in html or "</title>" not in html:
        errors.append("Balise <title> manquante")
    if 'meta name="description"' not in html:
        errors.append("Meta description manquante")
    if 'meta name="keywords"' not in html:
        errors.append("Meta keywords manquants")
    if 'lang="fr"' not in html:
        errors.append("Attribut lang='fr' manquant")

    # En-tête avec logo et menu
    if 'src="images/logo.png"' not in html:
        errors.append("Logo 'images/logo.png' manquant")
    for menu in ["Accueil", "Services", "Galerie", "Contact"]:
        if menu not in html:
            errors.append(f"Élément du menu manquant : {menu}")

    # WhatsApp et numéro
    if "0550 00 00 00" not in html and "0550000000" not in html:
        errors.append("Numéro 0550 00 00 00 manquant")
    if "wa.me/213550000000" not in html:
        errors.append("Lien WhatsApp wa.me/213550000000 manquant")
    if "tel:0550000000" not in html:
        errors.append("Lien d'appel tel:0550000000 manquant")

    # 4 Cartes de services
    service_cards = len(re.findall(r'class="[^"]*service-card[^"]*"', html))
    if service_cards < 4:
        errors.append(f"Nombre de cartes de services insuffisant : {service_cards} (attendu >= 4)")

    # Galerie des 3 photos
    for photo in ["photo1.jpg", "photo2.jpg", "photo3.jpg"]:
        if f'images/{photo}' not in html:
            errors.append(f"Image {photo} manquante dans le HTML")
    
    # Attributs alt et loading="lazy"
    img_tags = re.findall(r'<img[^>]+>', html)
    for tag in img_tags:
        if 'alt=' not in tag:
            errors.append(f"Attribut alt manquant dans : {tag}")
        if 'photo' in tag and 'loading="lazy"' not in tag:
            errors.append(f"Attribut loading='lazy' manquant dans : {tag}")

    # Google Maps iframe
    if "<iframe" not in html or "maps.google.com" not in html:
        errors.append("Carte Google Maps iframe manquante")

    # Horaires et adresse
    if "Horaires" not in html or "Boulevard de la Liberté" not in html:
        errors.append("Horaires ou adresse manquants")

    # Boutons flottants
    if "floating-btn" not in html or "floating-buttons" not in html:
        errors.append("Boutons flottants manquants")

    # Liens Facebook et Instagram
    if "facebook.com" not in html:
        errors.append("Lien Facebook manquant dans le footer")
    if "instagram.com" not in html:
        errors.append("Lien Instagram manquant dans le footer")

    # 3. Vérification du CSS
    with open("site-salon/style.css", "r", encoding="utf-8") as f:
        css = f.read()

    if "@media" not in css:
        errors.append("Media queries CSS manquantes pour le responsive")
    if "position: fixed" not in css and "position:fixed" not in css:
        errors.append("Position fixed manquante pour les boutons flottants")

    if errors:
        print(f"❌ ÉCHEC : {len(errors)} erreur(s) détectée(s) :")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("✅ SUCCÈS : Tous les critères et exigences sont validés à 100% !")
        return True

if __name__ == "__main__":
    success = test_all()
    exit(0 if success else 1)
