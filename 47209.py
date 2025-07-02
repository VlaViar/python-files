for n in range(0,1001):
    b=bin(n)[2:]
    if b.count('1')%2==0:
        b+='0'
        b='10'+b[2:]
    elif b.count('1')%2!=0:
        b+='1'
        b='11'+b[2:]
    r=b
    if int(r,2)>40:
        print(n)
        break