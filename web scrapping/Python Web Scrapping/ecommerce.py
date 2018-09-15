# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 22:43:19 2018

@author: Bhakti
"""

import requests
import urllib.request
import json


def product_search(keyword):
    """Search Product"""
    try:
        with urllib.request.urlopen(("https://shopee.co.id/api/v2/search_items/?by=relevancy&keyword={}&limit=50&newest=0&order=desc&page_type=search").format(keyword)) as url:
        
            data_search = json.loads(url.read().decode()) 
    
        return data_search
    except ValueError as v:
        print('Decoding JSON has failed \r\n {}'.format(v))

def product_detail(itemid, shopid):
    """Product Detail"""
    try:
        with urllib.request.urlopen(("https://shopee.co.id/api/v1/item_detail/?item_id={}&shop_id={}").format(item_id, shop_id)) as url1:
            data_detail = json.loads(url1.read().decode())
            
        return data_detail
    except ValueError as v:
        print(v)

    
if __name__ == '__main__':
    """Spasi gunakan {} """
    keyword = "samsung{}s7".format("%20")
    products = product_search(keyword)
    item_id = products['items'][0]['itemid']
    shop_id = products['items'][0]['shopid']
    item = product_detail(item_id, shop_id)
    print(item.get('itemid'), item.get('images'))