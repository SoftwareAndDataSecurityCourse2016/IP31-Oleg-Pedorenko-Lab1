import string

cipher = {}
s = open('key.txt').read()
a = string.uppercase;
if(len(s) == len(a)):
    for i in range(len(s)):
        cipher[a[i]] = s[i]
        cipher[a[i].lower()] = s[i].lower()

text = open('text.txt').read()
ctext = ''
for c in text:
    if c in cipher.keys():
        c = cipher[c]
    ctext+=c
    
with open('ctext.txt', 'w') as text_file:
    text_file.write(ctext)