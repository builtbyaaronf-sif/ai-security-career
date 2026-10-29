# <Topic>   (lecture / lab / date)
Understanding basics. Functions, variables, and different methods.

## The idea in one sentence
Basic hello world and what is your name programs using different functions. Created and ran the program hello.py 

## How it works
name = input ("What is your name")
print (f"Hello, {name}")

```python
# example
```

## Why it matters for security
n/a

## What confused me
none

## Questions I still have
- more clarity on defining and using your own functions

## Quiz me
(3 questions I could answer in a week's time)
1.What is a return value?
2.Can you write a simple program involving integers?
3.What's the difference between integers and floats

## Other notes
CLI - Command Line Interface
Functions - action or verb within program (e.g print)
Parameter - (name)
argument - value within a function e.g ("aaron")
Functions have side effects but not negative
return values - belongs to A function that hands a value back to the code that called it
variable - container of value
input() - returns Whatever the user typed, always as a string
= - assignment operator, copies from right to left
"" - anything inside quote marks is string
if function is using a variable no quote marks, it only accepts variables as string (text)
str - string
read documentation for program languages
parameters are akin to arguments
\n - new line
python runs in canonical order top to bottom as in a normal conversation
f at beginning of string for format string {}
method - function built in to a value
int-integer and can be used to convert strings into numbers as long as the string is defined as a number
can nest one function with another - works like brackets in math
float is number with decimal
def - define (use to create your own functions)
** - to the power of
q10 of quiz 1 - this was a question related to security

The MemoryError. m was the text "84" and c ** 2 is 90 quadrillion, so Python tried to repeat "84" 90 quadrillion times and ran out of memory. Security link: when user input controls how much work a program does, an attacker can crash or exhaust it. That’s a denial of service weakness (OWASP “unbounded consumption”), the same idea as the cost abuse risk in FORGE’s AI endpoints. The defence is to check the type and enforce limits on anything a user supplies.