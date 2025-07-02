for n in range(1,1001):
    a=bin(n)[2:]
    if n%3==0:
        a+=a[-3:]
    else:
        a+=bin(3*(n%3))[2:]
    r=int(a,2)
    if r<100:
        print(n)
    
    
    

        
