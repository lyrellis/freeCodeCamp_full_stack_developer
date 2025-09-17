# Python Notes

> Notes from the Python curriculum within the freeCodeCamp Full Stack Developer curriculum

The source material can be found here:

https://www.freecodecamp.org/learn/full-stack-developer

## Basics

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

**Immutable** data types can't be modified or altered once they're declared. You can point their variables at something new, which is called reassignment, but you can't change the original object itself by adding, removing, or replacing any of its elements. Examples of immutable data types in Python are *string*, *integer*, *float*, *boolean*, *tuple*, and *range*.

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

Although Python is dynamically typed, you can still add type hints. These are optional signals that tell other developers what the data type of a variable or function is expected to be. Here's an example:

```python
def greet(name: str, age: int) -> str:
    return f'Hello, {name}, age {age}.'

user_name: str = 'John Doe'
user_age: int = 24

print(greet(user_name, user_age)) # Hello, John Doe, age 24.
```

Note that, unlike TypeScript which enforces types at compile time, Python just uses these hints for static analysis, documentation, and editor support, not for enforcing types during runtime. This can help developers catch bugs early and improve code readability, especially in large projects.

### Print Function

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



## Loops and Sequences

## Dictionaries and Sets

## Error Handling

## Classes and Objects

## Object-Oriented Programmong (OOP)

## Linear Data Structures

## Algorithms

## Graphs and Trees

## Dynamic Programming

# References

*Certified Full Stack Developer Curriculum*. freecodecamp.org. (n.d.). https://www.freecodecamp.org/learn/full-stack-developer/ 