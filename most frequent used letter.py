# -*- coding: utf-8 -*-
"""
Created on Mon May 29 22:32:06 2023

@author: hp
"""

def most_frequent(string):
    d = dict()
    for key in string:
        if key is not d :
            d[key]=1
        else:
                d[key]+=1
                return d
        print (most_frequent('abdcsghfd'))
    