# Python Notes

> Notes from the Python curriculum within the freeCodeCamp Full Stack Developer curriculum

The source material can be found here:

<https://www.freecodecamp.org/learn/full-stack-developer>

## Table of Contents

1. Python Basics
    1. What is Python and what are some common uses in the industry
    2. Variables
        1. Data Types
        2. Immutable Data Types
        3. Determining Data Types
        4. Data Hints
    3. `print()` Function
    4. Working with Strings
        1. Multiline Strings
        2. Strings Containing Quotation Marks
        3. String Concatenation
        4. F-Strings
        5. Indexing
        6. String Slicing
        7. `in` Operator
    5. Common String Methods
    6. Working with Integers and Floats
        1. Basic Arithmetic Operators
        2. Combining Integers and Floats
        3. Other Common Operators
        4. Converting Between Integers and Floats
        5. Common Methods
    7. Augmented Assignments
        1. Introduction and Syntax
        2. Common Augmented Assignment Operators
    8. Functions
2. (WIP)

## Python Basics

### What is Python and what are some common uses in the industry?

Python is a general-purpose programming language known for its simplicity and ease of use. This ease of use has made Python the most popular programming language in modern times. In 2024, Python officially surpassed JavaScript as the most popular language on GitHub.

Python is used in many fields like data science and machine learning, web development, scripting and automation, embedded systems, IoT, and much more.

> - Python is the main language that most data scientist and machine learning engineers currently use. Libraries like Pandas and Numpy make data analysis less tedious, while others like Tensorflow and Scikit make machine learning and working with AI models much more accessible.
> - In web development, Python frameworks like Django, FastAPI, and Flask let developers build scalable and secure backend systems with minimal effort. Many social media platforms like Instagram and Pinterest use Python on the backend.
> - Cybersecurity professionals and ethical hackers use Python to detect vulnerabilities like malware and other viruses, build automated security scans, and analyze threats.
> - Python runs well on microcomputers like the Raspberry Pi and MicroPython-compatible boards, so you can build all kinds of IoT projects like smart home devices, weather monitoring stations, and more.
> - Finally, one of Python's biggest strengths is automation. You can write simple scripts to help you with repetitive tasks like extracting data from spreadsheets, sending emails, and working with files on your local machine.
> - Libraries like Selenium and BeautifulSoup also make it easy to interact with websites, so you can scrape public data, automate tasks through a web UI, and even manage cloud deployments for your projects.

As you can see, Python is a very powerful language, and yet, it's easy to learn. From simple automation scripts to large-scale, industrial-level applications, you can use Python for just about anything.

Python is a great choice for anyone who wants to learn programming, regardless of what they choose to specialize in later.

### Variables

When naming variables in Python, there are some important rules you should keep in mind:

> - Variable names can only start with a letter or an underscore (`_`), not a number.
> - Variable names can only contain alphanumeric characters (`a-z`, `A-Z`, `0-9`) and underscores (`_`).
> - Variable names are case-sensitive — `age`, `Age`, and `AGE` are all considered unique.
> - Variable names cannot be one of Python's reserved keywords such as `if`, `class`, or `def`.

#### Data Types

Python is a *dynamically-typed language* like JavaScript, meaning you don't need to explicitly declare types for variables. The language knows what data type a variable is based on what you assign to it.

The most common data types used in Python include:

> - **Integer:** A whole number without decimals
> - **Float:** A number with a decimal point
> - **Complex:** A number with a real and imaginary part
> - **String:** A sequence of characters enclosed in single or double quotation marks
> - **Boolean:** A true or false
> - **Set:** An unordered collection of unique elements
> - **Dictionary:** A collection of key-value pairs enclosed in curly braces
> - **Tuple:** An immutable ordered collection, enclosed in brackets
> - **Range:** A sequence of numbers, often used in loops
> - **List:** An ordered collection of elements that supports different data types
> - **None:** A special value that represents the absense of a value

#### Immutable Data Types

Immutable data types can't be modified or altered once they're declared. You can point their variables at something new, which is called reassignment, but you can't change the original object itself by adding, removing, or replacing any of its elements. Examples of immutable data types in Python are *string*, *integer*, *float*, *boolean*, *tuple*, and *range*.

#### Determining Data Types

To get the data type of a variable, you can use the `type()` function:

```python
my_var_1 = 'Hello world'
print(type(my_var_1)) # <class 'str'>
```

Another way to check the type of a variable is to use the built-in `isinstance()` function, which checks if a variable matches a specific data type.

`isinstance()` takes in an object and the type you want to check it against, then returns a boolean. Here are some examples:

```python
isinstance('Hello world', str) # True
```

#### Data Hints

Although Python is dynamically typed, you can still add type hints. These are optional signals that tell other developers what the data type of a variable or function is expected to be. Here's an example:

```python
def greet(name: str, age: int) -> str:
    return f'Hello, {name}, age {age}.'

user_name: str = 'John Doe'
user_age: int = 24

print(greet(user_name, user_age)) # Hello, John Doe, age 24.
```

Note that, unlike TypeScript which enforces types at compile time, Python just uses these hints for static analysis, documentation, and editor support, not for enforcing types during runtime. This can help developers catch bugs early and improve code readability, especially in large projects.

### `print()` Function

There's a lot more to the `print` function than first meets the eye. There are four other arguments you can pass to it, so here's the full syntax of the function.

```python
print(*objects sep=' ', end='\n', file=sys.stdout, flush=False)
```

> - `objects` : The data you want to print. The `*` sign means that yu can print multiple things to the terminal by passing in multiple objects.
> - `sep` : The seperator between the obsects. This defaults to a single space character.  
> - `end` : What to print at the end of the object. This defaults to a new line character.
> - `file` : Determines where to send the output. The default is in the terminal, but it can be a file.
> - `flush` : Determines whether to show the output data right away. The default is `False`, which means Python may wait before displaying the output.

### Working with Strings

#### Multiline Strings

If you need a multi-line string, you can use triple double quotes or single quotes:

```python
my_str = """Multiline
string"""
```

#### Strings Containing Quotation Marks

If your string contains either single or double quotation marks, then you have two options:

- Use the opposite kind of quotes. That is, if your string contains single quotes, use double quotes to wrap the string, and vice versa:

    ```python
    msg = "It's a sunny day"
    quote = 'She said, "Hello World!"'
    ```

- Escape the single or double quotation mark in the string with a backslash (`\`). With this method, you can use either single or double quotation marks to wrap the string itself:

    ```python
    msg = 'It\'s a sunny day'
    quote = "She said, \"Hello!\""
    ```

#### String Concatenation

You can also combine multiple strings together with the plus (`+`) operator. This process is called string concatenation. Here's how to concatenate two strings with the plus operator:

```python
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) # Hello World
```

> But note that this only works with strings. If you try to concatenate a string with a number, you'll get a `TypeError`.

You can also use the augmented assignment operator for concatenation. This is represented by a plus and equals sign (`+=`), and performs both concatenation and assignment in one step.

#### F-Strings

F-strings start with `f` (either lowercase or uppercase) before the quotes, and allow you to embed variables or expressions inside replacement fields indicated by curly braces (`{}`). Here's an example:

```python
name = 'John Doe'
age = 26
name_and_age = f'My name is {name} and I am {age} years old'
print(name_and_age) # My name is John Doe and I am 26 years old

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}') # The sum of 5 and 10 is 15
```

#### Indexing

Now that you've learned about string concatenation and f-strings, let's look at how you can get the length of a string and work with the individual characters in a string, a process called indexing. To get the length of a string, you can use the built-in `len()` function. Here's an example:

```python
my_str = 'Hello world'
print(len(my_str))  # 11
```

Now onto indexing. Each character in a string has a position called an index. The index is zero-based, meaning that the index of the first character of a string is 0, the index of the second character is `1`, and so on. To access a character by its index, you use square brackets (`[]`) with the index of the character you want to access inside. Here are some examples:

```python
my_str = "Hello world"

print(my_str[0])  # H
print(my_str[6])  # w
```

Negative indexing is also allowed, so you can get the last character of any string with `-1`, the second-to-last character with `-2`, and so on.

#### String Slicing

Now that you're familiar with indexing, let's take things a bit further with string slicing. String slicing lets you extract a portion of a string or work with only a specific part of it. Here's the basic syntax:

```python
string[start:stop]
```

If you want to extract characters from a certain index to another, you just separate the `start` and `stop` indices with a colon:

```python
my_str = 'Hello world'
print(my_str[1:4]) # ell
```

Apart from the `start` and `stop` indices, there's also an optional `step` parameter, which is used to specify the increment between each index in the slice.

Here's the syntax for that:

```python
string[start:stop:step]
```

In the example below, the slicing starts at index `0`, stops before `11`, and extracts every second character:

```python
my_str = 'Hello world'
print(my_str[0:11:2])  # Hlowrd
```

A helpful trick you can do with the step parameter is to reverse a string by setting step to `-1`, and leaving `start` and `stop` blank:

```python
my_str = 'Hello world'
print(my_str[::-1]) # dlrow olleH
```

#### `in` Operator

It can also be helpful to check if a character or set of characters exist in a string before slicing it. To do that, Python provides the `in` operator, which returns a boolean that specifies whether the character or characters exist in the string or not.

Here are some examples:

```python
my_str = 'Hello world'

print('Hello' in my_str)  # True
print('hey' in my_str)    # False
print('hi' in my_str)    # False
print('e' in my_str)  # True
print('f' in my_str)  # False
```

### Common String Methods

Python provides a number of built-in methods that make working with strings a breeze. They include, but are not limited to, the following:

> - `upper()`: Returns a new string with all characters converted to uppercase.

```python
my_str = 'hello world'

uppercase_my_str = my_str.upper()
print(uppercase_my_str)  # HELLO WORLD
```

> - `lower()`: Returns a new string with all characters converted to lowercase.

```python
my_str = 'Hello World'

lowercase_my_str = my_str.lower()
print(lowercase_my_str)  # hello world
```

> - `strip()`: Returns a new string with the specified leading and trailing characters removed. If no argument is passed it removes leading and trailing whitespace.

```python
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str)  # "hello world"
```

> - `replace(old, new)`: Returns a new string with all occurrences of `old` replaced by `new`.

```python
my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)  # hi world
```

> - `split(separator)`: Splits a string on a specified separator into a list of strings. If no separator is specified, it splits on whitespace.

```python
my_str = 'hello world'

split_words = my_str.split()
print(split_words)  # ['hello', 'world']
```

> - `join(iterable)`: Joins elements of an iterable into a string with a separator.

```python
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)  # hello world
```

> - `startswith(prefix)`: Returns a boolean indicating if a string starts with the specified prefix.

```python
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)  # True
```

> - `endswith(suffix)`: Returns a boolean indicating if a string ends with the specified suffix.

```python
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)  # True
```

> - `find(substring)`: Returns the index of the first occurrence of substring, or -1 if it doesn't find one.

```python
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index)  # 6
```

> - `count(substring)`: Returns the number of times a substring appears in a string.

```python
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)  # 2
```

> - `capitalize()`: Returns a new string with the first character capitalized and the other characters lowercased.

```python
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str)  # Hello world
```

> - `isupper()`: Returns `True` if all letters in the string are uppercase and `False` if not.

```python
my_str = 'hello world'

is_all_upper = my_str.isupper()
print(is_all_upper)  # False
```

> - `islower()`: Returns `True` if all letters in the string are lowercase and `False` if not.

```python
my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)  # True
```

> - `title()`: Returns a new string with the first letter of each word capitalized.

```python
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)  # Hello World
```

### Working with Integers and Floats

#### Basic Arithmetic Operators

Common operators for integers and floats include:

> - Addition: `+`
> - Subtraction: `-`
> - Multiplication: `*`
> - Division: `/`

#### Combining Integers and Floats

If you add an integer and a float, the result is automatically converted to a float:

```python
my_int = 56
my_float = 5.4

sum_int_and_float = my_int + my_float

print(sum_int_and_float) # 61.4
print(type(sum_int_and_float)) # <class 'float'>
```

This is true for other basic arithmetic operations, too, like subtraction, multiplication, and division. If you mix integers and floats, Python will return a float as the result.

You can also perform more complex arithmetic calculations such as getting the remainder of two numbers with the modulo operator, floor division, and exponentiation with both integers and floats.

#### Other Operators

The modulo operator (`%`) returns the remainder when the value on the left is divided by the value on the right:

```python
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

mod_ints = my_int_1 % my_int_2
mod_floats = my_float_2 % my_float_1

print('Integer Modulus:', mod_ints) # Integer Modulus: 8
print('Float Modulus:', mod_floats) # Float Modulus: 1.1999999999999993
```

Floor division divides two numbers and rounds down the result to the nearest whole number. This is done with the double forward slash operator (`//`):

```python
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

floor_div_ints = my_int_1 // my_int_2
floor_div_floats = my_float_2 // my_float_1

print('Integer Floor Division:', floor_div_ints) # Integer Floor Division: 4
print('Float Floor Division:', floor_div_floats) # Float Floor Division: 2.0
```

Exponentiation raises a number to the power of another, and is done with the double asterisk operator (`**`):

```python
my_int_1 = 56
my_int_2 = 12

my_float_1 = 5.4
my_float_2 = 12.0

exp_ints = my_int_1 ** my_int_2
exp_floats = my_float_1 ** my_float_2

print('Integer Exponentiation:', exp_ints) # Integer Exponentiation: 951166013805414055936
print('Float Exponentiation:',  exp_floats) # Float Exponentiation: 614787626.1765089
```

#### Converting Between Integers and Floats

Python also provides built-in functions for converting either numeric data or strings into integers or floats. You can use the `float()` function to convert an integer into a float by adding a decimal point of `0` to the integer.

And you can use the `int()` function to convert a float into an integer, which removes the decimal point and everything after it from the float you pass it.

Also, you can use the same built-in functions to convert a string into either a float or integer:

```python
my_str_int = '45'
my_str_float = '7.8'

converted_int = int(my_str_int)
converted_float = float(my_str_float)

print(converted_int, type(converted_int))  # 45 <class 'int'>
print(converted_float, type(converted_float))  # 7.8 <class 'float'>
```

#### Common Methods

Here are some other methods Python provides for working with integers and floats:

> - `round()`: Rounds a number to the specified number of decimal places. By default this function rounds to the nearest integer, and returns a whole number with no decimal places:

```python
my_int_1 = 4.798
my_int_2 = 4.253

rounded_int_1 = round(my_int_1)
rounded_int_2 = round(my_int_2, 1)

print(rounded_int_1) # 5
print(rounded_int_2) # 4.3
abs(): returns the absolute value of a number,
num = -15

absolute_value = abs(num)
print(absolute_value) # 15
```

> - `bin()`: converts an integer to its binary representation as a string.
> - `oct()`: converts an integer to its octal representation as a string.
> - `hex()`: converts an integer to its hexadecimal representation as a string.

```python
my_int = 56

binary_representation = bin(my_int)
print(binary_representation)  # 0b111000

octal_representation = oct(my_int)
print(octal_representation) # 0o70

hex_representation = hex(my_int)
print(hex_representation) # 0x38
```

>- `pow()`: raises a number to the power of another or performs modular exponentiation.

```python
result_1 = pow(2, 3)  # Equivalent to 2 ** 3
print(result_1)  # 8

result_2 = pow(2, 3, 5)  # (2 ** 3) % 5
print(result_2)  # 3
```

### Augmented Assignments

#### Introduction and Syntax

Augmented assignment combines a binary operation with an assignment in one step. It takes a variable, applies an operation to it with another value, and stores the result back into the same variable.

If you're familiar with a language like JavaScript, you've probably heard of the addition assignment operator (`+=`) or subtraction assignment (`-=`), and others. Those exist in Python, too. The only difference is that they're referred to as augmented assignments.

The basic syntax of an augmented assignment looks like this:

```python
variable <operator>= value
```

Which is a more efficient way of doing this:

```python
variable = variable <operator> value
```

For example, here's an example of using augmented assignment to add `5` to an existing variable:

```python
my_var = 10
my_var += 5

print(my_var) # 15
```

The advantage of augmented assignment is that it provides a concise and readable way to update a variable value without repeating the variable name. In turn, this reduces redundancy and potential errors that might arise from a typo or something similar.

#### Common Augmented Assignment Operators

Every operator can use an augmented assignment. We've looked at the addition assignment operator (`+=`), so let's look at others.

The subtraction assignment operator (`-=`) subtracts the right operand from the left variable and stores the difference in the left variable:

```python
count = 14
count -= 3

print(count) # 11
```

The multiplication assignment operator (`*=`) multiplies the left variable by the right operand and stores the product back in the left variable:

```python
product = 65
product *= 7

print(product) # 455
```

The division assignment operator (`/=`) divides the left variable by the right and stores the result back in the left variable:

```python
price = 100
price /= 4

print(price) # 25.0
```

The floor division operator (`//=`) floor‑divides the left variable by the right and stores the result back in the left variable:

```python
total_pages = 23
total_pages //= 5

print(total_pages) # 4
```

The modulus assignment operator (`%=`) computes the remainder of the left variable divided by the right and stores it back in the left variable:

```python
bits = 35
bits %= 2

print(bits) # 1
```

The exponentiation assignment operator (`**=`) raises the left variable to the power of the right and stores the result back in the left variable:

```python
power = 2
power **= 3

print(power) # 8
```

There are other augmented assignment operators too, like those for bitwise operators. They include `&=`, `^=`, `>>=`, and `<<=`.

### Functions

(WIP)

## Loops and Sequences

## Dictionaries and Sets

## Error Handling

## Classes and Objects

## Object-Oriented Programming (OOP)

## Linear Data Structures

## Algorithms

## Graphs and Trees

## Dynamic Programming

## References

*Certified Full Stack Developer Curriculum*. freecodecamp.org. (n.d.). <https://www.freecodecamp.org/learn/full-stack-developer/>
