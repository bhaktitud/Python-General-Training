# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:26:14 2018

@author: Bhakti
"""

from translate import Translator

translator = Translator(to_lang="id")
translation = translator.translate("This is Phone")

print(translation)