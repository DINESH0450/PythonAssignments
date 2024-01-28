# 5.Print list in reverse order using a loop
list=[10,30,50,60,70,80,90]
newList=[]
for i in list:
    newList=[i]+newList
print(newList)