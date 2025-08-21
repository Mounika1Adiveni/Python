str1="mindx"
str2="solutions"
str3=str1+" "+str2
print(str3)
print(len(str3))

print(str3.upper())
print(str3.lower())
print(str3.isupper())
print(str3.islower())
name="mindx\n"
print(name *10)
name1="mindx solutions"
print(name1.capitalize())
print(name1.title())
print(name1.istitle())
print(name1.count("mindx"))
print(name1.count("solutions"))
name2="   welcome to mindx"
print(name2.strip())
print(name2.lstrip())
print(name2.rstrip())
name3="welcome to MINDX solutions"
print(name3.ljust(50),".")
print(name3.rjust(50),".")
print(name3.swapcase())

var="welcome to mindx solutions"
print(var.find("mindx"))
print(var.find('p'))
print(var.index('to'))
print(var.replace('solutions','placement drive'))
print(var.isalpha())
print(var.isnumeric())
print(var.isdigit())
print(var.isdecimal())

num='12345'
print(num.isnumeric())
print(num.isalpha())
print(num.isnumeric())
print(num.isdigit())

num1='mindx123'
print(num1.isnumeric())
print(num1.isalpha())
print(num1.isalnum())

var1="Mindx solutions"
print(var1.startswith("Mindx"))
print(var1.startswith("p"))
print(var1.endswith("s"))
print(var1.endswith("solutions"))

_var="  "
print(_var.isspace())
var2="  342"
print(var.isspace())
