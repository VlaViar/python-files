for n in range(1000,10000):
    z=str(n)
    a=int(z[0])+int(z[1])
    b=int(z[1])+int(z[2])
    c=int(z[2])+int(z[3])
    first=str((a+b+c)-max(a,b,c)-min(a,b,c))
    second=str(max(a,b,c))
    r=int(first+second)
    if r==1517:
        print(n)
        break