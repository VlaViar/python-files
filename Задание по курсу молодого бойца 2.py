# №1
tpl = (42, [1, 2, 3], 'hello', False)
print(tpl)

# №2
txt = 'abcdef'
tpl = tuple(txt)
print(tpl)
tst = 54321
txt = str(tst)
tpl = tuple(txt)
print(tpl)

# №3
tpl1 = (7,)
tpl2 = (True,)
tpl3 = ('Python',)
print(tpl1,tpl2,tpl3)

# №4
tpl1 = (1, 'a', False)
tpl2 = 1, 'a', False
lst = [1, 'a', False]
tpl3 = tuple(list(lst))
print(tpl1,tpl2,tpl3)
print(type(tpl1))
print(type(tpl2))
print(type(tpl3))

# №5
tpl = (10, 20, 30, 40, 50)
print(tpl[0],tpl[-1],tpl[0]+tpl[-1])

# №6
# tpl = (4, 6, 8, 10)
# tpl[1] = 20
"""
Данный код вызовет ошибку,
так как в нем предпринимается
попытка изменить один из элементов
кортежа, что сделать невозможно.
"""

# №7
tpl = 1, 2, 3, 'a', 'b', True
print(len(tpl))

# №8
tpl1 = (1, 2, 3)
tpl2 = (4, 5, 6)
tpl3 = (7, 8, 9)
tpl_all = tpl1 + tpl2 + tpl3
print(tpl_all)

# №9
tpl1 = ('A', 'B', 'C')
tpl2 = (1, 2, 3)
tpl_r = tpl1 * 2 + tpl2
print(tpl_r)

# №10
tpl = ('apple', 'banana', 'cherry')
r = 'banana' in tpl
print(r)

# №11
tpl = ('Python', 'Java', 'C++')
lang1, lang2, lang3 = tpl
print(lang1, lang2, lang3)

# №12
lst = [10, 20, 30, 40]
tpl = tuple(lst)
print(tpl)

# №13
tpl = (5, 10, 15, 20)
lst = list(tpl)
lst.sort(reverse=True)
tpl2 = tuple(lst)
print(tpl2)

# №14
tpl = ('H', 'e', 'l', 'l', 'o')
txt = ''.join(tpl)
print(txt)