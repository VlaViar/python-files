from itertools import *
r=0
for a in product('АБВГ',repeat=5):
    b=''.join(a)
    if b.count('А')==1:
        r=r+1
    else:
        r=r+0
print(r)