import os
import urllib.request
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image, ImageFont, ImageDraw, ImageFile
from rembg.bg import remove
import numpy as np
from io import BytesIO
from requests import get


def create_poster(img,txt):
    filename = 'input_image.jpg'
    image_url = img
    urllib.request.urlretrieve(image_url, filename)
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    input_path = filename
    f = np.fromfile(input_path)
    result = remove(f)
    image_add = Image.open(BytesIO(result)).convert("RGBA")
    file_name = 'background.jpg'
    image = Image.open(file_name)
    font = ImageFont.truetype('BNazanin.ttf', 30, encoding='unic')
    draw = ImageDraw.Draw(image)
    text = txt
    reshaped_text = arabic_reshaper.reshape(text)  # correct its shape
    bidi_text = get_display(reshaped_text)  # correct its direction
    draw.text((170, 450), bidi_text, (255, 9, 250), font=font, align='center')
    img2 = image_add.resize((200, 200))
    image.paste(img2.convert("RGBA"), (130, 140), img2.convert("RGBA"))
    os.remove(filename)
    save_name = img.split('/')[-1]
    image.save(save_name + '.jpg')
    image.show()


http_add = input('Enter the URL:')
price_add = input('Enter the price:')
create_poster(http_add,price_add)