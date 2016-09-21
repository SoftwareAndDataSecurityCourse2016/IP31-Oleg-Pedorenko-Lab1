import string
import pprint
from operator import itemgetter
import os
import re

def hack(text):
    freq = {}
    sample = [('E', 12.51), ('T', 9.25), ('A', 8.04), ('O', 7.60), ('I', 7.26), ('N', 7.09), ('S', 6.54), ('R', 6.12), ('H', 5.49), ('L', 4.14), ('D', 3.99), ('C', 3.06), ('U', 2.71), ('M', 2.53), ('F', 2.30), ('P', 2.00), ('G', 1.96), ('W', 1.92), ('Y', 1.73), ('B', 1.54), ('V', 0.99), ('K', 0.67), ('X', 0.19), ('J', 0.16), ('Q', 0.11), ('Z', 0.09)]
    regex = re.compile('[^a-zA-Z]')
    su = text.upper()
    su = regex.sub('', su)
    a = string.uppercase
    l = len(su)
    for c in a:
        freq[c] = round((su.count(c) + 0.0)/l * 100,3)
    freq = sorted(freq.items(), key=itemgetter(1), reverse = True)
    blah = sorted(zip(sample, freq), key = lambda x: x[0][0])    
    x = {}
    for a in blah:
        x[a[1][0]] = a[0][0]
        x[a[1][0].lower()] = a[0][0].lower()
    return x
    
def translate(text, key):
    res = ''
    for c in text:
        if c in key.keys():
            c = key[c]
        res += c
    return res
    
def swapkey(c1, c2):
    k = {}
    c1 = c1.upper()
    c2 = c2.upper()
    k[c1] = c2
    k[c1.lower()] = c2.lower()
    k[c2] = c1
    k[c2.lower()] = c1.lower()
    return k
    
s = open('ctext.txt').read()
key = hack(s)
while True:
    s = translate(s, key)    
    with open('out.txt', 'w') as o:
        o.write(s)
    y = raw_input("Enter a character to replace: ")
    z = raw_input("Enter a character to replace with: ")
    key = swapkey(y, z)
