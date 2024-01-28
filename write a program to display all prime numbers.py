#8. Write a program to display all prime numbers within a range
num=int(input('Enter the number to print prime numbers with in the range:'))
for i in range (num + 1):
    if i>1:
        for j in range (2,i):
            if (i %j)==0:
                break
        else:
            print(i)