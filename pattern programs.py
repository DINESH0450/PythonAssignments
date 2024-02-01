n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("*", end=" ")
    print()

n=5
k=2*n-2
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(0,i+1):
        print("*", end=" ")
    print()

n=5
for i in range (n,0,-1):
    for j in range(0,i):
        print("*", end=" ")
    print()

n=5
for i in range(n):
    for j in range (i):
        print(" ",end=" ")
    for j in range (i,n):
        print('*',end=" ")
    print()

n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()