for N in range (1,101):
    b=bin(N)[2:]
    b=str(b)
    b+='1'+'0'
    r=int(b,2)
    if r>90:
        print(r)
        break
        
