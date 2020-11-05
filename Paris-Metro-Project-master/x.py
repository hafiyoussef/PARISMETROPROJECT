import random as r 



def convert(n):
    L=list(str(n))
    for k in range(len(L)):
        L[k]=int(L[k])
        
    return L

x=r.randint(1,10)
print("x=",x)
y=x*3
print("y=",y)
d=y*r.randint(1,2)*6
print("d=",d)
print(d)
ch=str(d)
Q=convert(ch)
print(Q)

print(sum(Q)+27)







