print(2+2)
print(2*2)
print(54%2)
print(2+2)
print(2**4) #EXPONENET 2 ko 4 dafa multiply kro
print(32%2)#remainder after division
#PEMDAS KO FOLLLOW KRO YANI PARANTHESIS EXPONENET MULTIPLICATION DIVISION ADDITION SUBTRACTION
print(3**2/2*3/3+6-4/(2*6)) #

#type casting
int("25")        # 25      (str -> int)
float("3.5")     # 3.5     (str -> float)
str(100)         # "100"   (int -> str)
bool(0)          # False
list("abc")      # ['a', 'b', 'c']
tuple([1, 2])    # (1, 2)
set([1, 1, 2])   # {1, 2}
int(7.9)         # 7  (decimal part is cut off, not rounded)
float(5)         # 5.0
int("10", 2)     # 2  (string read as binary)
bool("")         # False  (empty string, 0, None, empty list are False)
bool("hello")    # True   (anything non-empty is True)

#Implicit typecasting (Python does it automatically)


x = 5        # int
y = 2.5      # float
z = x + y    # 7.5 -> int is promoted to float
print(type(z))  # <class 'float'>

#Python promotes to the “bigger” type (int to float) so no data is lost.

#Common mistake: input() always returns a string


age = input("Enter age: ")   # "20" (a string)
age = int(age)               # now a number
print(age + 1)               # 21

#Invalid conversions raise an error


# int("abc")      # ValueError
#2
# int("3.5")      # ValueError (convert to float first: int(float("3.5")))

#You can handle this safely:

try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid number")

# Quick summary

# Function	Converts to
# int()	integer
# float()	decimal number
# str()	string
# bool()	True/False
# list(), tuple(), set(), dict()	collections

hammad_age=4
age_at_school=5
print(hammad_age>=age_at_school) #False