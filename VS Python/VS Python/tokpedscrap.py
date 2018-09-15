import json

import requests
from bs4 import BeautifulSoup as bs

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko)"
      " Chrome/60.0.3112.113 Safari/537.36")

def search_product(keyword):
    search_url = ("https://ace.tokopedia.com/search/product/v3?"
                 "scheme=https&device=desktop&related=true&_catalog_rows=5&"
                 "catalog_rows=5&_rows=60&"
                 "source=universe&ob=23&st=product&sc=56&rows=60&q={}"
                 "&unique_id=d64ec87133b349b7a6db059b7d1314be").format(keyword)
    headers = {"User - Agent": UA}
    data = requests.get(url, headers=headers).content.decode("utf-8")

    data = json.loads(data)['data']['products']

    return data


