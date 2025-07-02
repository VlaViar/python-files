for n in range(0,101):
    a=bin(n)[2:]
    a+=str(a.count('1')%2)
    a+=str(a.count('1')%2)
    r=int(a,2)
    if r>77:
        print(n)
        break

