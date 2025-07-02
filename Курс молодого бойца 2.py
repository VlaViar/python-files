# Блок №2
# Урок №38
lst1 = ['ab','cd','ef']
lst2 = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье',1,2,3,4,5,6,7]

# Урок №39
tst = list('abcde')
print(tst)
tst = list('a12b')
print(tst)
# tst = list(5678)
# print(tst)
tst = list('4321')
print(tst)

# Урок №40
txt = 'a,b,c,d,e'
print(txt.split(','))
txt = 'a_bc_de'
print(txt.split('_'))
txt = 'ab 12 cd'
print(txt.split(' '))
txt = '123_45'
print(txt.split())

# Урок №41
lst = [1, 2, 3, 4, 5]
print(lst[0])
lst = [1, 2, 3, 4, 5]
print(lst[1])
lst = [1, 2, 3, 4, 5]
print(lst[-1])
lst = [2, 4, 6, 8]
res = lst[3] - lst[0]
print(res)

# Урок №42
lst = ['a', 'b', 'c', 'd']
print(len(lst))
tst = [1, 2,'a','b','c', 4, 5]
print(len(tst))

# Урок №43
lst = ['a', 'b', 'c', 'd']
print(lst[-2])

# Урок №44
lst = [1, 2, 3, 4, 5]
lst[1] = 10
print(lst)
lst = ['a', 'b', 'c', 'd']
lst[-1] = True
print(lst)
lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
lst1[-1] = lst2[-1]
print(lst1)

# Урок №45
lst = [1, 2, 3, 4, 5]
lst.append(6)
print(lst)
lst = []
lst.append(1)
print(lst)
lst = []
lst.append('a')
lst.append('b')
lst.append('c')
print(lst)

# Промежуточная практика (по каждому заданию)(GhatGPT)
# №1
lst = [17,9,8,1,35]
print(lst)

# №2
lst = list("Python3.10")
print(lst)

# №3
txt = "apple,banana,grape,orange"
lst = txt.split(',')
print(lst)

# №4
lst = [10, 20, 30, 40, 50]
print(lst[0], lst[-1], (lst[2]-lst[0]))

# №5
lst = [1,2,True,3,'abc',4]
print(len(lst))

# №6
lst = ['Python', 'Java', 'C++', 'JavaScript']
print(lst[-2])

# №7
lst = [100, 200, 300, 400, 500]
lst[1] = 'Python'
lst[-1] = 0
print(lst)

# №8
lst = []
lst.append('red')
lst.append('blue')
lst.append('violet')
print(lst)

# Урок №46
lst = [1, 2, 3, 4, 5]
lst.insert(2,'a')
print(lst)
lst = [1, 2, 3, 4, 5]
lst.insert(0,'a')
print(lst)
lst = [3, 6, 12]
lst.insert(-1,9)
print(lst)

# Урок №47
lst1 = ['a', 'b', 'c']
lst2 = ['d', 'e']
lst1.extend(lst2)
print(lst1)
lst1 = ['a', 'b', 'c']
lst2 = ['d', 'e']
lst3 = [1, 2, 3]
lst1.extend(lst2)
lst1.extend(lst3)
print(lst1)

# Урок №48
lst1 = ['4', '5', '6']
lst2 = ['1', '2', '3']
r = lst2 + lst1
print(r)
lst1 = ['a', 'b', 'c']
lst2 = ['d', 'e']
lst3 = [1, 2, 3]
lst = lst1 + lst2 + lst3
print(lst)

# Урок №49
lst1 = ['12', '34', '56']
lst2 = ['ab', 'cd', 'ef']
lst1 += lst2
print(lst1)
lst1 = ['a', 'b', 'c']
lst2 = [4, 5, 6]
lst2 += lst1
print(lst2)

# Промежуточная практика (по каждому заданию)(GhatGPT)
# №1
lst = [10, 20, 30, 40, 50]
lst.insert(2,25)
lst.insert(0,'Python')

# №2
fruits = ["яблоко", "банан", "виноград"]
berries = ["клубника", "малина"]
fruits.extend(berries)
print(fruits)

# №3
nums = [1, 2, 3]
letters = ["a", "b", "c"]
bools = [True, False]
lst = nums + letters + bools
print(lst)

# №4
lst1 = [100, 200, 300]
lst2 = ["x", "y", "z"]
lst1 += lst2
print(lst1)

# Урок №50
lst = ['a', 'b', 'c', 'd', 'e']
del lst[0]
print(lst)
lst = ['a', 1, 'b', 2, 'c', 3]
del lst[1]
del lst[2]
del lst[3]
print(lst)

# Урок №51
lst = ['a', 'b', 'c', 'd', 'e']
lst.remove('c')
print(lst)
lst = ['a','b','c','d','e']
lst.remove('b')
print(lst)
lst = ['b', 1, 2, 'b', 'c', 2]
lst.remove('b')
lst.remove(2)
print(lst)

# Урок №52
lst = ['a', 'b', 'c', 'd', 'e']
print(lst.pop())
print(lst)
lst = ['a', 'b', 'c', 'd', 'e']
print(lst.pop(0))
print(lst)
lst = ['a', 'b', 'c', 'd', 'e']
print(lst.pop(1))
print(lst)

# Урок №53
lst = ['a', 'b', 'c', 'd', 'e']
lst.clear()
print(lst)
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1.extend(lst2)
print(lst1)
lst2.clear()
print(lst2)

# Промежуточная практика (по каждому заданию)(GhatGPT)
# №1
lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
del lst[0]
print(lst)
del lst[1]
print(lst)
del lst[-1]
print(lst)

# №2
lst = ['cat', 'dog', 'fish', 'bird', 'cat', 'dog']
lst.remove('cat')
lst.remove('dog')
print(lst)

# №3
lst = [10, 20, 30, 40, 50]
print(lst.pop())
lst = [10, 20, 30, 40, 50]
print(lst.pop(2))
lst = [10, 20, 30, 40, 50]
print(lst.pop(0))

# №4
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1.clear()
lst1.extend(lst2)
print(lst1)
lst2.clear()
print(lst2)

# Урок №54
lst = ['a', 'b', 'c', 'd', 'e']
print(lst.index('c'))
lst = ['a', 'b', 'c', 'b', 'd']
print(lst.index('b'))
lst = ['ab', 12, 'cd', 34]
tst = 'cd'
print(lst.index(tst))
# lst = [1, 3, 'a', 'b', 3, 6]
# tst = 2
# print(lst.index(tst))

# Урок №55
lst = ['a', 'b', 'c', 'd', 'e']
r = 'c' in lst
print(r)
lst = ['a', 'b', 'c', 'd']
res = 'e' in lst
print(res)
lst = ['a', 1, 'b', 3, 'c']
res = 3 in lst
print(res)

# Урок №56
lst = ['a', 'b', 'c', 'd']
print(lst.count('c'))
lst = ['1', 'b', '2', 'd']
print(lst.count(1))
lst = ['ab', '12', 2, 'cd', 1, 2]
print(lst.count(2))

# Урок №57
lst = ['a', 'b', 'c', 'd']
lst.reverse()
print(lst)
lst = [10, 4, 8, 2]
lst.reverse()
print(lst)
lst1 = [1, 2, 3, 4]
lst2 = [7, 6, 5]
lst2.reverse()
lst1.extend(lst2)
print(lst1)

# Промежуточная практика (по каждому заданию)(GhatGPT)
# №1
lst = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(lst.index('cherry'))
print(lst.index('banana'))

# №2
lst = ['red', 'green', 'blue', 'yellow']
r1 = 'green' in lst
r2 = 'purple' in lst
print(r1, r2)
print(5 in ['a', 1, 'b', 5, 'c'])

# №3
lst = ['dog', 'cat', 'dog', 'bird', 'dog', 'cat']
print(lst.count('dog'))
print(lst.count('cat'))
print(lst.count('rabbit'))

# №4
lst1 = [3, 6, 9, 12, 15]
lst2 = ['one', 'two', 'three', 'four']
lst1.reverse()
lst2.reverse()
print(lst1)
print(lst2)
lst2.reverse()
print(lst2 + lst1)

# Урок №58
lst = [4, 2, 5, 1, 3]
# lst.sort(reverse=False)
# print(lst)
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
lst = [1, 2, 3, 4, 5]
# lst.reverse()
# print(lst)
lst.sort(reverse=True)
print(lst)
lst1 = ['a', 'b', 'c']
lst2 = [3, 2, 1]
lst2.sort()
lst1.reverse()
lst2.extend(lst1)
print(lst2)

# Урок №59
lst = ['d', 'c', 'b', 'a']
r = sorted(lst)
print(r)
lst = [4, 12, 24]
r = sorted(lst,reverse=True)
print(r)
lst = [10, 8, 6, 4]
r = sorted(lst,reverse=False)
print(r)

# Урок №60
lst = ['a', 'b', 'c', 'd', 'e']
r = '-'.join(lst)
print(r)
lst = ['a', '1', 'b', '2']
res = ''.join(lst)
print(res)
# lst = ['1', '2', 3, '4']
# res = '/'.join(lst)
# print(res)
lst = ['4', '3', '2', '1']
lst.reverse()
r = ''.join(lst)
print(r)

# Промежуточная практика (по каждому заданию)(GhatGPT)
# №1
numbers = [15, 3, 8, 22, 7, 10]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
words = ["apple", "banana", "cherry", "date"]
words.sort(reverse=True)
words += numbers
print(words)

# №2
values = [100, 50, 75, 25, 10]
asc_values = sorted(values,reverse=False)
desc_values = sorted(values,reverse=True)
print(values,asc_values,desc_values)

# №3
letters = ['A', 'B', 'C', 'D']
numbers = ['1', '2', '3', '4']
letters_txt = '*'.join(letters)
numbers_txt = ''.join(numbers)
numbers.reverse()
numbers = '-'.join(numbers)
print(letters_txt, numbers_txt, numbers)