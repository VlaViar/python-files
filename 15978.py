from itertools import *
number=0
for a in product('КЛНТЭ',repeat=6):
    b=''.join(a)
    number+=1
    if b=='ККЛКЛК':
        print(number)