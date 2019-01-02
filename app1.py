# -*- coding: utf-8 -*-

import json
from difflib import get_close_matches #method to campare sequences

data = json.load(open("data.json"))

def definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()] #check for proper names
    elif word.upper() in data:
        return data[word.upper()]#check for abbreviationslike USA
    elif len(get_close_matches(word, data.keys(), cutoff=0.7)) > 0:
        yn = input("Did you mean %s instead? Enter Y or N: " %get_close_matches(word, data.keys(), cutoff = 0.7)[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys(), cutoff = 0.7)[0]]
        elif yn == "N":
            return "The word does not exist."
        else:
            return "We did not undestood your entry."
    else:
        return "The word does not exist. Please double check it."


word = input("Enter word: ")
output = definition(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
