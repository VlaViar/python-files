from itertools import *
h=0
for y in product("1234",repeat=5):
    s=''.join(y)
    if s.count('1')==2:
        h+=1
print(h)