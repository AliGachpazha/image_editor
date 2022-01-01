import scrapy
from PIL import Image

class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['https://www.digikala.com/samsung-brand/mobile-phone/']
    start_urls = ['https://www.digikala.com/samsung-brand/mobile-phone/']

    def parse(self, response):
        titles = response.css(".c-listing__items .c-product-box .c-product-box__img img::attr(src)").extract()
        image_list=[]
        f = open("Image.txt", "w")
        for title in titles:
            f.write('%s\n' % title)
        f.close()