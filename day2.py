name = input ("enter your name: ")
age = input ("who old are you: ")
print("hello " + name + " :)" + " you are " + age)
num1 = input(" enter your first number ")
sign = input(" enter a sign ")
num2 = input(" enter your second number ")
if sign == "+":
 result = int(num1) + int(num2) 
elif sign == "*":
 result = int(num1) * int(num2)
elif sign == "/":
 result = int(num1) / int(num2) 
elif sign == "-":
  result = int(num1) - int(num2) 
else:
 result = "put only signs" 
print(result)



num3 = input("enter a number")
sign2 = input("enter a sign")
num4 = input("enter another number")
if sign2 == "+":
 result2 = float(num3) + float(num4)
elif sign2 == "-":
  result2 = float(num3) - float(num4)
elif sign2 == "*":
 result2 = float(num3) * float(num4)
elif sign2 == "/":
 result2 = float(num3) / float(num4)
else:
 result2 = "only signs"
print(result2)





name2 = input("enter your name: ")
age2 = input("enter your age: ")
colour = input("enter your favorate colour: ")
gender = input(" inter your gender: ")
if gender == "male":
 result3 = ("there onse was a man named " + name2 + "\n he was " + age2 + " years old, \n and he loved his children \n he also loved the colour " + colour)
elif gender == "female":
 result3 = ("there onse was a woman named " + name2 + "\n she was " + age2 + " years old,\n and she loved her children \n she also loved the colour " + colour)
else:
 result3 = (" enter male or femal")
print(result3)








members_of_my_family = ["nabhan", "fatima", "adnan", "ibrahim", "fatten", "rama", "marwan"]
print(members_of_my_family[0])
print(members_of_my_family[1])
print(members_of_my_family[2:])
print(members_of_my_family[3:6])
print(members_of_my_family[2:3])





members_of_my_family2 = ["nabhan", "fatima", "adnan", "ibrahim", "fatten", "rama", "marwan"]
my_nums = [4, 2, 5, 77, 7, 57, 357, 537]






members_of_my_family2.insert(1, "ayla")
members_of_my_family2.append("ahmad")
members_of_my_family2.extend(my_nums)
print(members_of_my_family2)
print(my_nums)
my_nums.remove(57)
print(my_nums)
members_of_my_family2.pop()
print(members_of_my_family2)

print(my_nums.index(4))
my_nums.sort()
print(my_nums)
my_nums.reverse()
print(my_nums)
family2 = members_of_my_family2.copy()
print(family2)
members_of_my_family2.clear()
print(members_of_my_family2)





















e1 = ["karen", "mike", "harry", "tom", "trump"]
e2 = [1, 2, 3, 4, 5]
print(e1)
e1.sort()
print(e1)
e1.pop()
print(e1)
e1.remove("mike")
print(e1)
e1.append("hero")
print(e1)
e1.insert(1, "kamal")
print(e1)
e2.reverse()
print(e2)
print(e1.index("tom"))
e3 = e1.copy()
print(e3)
e3.clear()
print(e3)
e1.extend(e2)
print(e1)
