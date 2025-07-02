for a in range(10000,100000):
    b=str(a)
    sum1=int(b[0])+int(b[2])+int(b[4])
    sum2=int(b[1])+int(b[3])
    c=str(min(sum1,sum2))+str(max(sum1,sum2))
    r=int(c)
    if r==723:
        print(a)
        break
