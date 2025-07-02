for n in range (1,101):
    s=bin(n)[2:]
    if s.count('1')%2==0:
        s=s+'0'
    else:
        s=s+'1'
    if s.count('1')%2==0:
        s=s+'0'
    else:
        s=s+'1'
    r=int(s,2)
    if r>43:
        print (r)
        break
        
