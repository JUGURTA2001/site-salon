import os
import math
from PIL import Image, ImageDraw, ImageFont

def create_directories():
    for d in ["images", "site-salon/images"]:
        os.makedirs(d, exist_ok=True)

def get_font(size, bold=False):
    font_names = [
        "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\calibri.ttf",
        "C:\\Windows\\Fonts\\tahoma.ttf"
    ]
    if bold:
        font_names = [
            "C:\\Windows\\Fonts\\segoeuib.ttf",
            "C:\\Windows\\Fonts\\arialbd.ttf",
            "C:\\Windows\\Fonts\\calibrib.ttf"
        ] + font_names
    for f in font_names:
        if os.path.exists(f):
            try:
                return ImageFont.truetype(f, size)
            except Exception:
                continue
    return ImageFont.load_default()

def generate_logo():
    width, height = 500, 140
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    gold = (212, 175, 55, 255)
    light_gold = (245, 218, 122, 255)
    dark_gold = (166, 124, 0, 255)
    white = (245, 245, 245, 255)

    cx, cy = 60, 70
    r = 38
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=gold, width=2)
    draw.ellipse([cx - r + 4, cy - r + 4, cx + r - 4, cy + r - 4], outline=dark_gold, width=1)

    draw.line([cx - 16, cy + 20, cx + 18, cy - 20], fill=light_gold, width=3)
    draw.line([cx + 16, cy + 20, cx - 18, cy - 20], fill=light_gold, width=3)
    draw.ellipse([cx - 4, cy - 2, cx + 4, cy + 6], fill=gold)
    draw.ellipse([cx - 22, cy + 14, cx - 10, cy + 26], outline=gold, width=2)
    draw.ellipse([cx + 10, cy + 14, cx + 22, cy + 26], outline=gold, width=2)

    title_font = get_font(38, bold=True)
    draw.text((125, 28), "L'ÉLÉGANCE", font=title_font, fill=light_gold)
    
    draw.line([125, 78, 470, 78], fill=gold, width=2)
    draw.polygon([(290, 74), (297, 78), (290, 82), (283, 78)], fill=light_gold)

    sub_font = get_font(16, bold=True)
    draw.text((128, 88), "SALON DE COIFFURE • BÉJAÏA", font=sub_font, fill=white)

    img.save("images/logo.png", "PNG")
    img.save("site-salon/images/logo.png", "PNG")
    print("Logo généré avec succès.")

def generate_photo1():
    w, h = 800, 600
    img = Image.new("RGB", (w, h), (18, 20, 24))
    draw = ImageDraw.Draw(img)

    for y in range(h):
        for x in range(0, w, 4):
            dx = x - 400
            dy = y - 300
            dist = math.sqrt(dx*dx + dy*dy)
            factor = max(0, min(1, 1 - dist / 500))
            r = int(18 + factor * 45)
            g = int(20 + factor * 35)
            b = int(24 + factor * 20)
            draw.rectangle([x, y, x+4, y+1], fill=(r, g, b))

    draw.ellipse([220, 70, 580, 430], outline=(212, 175, 55), width=3)
    draw.ellipse([230, 80, 570, 420], outline=(70, 55, 20), width=1)

    draw.ellipse([250, 360, 550, 650], fill=(28, 30, 36), outline=(212, 175, 55), width=2)
    draw.ellipse([320, 150, 480, 380], fill=(38, 40, 48), outline=(212, 175, 55), width=2)

    hair_points = [
        (330, 220), (315, 170), (340, 110), (410, 85), 
        (470, 110), (490, 170), (470, 220), (455, 160), 
        (405, 140), (355, 160)
    ]
    draw.polygon(hair_points, fill=(212, 175, 55))

    beard_points = [
        (340, 280), (330, 330), (370, 395), (400, 410), 
        (430, 395), (470, 330), (460, 280), (430, 330), (370, 330)
    ]
    draw.polygon(beard_points, fill=(180, 140, 40))

    draw.line([60, 100, 60, 500], fill=(212, 175, 55), width=3)
    draw.line([740, 100, 740, 500], fill=(212, 175, 55), width=3)

    draw.rectangle([100, 480, 700, 570], fill=(15, 15, 18), outline=(212, 175, 55), width=2)
    title_font = get_font(26, bold=True)
    sub_font = get_font(15)
    draw.text((130, 495), "COUPE HOMME & DÉGRADÉ DE PRÉCISION", font=title_font, fill=(245, 218, 122))
    draw.text((130, 535), "Expertise coiffure, traçage de barbe & finitions soignées", font=sub_font, fill=(200, 200, 200))

    img.save("images/photo1.jpg", "JPEG", quality=92)
    img.save("site-salon/images/photo1.jpg", "JPEG", quality=92)
    print("Photo 1 générée.")

def generate_photo2():
    w, h = 800, 600
    img = Image.new("RGB", (w, h), (14, 15, 18))
    draw = ImageDraw.Draw(img)

    for i in range(12):
        x_start = int(w * i / 11)
        draw.line([x_start, 400, int(w/2 + (x_start - w/2)*2.2), 600], fill=(35, 30, 22), width=2)

    for x in range(30, 770, 25):
        draw.line([x, 50, x, 400], fill=(28, 24, 20), width=12)

    mirror_centers = [200, 400, 600]
    for mc in mirror_centers:
        draw.ellipse([mc - 85, 95, mc + 85, 265], fill=(45, 38, 20), outline=(230, 190, 80), width=4)
        draw.ellipse([mc - 75, 105, mc + 75, 255], fill=(22, 26, 32), outline=(100, 90, 60), width=2)
        draw.line([mc - 40, 130, mc + 20, 230], fill=(60, 70, 85), width=3)
        draw.line([mc - 25, 130, mc + 35, 230], fill=(60, 70, 85), width=1)

        draw.rounded_rectangle([mc - 45, 260, mc + 45, 340], radius=8, fill=(35, 35, 40), outline=(212, 175, 55), width=2)
        draw.rounded_rectangle([mc - 20, 235, mc + 20, 255], radius=4, fill=(45, 45, 50), outline=(212, 175, 55), width=1)
        draw.rounded_rectangle([mc - 50, 340, mc + 50, 380], radius=6, fill=(30, 30, 35), outline=(212, 175, 55), width=2)
        draw.rectangle([mc - 8, 380, mc + 8, 430], fill=(180, 180, 190))
        draw.ellipse([mc - 40, 420, mc + 40, 445], fill=(150, 150, 160), outline=(212, 175, 55), width=2)

    draw.rectangle([60, 370, 740, 385], fill=(20, 18, 15), outline=(212, 175, 55), width=2)

    draw.rectangle([100, 480, 700, 570], fill=(15, 15, 18), outline=(212, 175, 55), width=2)
    title_font = get_font(26, bold=True)
    sub_font = get_font(15)
    draw.text((130, 495), "INTÉRIEUR DU SALON • AMBIANCE FEUTRÉE", font=title_font, fill=(245, 218, 122))
    draw.text((130, 535), "Cadre prestigieux, fauteuils grand confort & hygiène irréprochable", font=sub_font, fill=(200, 200, 200))

    img.save("images/photo2.jpg", "JPEG", quality=92)
    img.save("site-salon/images/photo2.jpg", "JPEG", quality=92)
    print("Photo 2 générée.")

def generate_photo3():
    w, h = 800, 600
    img = Image.new("RGB", (w, h), (16, 16, 20))
    draw = ImageDraw.Draw(img)

    for i in range(40):
        t = i / 40.0
        r = int(140 + 100 * math.sin(t * 3.14))
        g = int(90 + 95 * math.sin(t * 3.14))
        b = int(35 + 40 * math.sin(t * 3.14))
        
        offset = i * 14
        points = []
        for y in range(40, 460, 20):
            x = int(380 + 120 * math.sin((y + offset * 2) * 0.015) + (i - 20) * 12)
            points.append((x, y))
        
        for k in range(len(points) - 1):
            draw.line([points[k], points[k+1]], fill=(r, g, b), width=4)

    draw.ellipse([100, 240, 220, 320], outline=(212, 175, 55), width=3, fill=(25, 25, 30))
    draw.ellipse([115, 255, 205, 305], fill=(190, 140, 50))
    draw.line([160, 220, 230, 140], fill=(212, 175, 55), width=6)
    draw.polygon([(150, 225), (170, 215), (155, 245), (145, 235)], fill=(245, 218, 122))

    draw.rectangle([100, 480, 700, 570], fill=(15, 15, 18), outline=(212, 175, 55), width=2)
    title_font = get_font(26, bold=True)
    sub_font = get_font(15)
    draw.text((130, 495), "COLORATION, BALAYAGE & SOINS PROFONDS", font=title_font, fill=(245, 218, 122))
    draw.text((130, 535), "Nuances éclatantes, pigments de haute qualité & brillance miroir", font=sub_font, fill=(200, 200, 200))

    img.save("images/photo3.jpg", "JPEG", quality=92)
    img.save("site-salon/images/photo3.jpg", "JPEG", quality=92)
    print("Photo 3 générée.")

if __name__ == "__main__":
    create_directories()
    generate_logo()
    generate_photo1()
    generate_photo2()
    generate_photo3()
    print("Tous les assets ont été générés avec succès.")
