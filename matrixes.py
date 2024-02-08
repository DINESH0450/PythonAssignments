# 4*4 matrix
x=[[10,20,30],[40,50,60],[70,80,90],[100,110,120]]
for i in range(len(x)):
    for j in range(len(x[i])):
        print(x[i][j],end=" ")
    print()


#compare string elements by using sort 
fruits=["orange","mango","watermaleon","apple"]
fruits.sort()
print(fruits)

#print odd numbers in the range 0 to 30
for num in range(30):
    if num % 2 !=0:
        print(num)
        
#words=['balaya','shafi','chiru'] expected output/: [b,s,c]

actors=["ntr","ramacharan","nani"]
first_letters=[i[0] for i in actors]
print(first_letters)

#write a program to display unique vowels present in the user entered words 
name= input("Enter the name:")
vowels = ['a','e','i','o','u']
string = [i for i in name if i in vowels]
print(string)


#req 2*1 2*2 2*3 2*4 2*5(list comperhensive)
res = [2*i for i in range(1,11)]
print(res)