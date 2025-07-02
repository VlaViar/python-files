from itertools import *
r=0
for a in product('СВЕТА',repeat=5):
    b=''.join(a)
    if b.count('С')>=1:
        r+=1
print(r)