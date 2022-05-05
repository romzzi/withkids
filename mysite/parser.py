import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tutorialdjango.settings')
import django
import re

django.setup()

from main.models import Google

def parse_google_kids():
    result_1 = []
    req = requests.get('https://www.google.com/travel/things-to-do/see-all?g2lb=4605861%2C2502548%2C4515404%2C2503781%2C4524134%2C4545890%2C4577787%2C4597339%2C2503771%2C4308227%2C4371335%2C4306835%2C4270442%2C4401769%2C4617195%2C4317915%2C4596364%2C4258168%2C4419364%2C4284970%2C4291517%2C4270859&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0hsqf&dest_state_type=sattd&dest_src=ts&rf=EhEKDS9nLzExYzcxaHZmdDAoAQ&sa=X&ved=2ahUKEwjx7NWquLDzAhVJGaYKHSSODU8Q64UEKAF6BAggEAk#ttdm=37.551676_127.007967_12&ttdmf=%252Fm%252F06rbgx')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    list_items = soup.find_all("div", "Ld2paf")
    wiki_items = soup.find_all("div", "m3JYm UjZ9Nc")

    for item in list_items:
        
        my_name_full = item.find("div","rbj0Ud")
        my_content_full = item.find("div", "nFoFM")
        my_pic_full = item.find("img", "R1Ybne")

        my_name = my_name_full.text.strip()
        my_content = my_content_full.text.strip()
        my_pic = my_pic_full['data-src']
        
        item_obj = {
            'name' : my_name,
            'content' : my_content,
            'main_pic' : my_pic,
        }

        #print(my_pic)
        #print(my_name)
        #print(my_content)
        result_1.append(item_obj)
        #print(result_1)

    return result_1

# if __name__ == '__main__':
#     parse_google_kids()

if __name__=='__main__':
    result_2 = parse_google_kids()
    for m in result_2:
        Google(name=m['name'], content=m['content'], main_pic=m['main_pic']).save()