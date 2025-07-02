from itertools import *
c=0
for a in product('АКРУ',repeat=5):
    b=''.join(a)
    c+=1
    d=str(int(c))+str(' ')+b
    print(d)