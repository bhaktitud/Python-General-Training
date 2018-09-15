# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 21:00:36 2018

@author: Bhakti
"""

from functionMods import simple_get, get_names, get_hits_on_name
from functionMods import log_error
from bs4 import BeautifulSoup

raw_html = 'https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/{}'
source_html = 'http://www.fabpedigree.com/james/mathmen.htm'

#           https://shopee.co.id/shop/61648718/search/?shopCollection=10099797
#           http://www.fabpedigree.com/james/mathmen.htm


if __name__ == '__main__':
    print('Getting the list of names .... ')
    names = get_names(source_html)
    print('... done.\n')
    
    result = []
    
    print('Getting stats for each name....')
    
    for name in names:
        try:
            hits = get_hits_on_name(name, raw_html)
            if hits is None:
                hits = -1
                
            result.append((hits, name))
        
        except:
            result.append((-1, name))
            log_error('error encountered while processing '
                      '{}, skipping'.format(name))
            
    print('... done.\n')
    
    result.sort()
    result.reverse()
    
    if len(result) > 5:
        top_marks = result[:5]
    else:
        top_marks = result
        
    
    print('\nThe most popular mathematician are:\n')
    for (mark, mathematician) in top_marks:
        print('{} with {} pageviews'.format(mathematician, mark))
        
    no_result = len([res for res in result if res[0] == -1])
    print('\nBut we did not find results for '
          '{} mathematicians on the list'.format(no_result))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    