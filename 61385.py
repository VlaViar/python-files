summa = 0
for n in range(1,2000000001):
    a=bin(n)[2:]
    b=a+(bin(n%3)[2:])
    c=b+(bin(b%5)[2:])
    r=int(c,2)
    if r>=1222222222 and r<=1555555666:
        summa+=1
print(summa)