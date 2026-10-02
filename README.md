# Data Types, Variables, Operators, and Functions

Write small functions using Python's operators, variables, and f-strings.

**Practicing:** data types, operators, variables, functions, `return`, scope

- [AI Use on This Assignment](#ai-use-on-this-assignment)
- [Before We Begin](#before-we-begin)
  - [What's In An Assignment?](#whats-in-an-assignment)
  - [Predict Before You Run](#predict-before-you-run)
- [Setup](#setup)
- [From Scratch](#from-scratch)
  - [Question 1: `calculate_area`](#question-1-calculate_area)
  - [Question 2: `is_even`](#question-2-is_even)
  - [Question 3: `convert_to_fahrenheit`](#question-3-convert_to_fahrenheit)
  - [Question 4: `is_valid_age`](#question-4-is_valid_age)
  - [Question 5: `create_greeting`](#question-5-create_greeting)
- [Modify](#modify)
  - [Question 6: `return` vs `print`](#question-6-return-vs-print)
  - [Question 7: `greet`](#question-7-greet)
- [Debug](#debug)
  - [Question 8: Fix our mess of a function](#question-8-fix-our-mess-of-a-function)
- [Resources](#resources)
- [Submitting](#submitting)
- [Good luck!](#good-luck)

## AI Use on This Assignment

Use whichever mode matches where you are with this material. Both are fine,
and most people move between them as a concept clicks.

**Tutor mode.** The AI explains, questions, quizzes, and critiques, and you
write every line you submit. For this assignment that means asking it what an
f-string does, or having it quiz you on operators until you can predict what
your own code will do. Ask it a hundred questions — that is the whole point.
What you do not do is ask it for the function. Paste this at the start of a
chat and it will hold for the rest of the conversation:

> You are acting as a tutor. Your job is to explain what this coding question
> is asking, clarify confusing wording, and highlight the relevant concepts I
> need to know — but do not provide the full solution or code that directly
> answers the question. Instead, rephrase the problem in simpler terms,
> identify what is being tested, and suggest what steps or thought processes
> might help. Ask me guiding questions to make sure I am thinking critically.
> Do not write the final function, algorithm, or code implementation.

**Implementer mode.** You write a specification first, the AI writes code from
it, and then you verify that code line by line. For this assignment your spec
has to give each function's inputs, its return value, and one example. If what
comes back does more than you asked for, reject it — over-delivery is a
defect, and catching it is part of the job.

You own every line either way, and you will be asked to explain it.

## Before We Begin

Welcome to your first Python assignment! Before starting, we are going to go
over a few important things about assignments at Marcy.

### What's In An Assignment?

Assignments have three kinds of coding question.

- **From Scratch**: the bulk of the assignment. It tests your ability to look
  at a blank page and create something. Usually there is a `from_scratch.py`
  file, but not always.
- **Modify**: given some existing code, can you change or improve it? Nothing
  is broken here. The code works and you are making it better.
- **Debug**: we'll be real with you, most of this job is fixing something
  broken. Here you get code that does not work, and you get it working by
  *mostly* relying on reading the tests.

This assignment has all three. Not every assignment will. Read the whole
README and use the tests to confirm you have finished.

### Predict Before You Run

`src/playground.py` is yours to experiment in. Nothing in it is graded, so
print whatever you like, and run it with `python3 src/playground.py`.

It opens with five lines whose results surprise most people the first time.
Predict each one before you run the file, then see which predictions were
wrong. A wrong prediction is the most useful thing you will find all week,
because it points at a rule you did not know you were missing.

## Setup

Work in `development/mod-1`. Make a draft branch before you start.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git checkout -b draft
```

Run `pytest` for everything, or `pytest -k is_even` for one question.

Every time you push, GitHub runs the tests for you and reports your score. Open
the **Actions** tab in your repository to see it. 75% of tests passing counts
as complete. Submit at that point even if it is not perfect. Treat submitting
as a checkpoint rather than a finish line, and come back to improve it.

## From Scratch

Okay, now let's get started! Write your solutions in `src/from_scratch.py`.

### Question 1: `calculate_area`

Write a function `calculate_area` that takes two parameters: a number `width`
and a number `height`. It should return the area of a rectangle.

```python
calculate_area(5, 3)
# 15
calculate_area(10, 7)
# 70
```

### Question 2: `is_even`

Write a function `is_even` that takes one parameter: a number. It should
return `True` if the number is even, and `False` if the number is odd.

```python
is_even(2)
# True
is_even(3)
# False
is_even(0)
# True
```

The `%` operator gives you the remainder after division. An even number
divides by 2 with nothing left over, so its remainder is 0.

### Question 3: `convert_to_fahrenheit`

Write a function `convert_to_fahrenheit` that takes one parameter: a number
`celsius`. It should return the temperature converted to Fahrenheit using the
formula `(celsius * 9 / 5) + 32`.

```python
convert_to_fahrenheit(0)
# 32
convert_to_fahrenheit(100)
# 212
convert_to_fahrenheit(-40)
# -40
```

Python multiplies and divides before it adds, so `celsius * 9 / 5 + 32` gives
the same answer as the version with parentheses. Keep the parentheses anyway.
They tell the next reader which part is the conversion and which part is the
offset, and that reader is usually you in three weeks.

That `-40` is not a typo. It is the one temperature where both scales agree,
which is a genuinely great piece of trivia.

### Question 4: `is_valid_age`

Write a function `is_valid_age` that takes one parameter: a number `age`. It
should return `True` if the age is from 0 to 120, and `False` otherwise. Both
0 and 120 count as valid.

```python
is_valid_age(0)
# True
is_valid_age(120)
# True
is_valid_age(121)
# False
is_valid_age(-1)
# False
```

Python lets you chain comparisons, so you can write this the way you would say
it out loud: `0 <= age <= 120`. How about that?

### Question 5: `create_greeting`

Write a function `create_greeting` that takes one parameter: a string `name`.
It should return a greeting string in the format `"Hello, [name]!"`.

Do not include the `[]` characters. They are there to show you where the
variable goes.

```python
create_greeting("Alice")
# "Hello, Alice!"
create_greeting("")
# "Hello, !"
```

An **f-string** is a string with an `f` before the opening quote. Any
expression inside `{}` is evaluated and its value is placed into the text:

```python
name = "Zo"
f"Hello, {name}!"   # "Hello, Zo!"
```

An empty name still has to produce a valid string, comma and all.

## Modify

### Question 6: `return` vs `print`

Make each of the four functions in `src/return_vs_print.py` return its result.

Right now each one prints its answer and stops. A function that does not reach
a `return` gives back `None`, so `add(2, 3)` prints the right message and
evaluates to `None`. That breaks the moment you try to use the answer:
`add(add(1, 2), 3)` passes `None` into `add`, and adding `None` to a number
raises a `TypeError`.

Keep the printed messages exactly as they are. The tests check that the
printing still works and that the value comes back.

```python
add(2, 3)
# prints "The sum of 2 and 3 is 5", returns 5
add(add(1, 2), 3)
# 6
```

`print` shows a value to a person. `return` hands a value back to your code.
A function that only prints cannot be used by another function, which is most
of what functions are for.

### Question 7: `greet`

Modify `greet` in `src/default_args.py` so that only `name` is required.

Right now `greet` demands all three arguments, so `greet("Alice")` raises a
`TypeError` for the two that are missing. Give `greeting` a **default value**
of `"Hello"` and `punctuation` a default value of `"!"`. A parameter with a
default value becomes optional, because Python uses the default whenever the
caller leaves that argument out.

```python
greet("Alice")
# "Hello, Alice!"
greet("Bob", "Hi")
# "Hi, Bob!"
greet("Dev", punctuation=".")
# "Hello, Dev."
greet(greeting="Yo", name="Eve")
# "Yo, Eve!"
```

Look at those last two calls. Naming your arguments lets them arrive in any
order you like.

## Debug

### Question 8: Fix our mess of a function

Inside `src/bad_scope.py` we have a doozy of a function. It is reaching for a
global, gluing strings together with `+`, and trying (poorly) to use a variable
before it has actually made it. Ugh.

Right now it does not even run:

```text
UnboundLocalError: cannot access local variable 'their_name'
where it is not associated with a value
```

Make it so it prints:

```text
Hello Zo, are you feeling happy today?
Oh no, I'm sorry you're feeling sad today.
```

Fix the function so:

- `global` is not used
- every name is assigned before it is read
- f-strings are used instead of `+` concatenation
- in the end you will have 4 variable assignments: 3 initial ones and 1
  reassignment

That first error is the interesting one. Python decides a name belongs to the
**local scope** of a function if the function assigns to it anywhere, and it
makes that decision before running a single line. `their_name` is assigned
further down, so Python treats it as local throughout, and reading it on the
first line finds a local variable that has no value yet. Where does the
assignment need to go?

## Resources

- [W3Schools: Python Operators](https://www.w3schools.com/python/python_operators.asp)
  — short, with examples of every operator
- [W3Schools: Python Functions](https://www.w3schools.com/python/python_functions.asp)
- [W3Schools: f-strings](https://www.w3schools.com/python/python_string_formatting.asp)

## Submitting

```sh
git add -A
git commit -m "your message"
git push
```

Pushing runs the tests on GitHub. Check the **Actions** tab for your score,
then open a pull request to your instructor for feedback.

## Good luck!

This is the foundation everything else sits on. Take your time with it, and
you can do this!
