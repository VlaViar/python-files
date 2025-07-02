s=0
for n in range(1,2000000001):
    a=bin(n)[2:]
    if n%2!=0:
        a+='1'
    elif n%2==0:
        a+='0'
        if n%2!=0:
            a+='1'
        elif n%2==0:
            a+='0'
            if n%2!=0:
                a+='1'
            elif n%2==0:
                a+='0'
            r=int(a,2)
            if 123456789<=r<=1987654321:
                s+=1
print(s)