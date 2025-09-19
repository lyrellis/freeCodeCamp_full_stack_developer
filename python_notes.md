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
        1. Code Blocks
        2. Parameters
        3. Return
        4. Decorators
    9. What is Scope in Python and How Doues it Work?
        1. Local Scope
        2. Enclosing Scope
        3. Global Scope
        4. Built-In Scope
    10. Conditional Statements and Logical Operators
        1. `if`, `else`, and `elif` Statements
    11. Truthy and Falsy Values, Boolean Operators, and Short-Circuiting
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

Functions are reusable pieces of code that run when you call them. Many programming languages come with built-in functions that make it easier to get started. Python is no exception, and we've already covered some built-in functions like `print()` in previous lectures.

Another helpful built-in function is `input()`, which lets you prompt the user for input:

```python
name = input('What is your name?') # User types "Kolade" and presses Enter  
print('Hello', name) # Output: Hello Kolade
```

On the other hand, int() converts a number, boolean, and a numeric string into an integer:

```python
print(int(3.14)) # 3
print(int('42')) # 42
print(int(True)) # 1
print(int(False)) # 0
```

Here's an example of a custom function named hello that prints the string Hello World to the terminal:

```python
def hello():
    print('Hello World')
```

To run the function, you need to call it with its name followed by a pair of parentheses:

```python
hello() # Hello World
```

#### Code Blocks

> Notice the indentation before `print('Hello World')`. The level of indentation defines a **"code block"** in Python, which is a group of statements that belong together.

While other programming languages use characters like curly braces to define code blocks, and just use indentation for readability, in Python, code blocks are determined by indentation.

Though you can use either two or four spaces to determine each level of indentation, the Python style guide recommends using four spaces.

Blocks are also found in loops and conditionals, which you'll learn about in future lectures.

#### Parameters

Here's another simple function that prints the sum of two numbers to the terminal:

```python
def calculate_sum(a, b):
    print(a + b)
```

You can see that our function, `calculate_sum`, has `a` and `b` in its parentheses, separated by a comma. Those are called parameters. Think of parameters as placeholder variables that act as "slots" for the values you pass into functions when you call them.

To use the parameters, you have to pass in "arguments". Arguments are the values you pass to a function when you call it.

Here's how to call the `calculate_sum` function to sum together the numbers `3` and `1`:

```python
calculate_sum(3, 1) # 4
```

If you call the function without the correct number of arguments, you'll get a `TypeError`:

```python
calculate_sum()

# TypeError: calculate_sum() missing 2 required positional arguments: 'a' and 'b'
```

#### Return

Functions also use a special `return` keyword to exit the function and return a value. If you don't explicitly use `return`, Python will return None by default.

Here's an example:

```python
def calculate_sum(a, b):
    print(a + b)

my_sum = calculate_sum(3, 1) # 4
print(my_sum) # None
```

You can see that the `calculate_sum` function prints the sum of a and b, but it doesn't return anything explicitly. So when we assign its result to `my_sum`, the value is actually `None`. To fix that, you can use the `return` keyword to send back the result:

```python
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(3, 1)
print(my_sum) # 4
```

Now, `calculate_sum` returns the sum of `a` and `b`, which gets stored in `my_sum`.

#### Decorators

Decorators are a special kind of function in Python. They are like wrappers for other functions, so they take another function as an argument. With decorators, you get to add extra functionality to a function without modifying its original code. Here's an example of how to use a decorator:

```python
def say_hello():
   name = input('What is your name? ')
   return 'Hello ' + name

def uppercase_decorator(func):
   def wrapper():
       original_func = func()
       modified_func = original_func.upper()
       return modified_func
   return wrapper

say_hello_res = uppercase_decorator(say_hello)

print(say_hello_res())
```

### What is Scope in Python and How Does it Work?

In Python, scope determines the point at which you can access a variable. It's what controls the lifetime of a variable and how it is resolved in different parts of the code.

To correctly determine scope, Python follows the LEGB rule, which stands for the following:

> - **Local scope (L)**: Variables defined in functions or classes.
> - **Enclosing scope (E)**: Variables defined in enclosing or nested functions.
> - **Global scope (G)**: Variables defined at the top level of the module or file.
> - **Built-in scope (B)**: Reserved names in Python for predefined functions, modules, keywords, and objects.

Python uses the LEGB rule to resolve the scope of the variables in your program. We'll dive into each of these rules so you get a better understanding of the process.

#### Local Scope

Local scope means that a variable declared inside a function or class can only be accessed within that function or class.

Here's an example:

```python
def my_func():
    my_var = 10
    print(my_var)
```

In this case, the `my_func` function has its own scope which cannot be accessed from outside the function. Calling `my_func` will output `10`, but printing `my_var` outside the function will lead to a `NameError`.

#### Enclosing Scope

Enclosing scope means that a function that's nested inside another function can access the variables of the function it's nested within.

For example:

```python
def outer_func():
    msg = 'Hello there!'

    def inner_func():
        print(msg)

    inner_func()

outer_func() # Hello there!
```

In this example, the inner function, `inner_func`, can freely access the `msg` variable defined in the outer function, `outer_func`. However, note that outer functions cannot access variables defined within any nested functions:

```python
def outer_func():
    msg = 'Hello there!'
    print(res)

    def inner_func():
        res = 'How are you?'
        print(msg)

    inner_func()

outer_func() # NameError: name 'res' is not defined
```

One solution is to initialize `res` as an empty string in the enclosing scope, which is within `outer_func`. Then within `inner_func`, make `res` a non-local variable with the `nonlocal` keyword:

```python
def outer_func():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()

    inner_func()
    print(res)  # Now res is accessible and modified

outer_func()

# Output:
# Hello there!
# How are you?
```

#### Global Scope

Global scope refers to variables that are declared outside any functions or classes which can be accessed from anywhere in the program. Here, `my_var` can be accessed anywhere, even inside a function it's not defined in:

```python
my_var = 100

def show_var():
    print(my_var)

show_var() # 100
print(my_var) # 100
```

And if you want to make a locally scoped variable defined inside a function globally accessible, you can use the `global` keyword:

```python
my_var_1 = 7

def show_vars():
    global my_var_2
    my_var_2 = 10
    print(my_var_1)
    print(my_var_2)

show_vars() # 7 10

# my_var_2 is now a global variable and can be accessed anywhere in the program
print(my_var_2) # 10
```

You can also use the `global` keyword to modify a global variable:

```python
my_var = 10  # A global variable

def change_var():
    global my_var  # Allows modification of a global variable
    my_var = 20

change_var()

print(my_var)  # my_var is now modified globally to 20
```

#### Built-In Scope

Finally, built-in scope refers to all of Python's built-in functions, modules, and keywords, and are available anywhere in your program:

```python
print(str(45)) # '45'
print(type(3.14)) # <class 'float'>
print(isinstance(3, str)) # False
```

### Conditional Statements and Logical Operators

Conditional statements, or conditionals, let you control the flow of your program based on whether certain conditions are true or false.

But before we get into all that, let's go over the basic building blocks of conditional statements, starting with comparison operators. Comparison operators are operators that let you compare two or more values, and return a boolean value.

Here's a table with the comparison operators in Python:

| Operator | Name | Description |
| --- | --- | --- |
| `==` | Equal | Checks if two values are equal |
| `!=` | Not equal | Checks if two values are not equal |
| `>` |Greater than | Checks if the value on the left is greater than the value on the right |
| `<` | Less than | Checks if the value on the left is less than the value on the right |
| `>=` | Greater than or equal | Checks if the value on the left is greater than or equal to the value on the right |
| `<=` | Less than or equal | Checks if the value on the left is less than or equal to the value on the right |

Here are some of those expressions that evaluate to True or False:

```python
print(3 > 4) # False
print(3 < 4) # True
print(3 == 4) # False
print(4 == 4) # True
print(3 != 4) # True
print(3 >= 4) # False
print(3 <= 4) # True
```

These operators can be used in conditionals to compare values and run certain code based on whether the conditional evaluates to `True` or `False`.

#### `if`, `elif`, and `else` Statements

In Python, the most basic conditional is the if statement. Here's the basic syntax:

```python
if condition:
    # Code to execute if condition is True
```

> - `if` statements start with the `if` keyword.
> - `condition` is an expression that evaluates to True of False, followed by a colon (`:`).
> - The indentation specifies the block of code within the body of the `if` statement.

The `else` clause runs when the `if` condition is false. Here's the syntax for an `if…else` statement:

```python
if condition:
   # Code to execute if condition is True
else:
   # Code to execute if condition is False
```

There might be situations in which you want to account for multiple conditions. To do that, Python lets you extend your `if` statement with the `elif` (else if) keyword.

Here's the syntax:

```python
if condition:
   # Code to execute if condition is True
elif condition2:
   # Code to execute if condition2 is True
else:
   # Code to execute if all conditions are False
```

> Note that you can use as many `elif` statements as you want:

```python
age = 2

if age >= 65:
    print('You are a senior citizen')
elif age >= 30:
    print('You are an adult in your prime')
elif age >= 18:
    print('You are a young adult')
elif age >= 13:
    print('You are a teenager')
elif age >= 3:
    print('You are a young child')
else:
    print('You are a toddler or an infant') # You are a toddler or an infant
```

### Truthy and Falsy Values, Boolean Operators, and Short-Circuiting

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
