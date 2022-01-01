import arabic_reshaper
from bidi.algorithm import get_display
import tkinter
from PIL import Image, ImageFont, ImageDraw
file_name = 'cat.jpg'
image = Image.open(file_name)
font = ImageFont.truetype('BNazanin.ttf', 40, encoding='unic')
draw = ImageDraw.Draw(image)
text = 'باسلام خدمت همکار گرامی آقای امیری'
reshaped_text = arabic_reshaper.reshape(text) # correct its shape
bidi_text = get_display(reshaped_text) # correct its direction

draw.text((500, 100), bidi_text,(255,9,250), font = font,align='center')
image.show()
#
#
#
# import tkinter as tk
# fields = 'Image', 'Text','X','Y','Address'
# def show(entries):
#     list_val=[]
#     for entry in entries:
#         text  = entry[1].get()
#         list_val.append(text)
#     image = Image.open(list_val[0])
#     font = ImageFont.truetype('BNazanin.ttf', 40, encoding='unic')
#     draw = ImageDraw.Draw(image)
#     reshaped_text = arabic_reshaper.reshape(list_val[1])  # correct its shape
#     bidi_text = get_display(reshaped_text)  # correct its direction
#     x=float( list_val[2])
#     y= float(list_val[3])
#     draw.text((x, y), bidi_text, (250, 250, 250), font=font, align='center')
#     image.show()
#
# def save(entries):
#     list_val=[]
#     for entry in entries:
#         text  = entry[1].get()
#         list_val.append(text)
#     image = Image.open(list_val[0])
#     font = ImageFont.truetype('BNazanin.ttf', 40, encoding='unic')
#     draw = ImageDraw.Draw(image)
#     reshaped_text = arabic_reshaper.reshape(list_val[1])  # correct its shape
#     bidi_text = get_display(reshaped_text)  # correct its direction
#     x = float(list_val[2])
#     y = float(list_val[3])
#     draw.text((x, y), bidi_text, (250, 250, 250), font=font, align='center')
#     addres = (list_val[4])
#     image.save(addres)
#
#
# def makeform(root, fields):
#     entries = []
#     for field in fields:
#         row = tk.Frame(root)
#         lab = tk.Label(row, width=15, text=field, anchor='w')
#         ent = tk.Entry(row)
#         row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
#         lab.pack(side=tk.LEFT)
#         ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
#         entries.append((field, ent))
#     return entries
#
# if __name__ == '__main__':
#     root = tk.Tk()
#     ents = makeform(root, fields)
#     root.bind('<Return>', (lambda event, e=ents: show(e)))
#     b1 = tk.Button(root, text='Show',
#                   command=(lambda e=ents: show(e)))
#     b1.pack(side=tk.LEFT, padx=5, pady=5)
#     b2 = tk.Button(root, text='save',
#                    command=(lambda e=ents: save(e)))
#     b2.pack(side=tk.LEFT, padx=5, pady=5)
#     b3 = tk.Button(root, text='Quit', command=root.quit)
#     b3.pack(side=tk.LEFT, padx=5, pady=5)
#     root.mainloop()
import requests
from bs4 import BeautifulSoup


# def main():
#     r = requests.get('https://www.trendyol.com/penti/cok-renkli-with-love-polar-pijama-takimi-p-194865919?boutiqueId=594215&merchantId=4442')
#     soup = BeautifulSoup(r.content, features = "lxml")
#     title = soup.title.string
#     print('TITLE IS :', title)
#     meta = soup.find_all('meta')
#     for tag in meta:
#            if 'property' in tag.attrs.keys() and tag.attrs['property'].strip().lower() in ['product:price:amount', 'keywords']:
#             print('CONTENT :', tag.attrs['content'])
#
# if __name__ == '__main__':
#    main()