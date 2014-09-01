# Notes from [Pluralsight - Python Fundamentals](http://pluralsight.com/training/Courses/Description/python-fundamentals)

*   [Python uses Duck Typing](#python-uses-duck-typing)
*   [REPL](#repl)
    *   [Underscore refers to the most recent calculation](#underscore)
    *   [How to Exit the REPL](#exit-repl)
*   [Style](#style)
*   [Help](#help)
*   [Import](#import)
*   [Types](#types)
*   [Loops and Conditionals](#loops-and-conditionals)


## Python uses Duck Typing

From [Wikipedia](http://en.wikipedia.org/wiki/Duck_typing):

*In computer programming with object-oriented programming languages, duck typing is a style of typing in which an object's methods and properties determine the valid semantics, rather than its inheritance from a particular class or implementation of an explicit interface. The name of the concept refers to the duck test, attributed to James Whitcomb Riley (see history below), which may be phrased as follows:*

*When I see a bird that walks like a duck and swims like a duck and quacks like a duck, I call that bird a duck.[1]*


## REPL

### Underscore

In the REPL, an underscore refers to the most recent calculation.  Here's an example:
```python
>>> x = 5
>>> x * 2
10
>>> _ + 3
13
```
### Exit REPL

How to exit the REPL:
- On Windows ```Ctrl+Z```
- On Mac OS X or Linux ```Ctrl+D```
- On all ```quit()```
- NOTE: On Mac OS X or Linux ```Ctrl+Z``` will suspend the python process, use ```fg``` to bring it back

## Style

Python is coding as Guido ~~intended~~ **indented** it.
- [PEP 8 -- Style Guide for Python Code](http://legacy.python.org/dev/peps/pep-0008/)
- [PEP 20 -- The Zen of Python](http://legacy.python.org/dev/peps/pep-0020/)

## Help

- At the REPL, type ```help```
- ```help()``` to get interactive help ```q``` to quit
- ```help(math)``` to get help on module math
- ```help(math.factorial)``` to get help on the factorial function in module math
- ```dir(math)``` list of objects in math module
- ```dir()``` return the names in the current scope

## Import

- ```import math```
- ```from math import factorial```
- ```from math import factorial as fac```

## Types
<ul style="list-style-type:square">
  <li>
    <dl>
      <dt>int</dt>
      <dd>- unlimited precision signed integer</dd>
    </dl>
  </li>
  <li>
    <dl>
      <dt>float</dt>
      <dd>- IEEE-754 double precision (64-bit)</dd>
      <dd>- 53 bits of binary precision</dd>
      <dd>- 15 to 16 bits of decimal precision</dd>
    </dl>
  </li>
  <li>
    <dl>
      <dt>Null / None</dt>
      <dd>- The sole value of NoneType</dd>
      <dd>- Often used to represent the absence of a value.</dd>
      <dd>- Not displayed by the REPL</dd>
    </dl>
  </li>
  <li>
    <dl>
      <dt>bool</dt>
      <dd>- Boolean logical value</dd>
      <dd>- Either <code>True</code> or <code>False</code></dd>
    </dl>
  </li>
</ul>

```python
>>> 0b10 #binary prefix 0b
2
>>> 0o10 #octal prefix 0o
8
>>> 0x10 #hexidecimal prefix
16
>>> int(3.5) #int constructor
3
>>> int("496") #convert string to int
496
>>> int("10000", 3) #base 3 to decimal, here 3 ** 4 = 81
81
>>> None #REPL doesn't return anything
>>> a = None
>>> a is None
True
>>> bool(0) #zero is false
False
>>> bool(42) #all non-zero, non-empty values are true
True
>>> bool([]) #empty list is false
False
>>> bool("") #empty string is false
False
>>> bool("False") #watch out!
True
```

## Loops and Conditionals

- [if, elif, else](https://github.com/dviar2718/DanWeb/blob/gh-pages/interests/python/sample_code/conditional.py)
- [while count down](https://github.com/dviar2718/DanWeb/blob/gh-pages/interests/python/sample_code/while_count_down.py)
- [while to run script more than once](https://github.com/dviar2718/DanWeb/blob/gh-pages/interests/python/sample_code/while_sum_digits.py)
- You can break out of an infinite loop in the REPL with <code>Ctrl+C</code>
- The <code>break</code> keyword terminates the innermost loop, transferring execution to the first statement after the loop.  Here is an [example](https://github.com/dviar2718/DanWeb/blob/gh-pages/interests/python/sample_code/while_with_break.py).
