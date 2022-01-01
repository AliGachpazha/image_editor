import requests
from pprint import pprint
import requests
import extruct
from w3lib.html import get_base_url


def get_html(url):
    """Get raw HTML from a URL."""
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    req = requests.get(url, headers=headers)
    return req.text


def get_metadata(html, url):
    """Fetch JSON-LD structured data."""
    metadata = extruct.extract(
        html,
        base_url=get_base_url(html, url),
        syntaxes=['json-ld'],
    )['json-ld'][0]
    return metadata

def get_metadata1(html, url):
    """Fetch JSON-LD structured data."""
    metadata = extruct.extract(
        html,
        base_url=get_base_url(html, url),
        syntaxes=['json-ld'],
    )['json-ld'][0]
    return metadata

def scrape(url):
    """Parse structured data from a target page."""
    html = get_html(url)
    metadata = get_metadata(html, url)

    return metadata

list=get_html('https://www.koton.com/tr/kadin-simli-pencere-detayli-yarim-balikci-yaka-uzun-kollu-bluz/p/2KAK18361EK999?_sgm_campaign=scn_7e9f7c0ab4000&_sgm_source=2KAK18361EK999&_sgm_action=click#tab-1')
print(list)
# dic={}
# for i in list:
#     if i == 'offers':
#        for j in list[i]:
#            if j =='lowPrice':
#                dic['lowPrice']=list[i][j]
#            if j=='highPrice':
#                 dic['highPrice']=list[i][j]
#            if j=='price':
#                 dic['price'] = list[i][j]
#            if j == 'offers':
#                for p in list[i][j]:
#                    if p == 'price':
#                        for q in list[i][j]:
#                            if q == 'price':
#                                dic['price']=list[i][j][q]
#     if i == 'image':
#         dic['image']=list[i]
# print(dic)
# next(item for item in list if item == 'price')
# def search(name):
#     for p in list:
#         if p['price'] == name:
#             return p
#
# search("price")
# d = next((d for d in dicts if d.get(key) == val), None)
# print(d)