import string
import pprint
from operator import itemgetter
import os
import re
import scorer
from pycipher import SimpleSubstitution as SimpleSub
import random
import math

def hack(ctext):
    fitness = scorer.scorer('quads.txt')
    maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    maxscore = -99999999999
    parentscore,parentkey = maxscore,maxkey[:]
    i = 0
    delta = 0.1
    while i < 1000:
        i = i+1
        random.shuffle(parentkey)
        deciphered = SimpleSub(parentkey).decipher(ctext)
        parentscore = fitness.score(deciphered)
        count = 0
        while count < 1000:
            a = random.randint(0,25)
            b = random.randint(0,25)
            child = parentkey[:]
            # swap two characters in the child
            child[a],child[b] = child[b],child[a]
            deciphered = SimpleSub(child).decipher(ctext)
            score = fitness.score(deciphered)
            # if the child was better, replace the parent with it
            if score > parentscore:
                parentscore = score
                parentkey = child[:]
                count = 0
            count = count+1
        # keep track of best score seen so far
        if parentscore>maxscore:
            maxscore,maxkey = parentscore,parentkey[:]
        if math.fabs(parentscore-maxscore) <= delta:
            break;
    return maxkey
    
def translate(text, key):
    return SimpleSub(key).decipher(text)
    
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
