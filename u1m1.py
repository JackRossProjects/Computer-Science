from __future__ import print_function, division
import os
import sys
# CS31 U1M1
# Part 1

'''
1.) How many seconds are there in 21 minutes and 15 seconds?

2.) How many miles are there in 5 kilometers?

3.) If you run a 5 kilometer race in 21 minutes and 15 seconds,
what is your average pace (time per mile in minutes and seconds)?

4.) What is your average speed in miles per hour?

5.) Suppose the cover price of a book is $19.95, but bookstores get a
25% discount. Shipping costs $2.50 for the first copy and $1 for each additional copy.
What is the total wholesale cost for 75 copies?
'''

print("Part 1")

# 1
min = 21
sec = 15

print((min * 60) + sec)

# 2
km = 5
conversion = 0.62137119
miles = km * conversion

print(miles)

# 3
avg_sec = miles / ((min * 60) + sec)
avg = avg_sec / 60

print(avg)

# 4
mph = avg * .21

print(mph)

# 5
copies = 75
price = 19.95
discount = .75
shipping = (2.50 + (copies - 1))

total = ((price * discount) * copies) + shipping
print(total)

# Part 2
print("Part 2")

''' A function object is a value you can assign to a variable or pass as an argument.
For example, do_twice is a function that takes a function object as an argument
and calls it twice:

def do_twice(f):
    """
    Takes a function and executes it twice.
    """
    f()
    f()

Here’s an example that uses do_twice to call a function named print_spam twice:

def print_spam():
    print('spam')

do_twice(print_spam)

1.) Type this example into a script and test it.

2.) Change do_twice so it takes two arguments, a function object and a value, and calls the function
twice, passing the value as an argument.

3.) Define a function called print_twice that takes one argument and prints the value of that argument twice.

4.) Use the changed version of do_twice to call print_twice twice, passing 'spam' as an argument.

5.) Define a new function called do_four that takes a function object and a value and calls
the function four times, passing the value as a parameter. There should be only two
statements in the body of this function, not four.
'''

# 1-5


def do_twice(func, arg):
    """Runs a function twice.

    func: function object
    arg: argument passed to the function
    """
    func(arg)
    func(arg)


def print_twice(arg):
    """Prints the argument twice.

    arg: anything printable
    """
    print(arg)
    print(arg)


def do_four(func, arg):
    """Runs a function four times.

    func: function object
    arg: argument passed to the function
    """
    do_twice(func, arg)
    do_twice(func, arg)


do_twice(print, 'spam')
print('')

do_four(print, 'spam') 

# Part 3

'''
Fermat’s Last Theorem says that there are no positive integers a, b, and c such that:

a**n + b**n == c**n

for any values of n greater than 2.

1.)" Write a function named check_fermat that takes four parameters—a, b, c and n —and checks to see if
Fermats theorem holds. If n is greater than 2 and a**n + b**n = c**n the program should print,
"Holy smokes, Fermat was wrong!" Otherwise the program should print, "No, that doesn't work."

2.) Write a function that prompts the user to input values for a, b, c and n, converts them to integers,
and uses check_fermat to check whether they violate Fermat’s theorem.
'''

# SOLUTION:

# Other:
print("Hello, World!")

x = 2 ** 65536

print(x)

"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.
Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

print(x + int(y))


# Write a print statement that combines x + y into the string value 57

print(str(x) + y)

"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
print(f'Arguments: {len(sys.argv)}')
print(f'Argument List: {str(sys.argv)}')

# Print out the OS platform you're using:
print(f'Windows Version: {sys.version}')

# Print out the version of Python you're using:
print(f'Python Version: {sys.version_info}')


# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
print(f'Current Process ID: {os.getpid()}')

# Print the current working directory (cwd):
print(f'PWD: {os.getcwd()}')

# Print out your machine's login name
print(f"Machine's login name: {os.getlogin()}")

"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x is %i, y is %f, z is \"%s\"" %(x , y, z))

# Use the 'format' string method to print the same thing
print("x is {}, y is {}, z is \"{}\"".format(x, y, z))

# Finally, print the same thing using an f-string
print(f"x is {x}, y is {y}, z is \"{z}\"")

 
"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x is %i, y is %f, z is \"%s\"" %(x , y, z))

# Use the 'format' string method to print the same thing
print("x is {}, y is {}, z is \"{}\"".format(x, y, z))

# Finally, print the same thing using an f-string
print(f"x is {x}, y is {y}, z is \"{z}\"")



# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.remove(8)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(-1, 99)
print(x)

# Print the length of list x
print(len(x))

# Print all the values in x multiplied by 1000
for i in x:
    print(i * 1000)



"""
Python tuples are sort of like lists, except they're immutable and
are usually used to hold heterogenous data, as opposed to lists
which are typically used to hold homogenous data. Tuples use
parens instead of square brackets.
More specifically, tuples are faster than lists. If you're looking
to just define a constant set of values and that set of values
never needs to be mutated, use a tuple instead of a list.
Additionally, your code will be safer if you opt to "write-protect"
data that does not need to be changed. Tuples enforce immutability
automatically.
"""

# Example:

import math

def dist(a, b):
    """Compute the distance between two x,y points."""
    x0, y0 = a  # Destructuring assignment
    x1, y1 = b

    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

a = (2, 7)   # <-- x,y coordinates stored in tuples
b = (-14, 72)

# Prints "Distance is 66.94"
print("Distance is: {:.2f}".format(dist(a, b)))



# Write a function `print_tuple` that prints all the values in a tuple

def print_tuple(tuple):
    """This function will print the each value in a tuple on a seperate line."""
    for t in tuple:
        print(t)

t = (1, 2, 5, 7, 99)
print_tuple(t)  # Prints 1 2 5 7 99, one per line

# Declare a tuple of 1 element then print it
u = (1,)  # What needs to be added to make this work? The ','.
print_tuple(u)


"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 
This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295
Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
print(a[1])

# Output the second-to-last element: 9
print(a[-2])

# Output the last three elements in the array: [7, 9, 6]
print(a[-3:])

# Output the two middle elements in the array: [1, 7]
print(a[2:4])

# Output every element except the first one: [4, 1, 7, 9, 6]
print(a[1:])

# Output every element except the last one: [2, 4, 1, 7, 9]
print(a[:-1])

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(s[7:12])



"""
List comprehensions are one cool and unique feature of Python.
They essentially act as a terse and concise way of initializing
and populating a list given some expression that specifies how
the list should be populated. 
Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
for more info regarding list comprehensions.
"""

# Write a list comprehension to produce the array [1, 2, 3, 4, 5]

y = [i for i in range(5)]

print (y)

# Write a list comprehension to produce the cubes of the numbers 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

y = [i ** 3 for i in range(9)]

print(y)

# Write a list comprehension to produce the uppercase version of all the
# elements in array a. Hint: "foo".upper() is "FOO".

a = ["foo", "bar", "baz"]

y = [i.upper() for i in a]

print(y)

# Use a list comprehension to create a list containing only the _even_ elements
# the user entered into list x.

x = input("Enter comma-separated numbers: ").split(',')

# What do you need between the square brackets to make it work?
y = [i for i in x if int(i)%2 == 0]

print(y)


"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).
The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries
For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
waypoints.append({
    "lat": 22,
    "lon": 42,
    "name": 'no where'})

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.

waypoints[0].update({
    "lon": -130,
    "name": "not a real place"
})

# Write a loop that prints out all the field values for all the waypoints
for x in waypoints:
    for key in x:
        print(key, '->', x[key])




 
# Write a function is_even that will return true if the passed-in number is even.

def is_even(num):
    return num % 2 == 0

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

if is_even(num) == True:
    print('Even!')
else:
    print('Odd')