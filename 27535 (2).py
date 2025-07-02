for n in range(1000,10000):
    s=str(n)
    sum1=s[0]+s[1]
    sum2=s[1]+s[2]
    sum3=s[2]+s[3]
    if sum1<sum2 and sum1<sum3:
        mn=min(sum2,sum3)
        mx=max(sum2,sum3)
        r=str(mn+mx)
        print (r)
    elif sum2<sum1 and sum2<sum3:
        mn=min(sum1,sum3)
        mx=max(sum1,sum3)
        r=str(mn+mx)
        print (r)
    elif sum3<sum2 and sum3<sum1:
        mn=min(sum1,sum2)
        mx=max(sum1,sum2)
        r=str(mn+mx)
        print (r)