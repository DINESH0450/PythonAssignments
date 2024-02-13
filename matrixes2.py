# len()
t=(10,20,30,40,50,60,70)
print(len(t))

s=("dinesh",20,1.2,40,"kumar",60,70,"pulakunta")
print(len(s))

a=(1.2,3.2,54,67,"p")
print(len(a))

# count()
num=(10,20,30,40,50,60,70)
x=num.count(50)
print(x)

num=(10,20,30,40,50,60,70,50,90,20,50,60)
x=num.count(50)
print(x)

fruits=("apple","banana","apple","cherry","kiwi")
f=fruits.count("apple")
print(f)

#index()
num=(10,20,30,40,50,60,70)
n=num.index(40)
print(n)

fruits=("apple","banana","apple","cherry","kiwi")
f=fruits.index("kiwi")
print(f)

a=(1,2,3,4,5,6,7,8,9)
b=a.index(9)
print(b)

#sorted()
num=(20,40,10,80,50,30,5,60)
s=sorted(num)
print(s)

name=("dineshkumar","pulakunta","laddu","dinesh","kumar")
s=sorted(name)
print(s)

nagitiveNum=(-2,-3,5,60,-59,-39,-10,-20,-40)
s=sorted(nagitiveNum)
print(s)

#tuple packing
a=10
b=20
c=30
d=40
num=a,b,c,d
print(num)

a="dinesh"
b="kumar"
c="pulakunta"
name=a,b,c
print(name)

a=10
b="dinesh"
c=-20
d="kumar"
e=10
nums=a,b,c,d,e
print(nums)

#tuple unpacking
name=("dineshkumar","pulakunta","laddu","dinesh","kumar")
a,b,c,d,e=name
print(a,b,c,d,e)

num=(20,40,10,80,30)
a,b,c,d,e=num
print(a,b,c)

#tuple comprehensive
a=(x*x for x in range(20) if x%2 !=0)
print(a)
for i in a:
    print(i)


a=(x*x for x in range(20) if x%2==0)
print(a)
for i in a:
    print(i)


b=(x*x for x in range(8)  if x%2==0)
print(b)
for i in b:
    print(i)

#set data type
#add()
s={10,20,30,40}
print(s)
s.add(50)
print(s)

s={10,20,30,40}
s.add("dineshkumar")
print(s)

s={"dinesh","kumar","pulakunta"}
s.add("dineskumar")
print(s)

#copy()
s1={"dinesh","kumar","pulakunta"}
s2=s1.copy()
print(s2)
print(s1)

set1={"dineshkumar",10,20,-30,"pulakunta"}
set2=set1.copy()
print(set2)
print(set1)

a={10,20,30,40,50}
b=a.copy()
c=b.copy()
print(a)
print(b)
print(c)

#pop()
a={10,20,30,40,50} 
print(a.pop())

set1={"dineshkumar",10,20,-30,"pulakunta"}
print(set1.pop())

s1={"dinesh","kumar","pulakunta"}
print(s1.pop())

# remove()
a={10,20,30,40,50,60} 
a.remove(10)
print(a)

a={10,20,30,40,50,60} 
a.remove(30)
print(a)

s1={"dinesh","kumar","pulakunta"}
s1.remove("kumar")
print(s1)

#discard()
s={10,30,40,50,60,70}
s.discard(30)
print(s)

set1={"dineshkumar",10,20,-30,"pulakunta"}
set1.discard("dineshkumar")
print(set1)

#clear()
s={10,30,40,50,60,70}
s.clear()
print(s)

set1={"dineshkumar",10,20,-30,"pulakunta"}
set1.clear()
print(set1)