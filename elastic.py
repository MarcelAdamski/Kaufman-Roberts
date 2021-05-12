def ZP_elastic(V,M,A,t,cr):
    for i in range(0,V+1):
        P.append(1)
    #formula for flexible movement
    for n in range(1,V+1):
        sum=0
        for i in range(0,M+1):
            if n >= t[i]:
                sum+=A[i]+t[i]*P[n-t[i]]
        div=min(n,cr)
        P[n]=sum/div

P=[]
#user input

#real capacity
cr=int(input("Enter real capacity [cr]:"))


#virtual capacity
cv=int(input("Enter virtual capacity [cv]:"))
V=cv

#number of service classes
M=int(input("Enter number of service classes (1-5) [M]:"))

#class traffic volume
A=[0]
for i in range(1,M+1):
    A.append(float(input("Enter class traffic volume A[%s]:"%i)))
A.append(0)

#amount of resources needed
t=[0]
for i in range(1,M+1):
    t.append(int(input("Enter the amount of resources needed t[%s]:"%i)))
t.append(0)

#calculating probabilities
ZP_elastic(V,M,A,t,cr)

#normaliation
total=0
for i in range(1,V+1):
    total+=P[i]
for i in range(1,V+1):
    P[i]/=total
print()

#probability of blockade of adaptive movement
E=[0]
for i in range(1,M+1):
    E.append(0)
    for n in range(V-t[i]+1,V+1):
        E[i]+=P[n]
    print('E({})={:.20f}'.format(i,E[i]))
