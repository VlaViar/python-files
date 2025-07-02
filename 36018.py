for n in range(1,1001):
    r=bin(n)[2:]
    r+=str(r.count('1')%2)
    r+=str(r.count('1')%2)
    res=int(r,2)
    if res>396:
        print(res)
        break
    
