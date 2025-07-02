from itertools import *
sum=0
for a in product('ABCDEFX',repeat=4):
    b=''.join(a)
    if b.count('X')==1:
        sum+=1
print(sum)