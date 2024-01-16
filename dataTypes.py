#bytes data type 
D=[87,93,10,38,47]
s=bytes(D)
#D.append(20)
#D.add(67)it will be an error because bytes are inmutable
print(s)
print(type(s))

#bytes array data type
v=[87,93,10,38,47]
m=bytearray(v)
m.append(20) # we can add items in bytes array data type because its mutable
print(m)
print(type(m))

#list data type

a=[5,4,7,20,60,53,60,"Dinu"]
a.append(True)
a.append(50)
a[4]="pulakunta"
a.remove(50)
print(a)

#tuple data type
b=(53,55,29,59,67,-2,58,57)
print(type(b))
#b.append(True) it will be an error because tuples are inmutable
print(b)

#set data type
c={34,67,90,45,20,59,10}
print(type(c))
c.add("Dinu")
c.remove(67)
print(c)

#Frozen set data type
d={57,48,90,204,589,274,29,50,10}
f=frozenset(d)
#f.add("Dinu") frozen sets are immutable, we can not add or remove elements from frozen set
print(f)

#dictionery data type
e={12:"dinu",10:True,20:40,}
print(type(e))
e[30]="yesu"
e[12]="pulakunta"
print(e)

#range data type
r=range(20)
print(type(r))
for i in r:
    print(i)

