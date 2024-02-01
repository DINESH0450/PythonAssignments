#strip
city=input("Enter the city name")
list=["Hyderabad","Bangalore","Mumbai","Kolakata"]
if city.strip() in list:
    print(city," it is available")
else:
    print(city," is not available")

name="Pulakunta Dinesh     "
myName=name.strip()
print(myName)

#lstrip
name="     Pulakunta Dinesh  "
myName=name.lstrip()
print(myName)

string1="#####my name"
string2=string1.lstrip("#")
print(string2)

#rstrip
name="Pulakunta Dinesh          "
myname=name.rstrip()
print(myname)


string1="#### my name#####"
string2=string1.rstrip("#")
print(string2)