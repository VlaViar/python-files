r=0
for n in range(1000,10000):
    a = str(n)
    if int(a[0])%2!=0 and int(a[1])%2!=0 and int(a[2])%2!=0 and int(a[3])%2!=0:
        sum1=int(a[0])+int(a[1])
        sum2=int(a[2])+int(a[3])
        sum3=str(min(sum1,sum2))+str(max(sum1,sum2))
        if int(sum3)==616:
            r+=1
print(r)