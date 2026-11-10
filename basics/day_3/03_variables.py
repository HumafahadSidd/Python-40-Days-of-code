"""
Rules for Naming Variables
1. A variable name must start with a letter or an underscore (_).
2. A variable name cannot start with a number.
3. A variable name can contain letters, numbers, and underscores.
4. Spaces are not allowed in variable names.
5. Special characters such as @, #, $, and % are not allowed.
6. Variable names are case-sensitive. For example, age and Age are different.
7. Python keywords such as if, for, and class cannot be used as variable names.
8. Use meaningful names to make code easier to understand
"""
#agr same name se variabe bnaya to update hojaega next line men
#operator use nahi kren in naming variables
#set ya array bnaen to variable men store kren
from typing import Type


fruit_basket = ("apple", "banana", "orange") #ye tuple hai iimutable hai change nahe hoge
print(fruit_basket)
x=(6-4)+6*5
print(x) #direct answer print krega
print(type(x)) #type of x print krega
print(type(fruit_basket)) #type of fruit_basket print krega

""""
   Type	Meaning	Example
   int	Whole numbers	age = 20
   float	Decimal numbers	price = 99.5
   str	Text	name = "Ali"
   bool	True or False	is_student = True
   list	Multi   ple values, changeable	fruits = ["apple", "mango"]
   tuple	Multiple values, unchangeable	fruits = ("apple", "mango")
   set	Unique values, no duplicates	nums = {1, 2, 3}
   dict	Key-value pairs	student = {"name": "Ali", "age": 20}
   NoneType	No value	result = None
   
   Yaad rakhne ka easy formula:
- int = Integer
- float = Decimal
- str = String / Text
- bool = True / False
- list = Changeable collection
- tuple = Fixed collection
- set = Unique collection
- dict = Key-value data
Tip: Kisi variable ka type check karne ke liye type() use karo.

"""

"""type casting 
Yaad rakho: int(), float(), str() aur bool() type casting ke common functions hain.
"""
age = "20"
age = int(age)
print(age + 5)

"""1. Tuple ()
Tuple multiple values store karta hai. Iski values change nahi kar sakte (immutable).
fruit_basket = ("apple", "banana", "orange")print(fruit_basket)print(fruit_basket[0])



Output:
('apple', 'banana', 'orange')
apple


2. List [] — Array jaisi
Python mein beginners ke liye List ko samajhna easy hai. Is mein values change, add aur remove kar sakte hain.
fruit_basket = ["apple", "banana", "orange"]fruit_basket.append("mango")print(fruit_basket)



Output:
['apple', 'banana', 'orange', 'mango']


3. Set {}
Set unique values store karta hai. Is mein duplicate values nahi rehtin aur indexing nahi hoti.
fruit_basket = {"apple", "banana", "apple"}print(fruit_basket)



Output mein apple sirf ek baar hoga:
{'apple', 'banana'}


Set mein items ka order guaranteed nahi hota.
Easy comparison
Feature	List	Tuple	Set
Brackets	[]	()	{}
Duplicates	Allowed	Allowed	Not allowed
Values change kar sakte hain?	Yes	No	Yes
Indexing	Yes	Yes	No

Yaad rakhne ka easy formula:
- List: values change karni hon.
- Tuple: values fixed rakhni hon.
- Set: sirf unique values chahiye hon.
Note: Python mein built-in array bhi hota hai, lekin list zyada flexible hai aur beginners aam tor par pehle List seekhte hain."""