orders = [
    "101, Иван, 2500",
    "102, Мария, 1800",
    "103, Алексей, 3200",
    "104, Ольга, 1500",
    "105, Дмитрий, 2900"
]
lst1 = orders[0].split(',')
lst2 = orders[1].split(',')
lst3 = orders[2].split(',')
lst4 = orders[3].split(',')
lst5 = orders[4].split(',')
names = [lst1[1], lst2[1], lst3[1], lst4[1], lst5[1]]
print(' '.join(names))
summa = [lst1[2], lst2[2], lst3[2], lst4[2], lst5[2]]
sum_all = int(lst1[2]) + int(lst2[2]) + int(lst3[2]) + int(lst4[2]) + int(lst5[2])
print(sum_all)
sum_sort = sorted(sum,reverse=True)
print(sum_sort[0])