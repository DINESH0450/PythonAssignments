#1 Calculate the sum of all numbers from 2 to a given number.
num=int(input("Enter the number:"))
sum=0
for i in range(2,num+2,):
    sum=sum+i
print(sum)