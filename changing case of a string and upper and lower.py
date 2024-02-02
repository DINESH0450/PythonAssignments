#changing case of a string
#upper()
name="my name is Dinesh"
print(name.upper())
#lower()
name="My Name is Dinesh"
print(name.lower())
#swapcase()
name="my name is Dinesh"
print(name.swapcase())
#tittle()
name="my name is Dinesh"
print(name.title())
#Captilise()
name="my name is Dinesh"
print(name.capitalize())

#isalnum()
name="my name is Dinesh07"
print(name.isalnum())
name="mynameisDinesh07"
print(name.isalnum())
name="my name is Dinesh1999"
print(name.isalnum())

#isalpha()
name="my name is Dinesh1999"
print(name.isalpha()) #False
name="My name Is Dinesh"
print(name.isalpha())#False
name="MY NAME IS DINESH"
print(name.isalpha())#False
name="MYNAMEISDINESH"
print(name.isalpha()) #True
name="MYNAMEISDINESH 1999"
print(name.isalpha())#False

#isdigit()
myNum="Dinesh 12345"
print(myNum.isdigit()) #False
myNum="Dinesh12345"
print(myNum.isdigit())#False
myNum="DINESH12345"
print(myNum.isdigit())#False
myNum="12345"         #True
print(myNum.isdigit())
myNum="  12345"       #False
print(myNum.isdigit()) 

#islower()
name="my name is Dinesh 1999"
print(name.islower())#False
name="my name is Dinesh 1999"
print(name.islower()) #True
name="my name is Dinesh"
print(name.islower()) #True
name="MY NAME IS DINESH " 
print(name.islower())#False 

#isupper()
name="My name is Dinesh 1999"
print(name.isupper()) #False
name="My Name Is Dinesh 1999"
print(name.isupper()) #False
name="MY NAME IS DINESH 1999" 
print(name.isupper()) # True
name="MYNAMEISDINESH"
print(name.isupper()) #True 

#istittlecase()
name="My name is Dinesh 1999"
print(name.istitle())#False
name="My Name Is Dinesh 1999"
print(name.istitle()) #True
name="MY NAME IS DINESH 1999"
print(name.istitle()) #False 

## isspace()
name="My name is Dinesh 1999"
print(name.isspace()) #False
name="MYNAMEISDINESH1999"
print(name.isspace()) #False
name="  My name is Dinesh 1999"
print(name.isspace()) #False
name="  My name is Dinesh 1999   "
print(name.isspace()) #False
name="  MynameisDinesh1999   "
print(name.isspace()) #False
name="  M y n a m e i s D i n e s h     "
print(name.isspace()) #False
name="  My name is Dinesh 1999   "
print(name.isspace()) #False
name="    "
print(name.isspace()) #True