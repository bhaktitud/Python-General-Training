# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 20:52:55 2018

@author: Bhakti
"""

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup



def simple_get(url):
    
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
            
            
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None
    
def is_good_response(resp):
    
    content_type = resp.headers['Content-Type'].lower()
    return(resp.status_code == 200
           and content_type is not None
           and content_type.find('html') > -1)

#site_url = 'https://indoxx1.com/genre/action'    
def get_names(site_url):
    
    url = site_url
    response = simple_get(url)
    
    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        names = set()
#        for i,li in enumerate(html.select('li')):
        for li in html.select('li'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
#            print(i, li.text)        
        return list(names)
    
    raise Exception('Error retrieving contents at {}'.format(url))

#get_names(site_url)

def get_hits_on_name(name, url):

    url_root = url
    response = simple_get(url_root.format(name))

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        
        hit_link = [a for a in html.select('a')
                    if a['href'].find('latest-60') > -1]
        
        if len(hit_link) > 0:
            link_text = hit_link[0].text.replace(',', '')
            try:
                return int(link_text)
            except:
                log_error("couldn't parse {} as an `int`".format(link_text))
                
        
    
    log_error('No pageviews found for {} as an `int`'.format(name))
    return None
    

    
    




def log_error(e):
    
    print(e)
    
    
