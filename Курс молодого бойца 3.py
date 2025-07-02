# Блок №3
# Урок №62
tst = (12, 34, 45)
tst = [1, 2, 3]
tst = ([1, 2, 3], True, 'a', 'b')
print(tst)

# Урок №63
tst = (1, 2, 3, 4, 5)
print(tst)
txt = '12345'
tpl = tuple(txt)
print(tpl)
tst = 98765
tpl = tuple(str(tst))
print(tpl)

# Урок №64
tst = ('1')
tst = (1,)
tst = (True)

# Урок №65
tst = 1, 2, 3, 4
tst = ['12', '34', '56', '78']
tst = '1,2,3,4'

# Урок №66
tpl = (1, 2, 3, 4)
print(tpl[0])
tpl = ('a', 'b', 3, 4, 'c')
print(tpl[2])
tpl = (10, 9, 8, 7, 6)
print(tpl[-1])
print(tpl[-2])
tpl = (1, 2, 3)
print(tpl[0]+tpl[1]+tpl[-1])

# Урок №67
tpl = ('ab', 'cd', 'ef')
print(tpl[1])
# tpl = (4, 6, 8, 10)
# res = tpl[-1] + tpl[0]
# tpl[1] = res
# print(res)

# Урок №68
tpl = ('1', 'b', '3', 'd', '5')
print(len(tpl))
tpl = (1, 2, 3)
print(len(tpl))

# Урок №69
tpl1 = ('1', '2', '3')
tpl2 = ('4', '5', '6')
tpl3 = ('7', '8', '9')
tpl1 += (tpl2 + tpl3)
print(tpl1)
tpl1 = (3, 4)
tpl2 = (1, 2)
tpl3 = tpl2 + tpl1
print(tpl3)

# Урок №70
tpl1 = ('1', '2', '3')
tpl2 = tpl1 * 3
print(tpl2)
tpl1 = ('a', 'b')
tpl2 = (1, 2)
tpl3 = tpl1 * 2 + tpl2
print(tpl3)

# Урок №71
tpl = (2, 4, 6, 10)
r = 8 in tpl
print(r)
tpl = ('abc', 'def')
r = 'd' in tpl
print(r)
tpl = ('1', '2', '3')
res = 1 not in tpl
print(res)
tpl1 = ('ac', '3', 4, 'bd', 5)
tpl2 = (1, 2, 3)
res1 = 4 in tpl1
res2 = 2 not in tpl2
print(res1)
print(res2)

# Урок №72
tpl = ('john', 'smit')
txt1, txt2 = tpl
print(txt1, txt2)
tpl = (2, 6, 14)
a, b, c, = tpl
print(a+b+c)

# Урок №73
tst = ['a', 'b', 'c', 'd']
tpl = tuple(tst)
print(tpl)
tst = 'abcde'
tpl = tuple(tst)
print(tpl)
tst = 12345
tpl = tuple(str(tst))
print(tpl)

# Урок №74
tpl = ('2', '6', '12')
lst = list(tpl)
print(lst)
tpl1 = ('1', '2', '3')
tpl2 = ('4', '5')
lst = list(tpl1) + list(tpl2)
print(lst)
tpl = (1, 2, 3, 4, 5)
lst = list(tpl)
lst.reverse()
r = tuple(lst)
print(r)

# Урок №75
tpl = ('1', '2', '3', '4', '5')
txt = '-'.join(tpl)
print(txt)
tpl = ('1', '2', '3', '4', '5')
txt = ''.join(tpl)
print(txt)