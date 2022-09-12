import img2pdf
import os
from PIL import Image, ImageDraw, ImageFont

def generate_image(start=int(input()), stop=int(input())+1):
    for i in range(start, stop):
        image = Image.new('RGB', (843, 596), (255, 255, 255, 0))
        font = ImageFont.truetype("impact.ttf", 390)
        draw = ImageDraw.Draw(image)
        draw.text((843/2, 596/2), str(i), font=font, fill='black', anchor='mm')
        image.save(f'{i}.jpg')

def generate_pdf():
    with open('images.pdf', 'wb') as f:
        f.write(img2pdf.convert([x for x in os.listdir(".") if x.endswith(".jpg")]))

def main():
    generate_image()
    generate_pdf()

if __name__ == "__main__":
    main()