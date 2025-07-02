from itertools import *
r=0
for a in product ('ABCDEX',repeat=4):
    b=''.join(a)
    if b.count('X')==1:
        r+=1
print (r)