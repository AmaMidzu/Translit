# -*- coding: utf-8 -*-
"""
Created on Thu Jul 7 18:04:17 2016

@author: dergachev
"""

dict_ = {
    u'�': 'a' ,
    u'�': 'b' ,
    u'�': 'v' ,
    u'�': 'g' ,
    u'�': 'd' ,
    u'�': 'e' ,
    u'�': 'yo' ,
    u'�': 'hz' ,
    u'�': 'z' ,
    u'�': 'i' ,
    u'�': 'j' ,
    u'�': 'k' ,
    u'�': 'l' ,
    u'�': 'm' ,
    u'�': 'n' ,
    u'�': 'o' ,
    u'�': 'p' ,
    u'�': 'r' ,
    u'�': 's' ,
    u'�': 't' ,
    u'�': 'u' ,
    u'�': 'f' ,
    u'�': 'x' ,
    u'�': 'c' ,
    u'�': 'hc' ,
    u'�': 'w' ,
    u'�': 'hw' ,
    u'�': 'hq' ,
    u'�': 'yi' ,
    u'�': 'q' ,
    u'�': 'ye' ,
    u'�': 'yu' ,
    u'�': 'ya'
}

def rus2latin(str):
    res = ""
    for c in str:
        print dict_[c]
    return res

def latin2rus(str):
    pass