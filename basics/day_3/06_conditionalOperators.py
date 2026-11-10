"""
    Python mein Conditional Operators
Python mein conditions check karne ke liye comparison operators use hote hain. Inki madad se hum check karte hain ke koi value doosri value ke barabar, bari ya chhoti hai.
Types of Comparison Operators
Operator	Meaning	Example	Result
==	Equal to	5 == 5	True #yahan single equal ka matlb value same hon or double equal ka men value or type same hon
!=	Not equal to	5 != 3	True
>	Greater than	8 > 5	True
<	Less than	3 < 7	True
>=	Greater than or equal to	5 >= 5	True
<=	Less than or equal to	4 <= 6	True

Example Program
    
 """
age = 20

print(age >= 18)
print(age < 18)
print(age == 20)
"""Conditional Statement: if-else
Conditions ko decision-making mein use karte hain:"""
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")
    """Comparison operators conditions check karte hain.



if, elif, else conditions ke mutabiq decisions lete hain."""