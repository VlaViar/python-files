for n in range(1000,10000):
    s=str(n)
    sum1=int(s[0])+int(s[1])
    sum2=int(s[1])+int(s[2])
    sum3=int(s[2])+int(s[3])
    m=min(sum1,sum2,sum3)
    del m
    
        
