# The len function is used to find the length of a string.
import datetime

message = 'Pinak95'
#          01234567
#          -7-6-5-4-3-2-1 0
print(len(message))

# To print the character at a particular index we can use the indexing operator.
print(message[3])

""" Printing the character that is out of index will throw an error.
    print(message[7])"""

# We can also use negative indexing to print the characters from the end.
print(message[-7])

# To print particular part of the string we can use slicing.
print(message[0:5])

# We can print the same part of the string using negative indexing.
print(message[-7:-2])

# Or we can print the same part by
print(message[:5])

""" If you want to include the last character of the string you can just mention the start index.
    Because the end in the slicing operator is not included.
    But the start in the slicing operator is included."""
print(message[0:])

""" Slicing is done by the colon operator. It is used in the following manner message[start:end:step].
    The default step value is 1."""
print(message[::2])

# The reverse slicing operator is used to print the characters in reverse order.
print(message[::-1])

# Methods and Functions are the same thing but a method is a function that belongs to an object.

# The upper method is used to convert the string to upper case.
print(message.upper())

# The lower method is used to convert the string to lower case.
print(message.lower())

# Combining the slicing operator along with the upper() and lower() method.
print(message[0:1].lower()+message[1:].upper())

# The count method is used to count the number of times a character occurs in a string.
print(message.count('ak'))

# The find method is used to find the index of a character in a string.
print(message.find('a'))

# When we try to find the index of a character that is not present in the string it will give us -1.
print(message.find('ok'))

# The index() method is used to find the index of a character in a string.
print(message.index('a'))

""""When we use the index() method to find the index of a character that is not present
in the string it will give us an error. """
# print(message.index('ok'))

# The replace method is used to replace a character/substring in a string.
print(message.replace('Pinak', 'Aditya'))

""" We can even set the same variable to a new string using the replace() method.
    message = message.replace('Pinak', 'Aditya')"""

name = 'Aditya'
programming_language = 'Python'
greetings = 'Hello!'

# Using concatenation operator.
print("Hello, I am " + name + " and I am learning " + programming_language)

# Concatenation of the variables.
print(greetings + " " + name)

"""You can even do it in the variables as well.
    message = greetings + ' ' + name"""

""" We can create a message template using the format() method.
    Creating a simple template with placeholders """
template = "Hello, I am {} and I am learning {}."

# Using format() to fill in the placeholders
result = template.format(name, programming_language)

# Output: Hello, I am Pinak and I am learning Python.
""" You can change the variables name 
    and programming_language as per your requirement. """
print(result)

# How to format a dictionary.
person = {'name': 'Aditya', 'programming_language': 'Python'}
result = "Hello, I am {0} and I am learning {1}.".format(person['name'], person['programming_language'])

""" 
result: 'My name is {0[name]} and I am learning {1[programming_language]}'.format(person, person)
result: 'My name is {0[name]} and I am learning {0[programming_language]}'.format(person)
result: 'My name is {name} and I am learning {programming_language}'.format(**person) 
"""
print(result)

# Formatting a decimal place.

pi = 3.1415926
result = "The value of pi is {0:.2f}".format(pi)
print(result)

# Formatting a large number.
result = "The value of pi is {0:,}".format(pi*100000)
print(result)

# How to format a date.
birth_date = datetime.datetime(2001, 2, 11, 21, 4, 00)

# February 11, 2001
result = "I was born on {0:%A} of {0:%B %d %Y} at {0:%H:%M:%S}".format(birth_date)
print(result)

"""You can use https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes 
   to check the codes for the formatting using strftime()"""

# The f strings are used to format the string. And they are introduced after python 3.6.
result = f"I was born on {birth_date:%A} of {birth_date:%B %d %Y} at {birth_date:%H:%M:%S}"
print(result)

# If you want to see all the methods regarding the string class you can use dir() function.
print(dir(str))

# You can even use the help() function to see the documentation of the string class.
print(help(str))
