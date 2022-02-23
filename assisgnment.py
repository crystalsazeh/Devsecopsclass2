A Constructor is the special method (function) used to initialize the instance variables during object creation.

Types of constructors in Python

Default Constructor /Non parameterized Constructor
Parameterized Constructor
How to create the Constructors?

In python, __init__ method stimulates the constructor of the class.

When we instantiate the class we call this method. It generally used when we initialize the class attributes. It is a must for a class to have the constructor, even if they rely on the default constructor.

Syntax to define a constructor:

While declaring the constructor one important thing is Constructor always has init and the word init is having two underscores ( __ ) before and after it, Like: __init__

We declare the constructor using def Keyword.

class Addition:
    # Defininf a constructor
    def __init__(self):
        # with the help of self.xyz 
		# we are initializing instance variable
        self.num1=1000
        self.num2=2000
        self.num3=3000

    def result(self):
        self.num=self.num1+self.num2+self.num3
        print('Output:',self.num)


# Here we create the object for call 
# which calls the constructor
Sum = Addition()

# calling the instance method 
# using the object Sum
Sum.result()
................................................................................................
Python 03  buidins
abs(x)
Return the absolute value of a number. The argument may be an integer, a floating point number, or an object implementing __abs__(). If the argument is a complex number, its magnitude is returned.

aiter(async_iterable)
Return an asynchronous iterator for an asynchronous iterable. Equivalent to calling x.__aiter__().

Note: Unlike iter(), aiter() has no 2-argument variant.

New in version 3.10.

all(iterable)¶
Return True if all elements of the iterable are true (or if the iterable is empty). Equivalent to:
