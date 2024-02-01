#break, continue, pass
list=[20,57,93,38,78,130,79,48]
for i in list:
    if i>100:
        print(i,"sorry limit exceeded")
        break
    print(i,"is processed")

list1=[10,20,30,40,50]
list2=[10,20,50,60,90]
for i in list1:
    if list1>list2:
        print(list1,"and",list2,"are equal")
        break
    print("both are not equal")

numbers=[1,2,4,5,6,7,8,9,10]
for i in numbers:
    print(i)
    if i==8:
        print("limit reached")
        break

for i in range(5):
    for j in range(5):
        print(i,j)

        if i+j==8:
            print("hello people")
            break

numbers=[10,20,30,40,50]
target=40
for num in numbers:
    if num==target:
        print(num," is found")
        break
else:
    print(target,"not found")


for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)


numbers = [1,2,3,4,5,6,7]
for num in numbers:
    if num == 3:
        continue
    print(num)

for i in range(10):
    usernum=input("Enter 'skip' the number to skip ")
    if input=='skip':
        continue
    print(i)

nums=[10,20,30,40,50,60]
for num in nums:
    if num<40:
        continue
    print(num)