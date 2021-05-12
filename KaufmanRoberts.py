def Kaufman_Roberts(V,M,A,t):
    for i in range(0,V+1):
        P.append(1)
    #Kaufman-Roberts formula
    for n in range(1,V+1):
        sum=0
        for i in range(0,M+1):
            if n >= t[i]:
                sum+=A[i]*t[i]*P[n-t[i]]
        P[n]=sum/n

P=[]
#user input

#capacity of system
V=int(input("Enter capacity of the system[V]:"))

#ilość klas usług
M=int(input("Enter the number of service classes(1-5) [M]:"))

#class traffic volume
A=[0]
for i in range(1,M+1):
    A.append(float(input("Enter class traffic volume A[%s]:"%i)))
A.append(0)

#the amount of resources needed
t=[0]
for i in range(1,M+1):
    t.append(int(input("Enter the amount of resources needed t[%s]:"%i)))
t.append(0)
print()

#calculating probabilities
Kaufman_Roberts(V,M,A,t)

#normalization
total=0
for i in range(1,V+1):
    total+=P[i]
for i in range(1,V+1):
    P[i]/=total

#blocking probability
E=[0]
for i in range(1,M+1):
    E.append(0)
    for n in range(V-t[i]+1,V+1):
        E[i]+=P[n]
    print("E(%s)=%s"%(i,E[i]))