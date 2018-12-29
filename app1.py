# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 01:53:50 2018

@author: lenovo
"""
import json
data = json.load(open("data.json"))

def definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        return "The word is not in  the dictionary"


word = input("Enter word: ")
print(definition(word))
