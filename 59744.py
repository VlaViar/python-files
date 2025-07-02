from itertools import *
a=0
number=0
for c in permutations('МУЖЧИНА',6):
    d=''.join(c)
    if d[0]!='Ч' and d.count('Ж')>=1:
        number+=1
        if number%2!=0:
            a+=1
print(a)