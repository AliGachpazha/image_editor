import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image, ImageFont, ImageDraw
import requests
import urllib.request
places=[]
with open('Image.txt', 'r') as filehandle:
    for line in filehandle:
        # remove linebreak which is the last character of the string
        currentPlace = line[:-1]
        # add item to the list
        places.append(currentPlace)
print(places[0])

url = places[2]
urllib.request.urlretrieve(url, f'/Users/gachp/PycharmProjects/pythonProject2/cat.jpg')



# file_name = places[0]
# image = Image.open(requests.get(file_name, stream=True).raw)
# font = ImageFont.truetype('BNazanin.ttf', 40, encoding='unic')
# draw = ImageDraw.Draw(image)
# text = 'باسلام خدمت همکار گرامی آقای امیری'
# reshaped_text = arabic_reshaper.reshape(text) # correct its shape
# bidi_text = get_display(reshaped_text) # correct its direction
# draw.text((500, 100), bidi_text,(250,250,250), font = font,align='center')
# image.show()