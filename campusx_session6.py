# ********Let's create a function(with docstring)**********
'''def is_even(num):
  """
  This function returns if a given number is odd or even
  input - any valid integer
  output - odd/even
  created on - 16th Nov 2022
  """
  if type(num) == int:
    if num % 2 == 0:
      return 'even'
    else:
      return 'odd'
  else:
    return 'pagal hai kya?'
# function
# function_name(input)
for i in range(1,11):
  x = is_even(i)
  print(x)

print(list.__doc__) #---> predefined function documentation

# Point of views
print(is_even('hello'))

# Parameters Vs Arguments ---> also same but where in line 25 we pass parameters and in line 2 here parameter made arguments

# Types of Arguments
# Default Argument

def power(a=1,b=1):
  return a**b
print(power())

# Positional Argument

print(power(2,3))

# Keyword Argument

print(power(b=4,a=2))

#***********( *args and ** )****************
# *args passes variable number of non-keyworded arguments and on which operation of the tuple can be performed. 
# **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.
# *args and **kwargs are special Python keywords that are used to pass the variable length of arguments to a function

# *args
# allows us to pass a variable number of non-keyword arguments to a function.

def multiply(*args):
  product = 1

  for i in args:
    product = product * i

  print(args)
  return product

x=multiply(1,2,3,4,5,6,7,8)
print(x)

# **kwargs
# **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.

def display(**kwargs):

  for (key,value) in kwargs.items():
    print(key,'->',value)
display(delhi = 2600,patna = 100,nalanda = 'apna ghar')

#*************************************************************#

def myFun(arg1, **kwargs):
	for key, value in kwargs.items():
		print(key, '==', value)

myFun("Hi", first='Geeks', mid='for', last='Geeks')

# Points to remember while using *args and **kwargs
# order of the arguments matter(normal -> *args -> **kwargs)
# The words “args” and “kwargs” are only a convention, you can use any name of your choice

# Without return statement
L = [1,2,3]
print(L.append(4))
print(L)

#************ Variable Scope ***************
#---> function access the global variable
def g(y):         
    print(x)
    print(x+1)
    print(z)
x = 5
z = 4
g(x)
print(x)

# if we have also a same name variable in fuction then function use own variable not global variable
def f(y):
    x = 1
    x += 1
    print(x)
    print(y)
x = 5
f(x)
print(x)

# we cannot do any opertion on global variable through function
# def h(y):
#     x += 1
# x = 5
# h(x)
# print(x)

#****
def f(x):
   x = x + 1
   print('in f(x): x =', x)
   return x

x = 3
z = f(x)
print('in main program scope: z =', z)
print('in main program scope: x =', x)

# Nested Functions
# def f():
#   def g():
#     print('inside function g')
#     f()
#   g()
#   print('inside function f')

# print(f())

# example --> 1
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)
print(z)

# example --> 2
def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x

x = 3
z = g(x)
print('in main program scope: x = ', x)
print('in main program scope: z = ', z)

# Functions are 1st class citizens
#  functions behave like any other object, such as an int or a list.
#  That means that you can use functions as arguments to other functions,
#  store functions as dictionary values, or return a function from another function

# type and id
def square(num):
  return num**2

print(type(square))

print(id(square))

# reassign
x = square
print(id(x))
print(x(3))

a = 2
b = a
print(b)

# deleting a function
del square

def square(num):
  return num**2

# storing
L = [1,2,3,4,square]
print(L[-1](3))

s = {square}
print(s)

# returning a function
def f():
    def x(a, b):
        return a+b
    return x
    
val = f()(3,4)
print(val)

# function as argument
def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_c')
    return z()

func_b(func_a)

# Benefits of using a Function
# Code Modularity
# Code Readibility
# Code Reusability


# ******************Lambda Function*****************
# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# lamda a,b:a+b

# x -> x^2
y = lambda x:x**2
print(y(2))

# x,y -> x+y
a = lambda x,y:x+y
print(a(5,2))

# Diff between lambda vs Normal Function
# No name
# lambda has no return value(infact,returns a function)
# lambda is written in 1 line
# not reusable
# Then why use lambda functions?
# They are used with HOF

# check if a string has 'a'
a = lambda s:'a' in s
print(a('hello'))

# odd or even
a = lambda x:'even' if x%2 == 0 else 'odd'
print(a(6))

#*************** Higher Order Functions****************
# Example

def square(x):
  return x**2

def cube(x):
  return x**3

# HOF
def transform(f,L):
  output = []
  for i in L:
    output.append(f(i))

  print(output)

L = [1,2,3,4,5]

transform(lambda x:x**3,L)

# ***************Map function******************

# square the items of a list
print(list(map(lambda x:x**2,[1,2,3,4,5])))

# odd/even labelling of list items
L = [1,2,3,4,5]
print(list(map(lambda x:'even' if x%2 == 0 else 'odd',L)))

# fetch names from a list of dict

users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]

print(list(map(lambda users:users['gender'],users)))

# ******************Filter Function******************

# numbers greater than 5
L = [3,4,5,6,7]

print(list(filter(lambda x:x>5,L)))

# fetch fruits starting with 'a'
fruits = ['apple','guava','cherry']

print(list(filter(lambda x:x.startswith('a'),fruits)))

# ***************Reduce Function **************

# sum of all item
import functools

print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5]))

# find min
print(functools.reduce(lambda x,y:x if x>y else y,[23,11,45,10,1]))'''