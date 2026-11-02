# <Topic>   (lecture / lab / date)
Conditionals, if elif else match case Lecture 1

## The idea in one sentence
Explore programs that use conditionals and how different conditionals behave

## How it works
If parameter is condition then print outcome

Here is an example

x = int(input("what is the value of x? "))
y = int(input("what is the value of y? "))
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")


## Why it matters for security
Someone can rename malware.exe to holiday.png.
Safer systems use conditionals to  check the content of the file, not only its name, and they send a strict Content-Type header with X-Content-Type-Options: nosniff so the browser doesn’t guess.

## What confused me
When and how to use match and case

## Questions I still have
What scenario could I not use if and elif conditionals instead of match and case?

## Quiz me
(3 questions I could answer in a week's time)
1. Write a simple program using if elif and else
2. Identify and explain a boolean
3. Why must you indent conditionals

## Notes
== - eqaul to not assignment
if then is the key part of conditionals
boolean - an expression that can only be true or false
elif - else if , if an earlier answer is reach this stops multiple further conditionals being asked if the answer is already reached
else - is final conclusion by deduction
indentation must be used for conditionals
and & or - works as natural language
ALWAYS THINK ABOUT HOW TO SHORTEN CODE
% - is not the same percentage it means remainder
.strip() - removes the spaces at the end of string input

input normalisation, and it’s a core security principle. Attackers exploit differences between what a program checks and what it uses. Examples: admin versus Admin, a trailing space in a username, or hidden Unicode lookalike characters. Defenders normalise first, then validate, and do it in one place.

A file name is whatever the uploader says it is. Someone can rename malware.exe to holiday.png.
Safer systems use conditionals to  check the content of the file, not only its name, and they send a strict Content-Type header with X-Content-Type-Options: nosniff so the browser doesn’t guess.
That’s why FORGE blocks SVG uploads. An SVG is image/svg+xml, but it can carry JavaScript, so treating it as “just an image” is dangerous