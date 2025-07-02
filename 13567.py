from itertools import *
number=0
for a in product('ABCDE',repeat=5):
    b=''.join(a)
    if b[0]!='E' and b[4]!='A':
        number+=1
print(number)