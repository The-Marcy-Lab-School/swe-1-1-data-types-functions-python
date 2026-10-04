# Data Types, Variables, Operators, and Functions

Write small functions using Python's operators, variables, and f-strings.

**Practicing:** data types, operators, variables, functions, `return`, default arguments, scope

- [AI Use on This Assignment](#ai-use-on-this-assignment)
- [Before We Begin](#before-we-begin)
  - [What's In An Assignment?](#whats-in-an-assignment)
  - [Predict Before You Run](#predict-before-you-run)
- [Setup](#setup)
  - [Testing](#testing)
- [From Scratch](#from-scratch)
  - [Question 1: `calculate_area`](#question-1-calculate_area)
  - [Question 2: `is_even`](#question-2-is_even)
  - [Question 3: `convert_to_fahrenheit`](#question-3-convert_to_fahrenheit)
  - [Question 4: `is_valid_age`](#question-4-is_valid_age)
  - [Question 5: `create_greeting`](#question-5-create_greeting)
  - [Question 6: `minutes_to_clock`](#question-6-minutes_to_clock)
  - [Question 7: `is_leap_year`](#question-7-is_leap_year)
  - [Question 8: `make_banner`](#question-8-make_banner)
  - [Question 9: `calculate_room_cost`](#question-9-calculate_room_cost)
  - [Question 10: `is_vowel`](#question-10-is_vowel)
- [Modify](#modify)
  - [Question 11: `return` vs `print`](#question-11-return-vs-print)
  - [Question 12: `greet`](#question-12-greet)
- [Debug](#debug)
  - [Question 13: Fix our mess of a function](#question-13-fix-our-mess-of-a-function)
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
  _mostly_ relying on reading the tests.

This assignment has all three. Not every assignment will. Read the whole
README and use the tests to confirm you have finished.

### Predict Before You Run

`src/playground.py` is yours to experiment in. Nothing in it is graded, so
print whatever you like, and run it with `python3 src/playground.py`.

It opens with five lines whose results surprise most people the first time.
Predict each one before you run the file, then see which predictions were
wrong. A wrong prediction may the most useful learning moment,
because it reveals a rule you didn't know you misunderstood.

## Setup

Work in `development/mod-1` then use the commands below to get started. You will first make a virtual environment and install the required packages that enable testing for this assignment (`pytest`). You will learn more about virtual environments in lesson 1.9 but for now you just need to remember to run these commands.

Make a `draft` branch before you start.

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
git checkout -b draft
```

The first line makes a `.venv` folder to hold this assignment's packages. The
second turns it on, which you do again in every new terminal you open. The
third installs pytest into it, and the fourth puts you on a draft branch.

### Testing

There are automated tests provided for you in the `tests/` directory that will help you verify that your functions are behaving as expected. You may read these test files but **you are not allowed to modify them**. You will learn more about `pytest` in lesson 1.9 but for now, you can just use the commands below to run them:

```sh
pytest
pytest -k is_even
```

`pytest` on its own runs everything. Adding `-k is_even` runs only the tests
whose name contains `is_even`, which is how you work on one question at a time.

Additionally, every time you push, GitHub runs the tests for you and reports your score. Open
the **Actions** tab in your repository to see it.

75% of tests passing counts
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

Hint: The `%` operator gives you the remainder after division:

```py
17 % 5
# 2
```

What remainder does an even number leave when you divide it by 2?

### Question 3: `convert_to_fahrenheit`

Write a function `convert_to_fahrenheit` that takes one parameter: a number
`celsius`. It should return the temperature converted to Fahrenheit using the
formula `(celsius * 9 / 5) + 32`.

```python
convert_to_fahrenheit(0)
# 32.0
convert_to_fahrenheit(100)
# 212.0
convert_to_fahrenheit(-40)
# -40.0
```

Consider this: why are the results floats if the inputs are integers? Ask an instructor to explain this if
you are unable to find an answer on your own.

Fun fact: That `-40` is not a typo. It is the one temperature where both scales agree,
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

Hint: Python lets you chain comparisons, so you can write this the way you would say
it out loud:

```py
valueA < valueB < valueC
```

instead of writing separate statements and joining them with `and`:

```py
valueA < valueB and valueB < valueC
```

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

Note that an empty name still has to produce a valid string, comma and all.

Hint: An **f-string** is a string with an `f` before the opening quote. Any
expression inside `{}` is evaluated and its value is placed into the text:

```python
age = 25
years_in_the_future = 5
f"In {years_in_the_future} years I will be {years_in_the_future + age} years old."
# "In 5 years I will be 30 years old."
```

### Question 6: `minutes_to_clock`

Write a function `minutes_to_clock` that takes one parameter: a whole number `total_minutes`. It should return a string in the format `"[hours]h [minutes]m"`, where the hours and minutes are the whole hours and the leftover minutes in `total_minutes`.

Do not include the `[]` characters. They are there to show you where the variables go.

```python
minutes_to_clock(125)
# "2h 5m"
minutes_to_clock(45)
# "0h 45m"
minutes_to_clock(60)
# "1h 0m"
```

Hint: The `//` operator divides and rounds down to a whole number, and the `%` operator gives the remainder. One of them gives you the number of whole hours and the other gives you the minutes left over. Which is which?

### Question 7: `is_leap_year`

Write a function `is_leap_year` that takes one parameter: a whole number `year`. It should return `True` if the year is a leap year and `False` otherwise.

A year is a leap year if it is divisible by 4, with one exception: a year divisible by 100 is not a leap year, unless it is also divisible by 400.

```python
is_leap_year(2024)
# True
is_leap_year(2023)
# False
is_leap_year(1900)
# False
is_leap_year(2000)
# True
```

Hint: You will need `and`, `or`, and probably `not`. Python evaluates `and` before `or`, so an expression without parentheses may group your conditions differently than you intended. Test your function against `1900` and `2000` to find out whether your grouping is right.

### Question 8: `make_banner`

Write a function `make_banner` that takes two parameters: a string `text` and a string `symbol`. The `symbol` parameter should have a default value of `"*"`. The function should return the text with a space on each side, surrounded by three copies of the symbol on each side.

```python
make_banner("Hi")
# "*** Hi ***"
make_banner("Hi", "=")
# "=== Hi ==="
make_banner("Hi", symbol="-")
# "--- Hi ---"
```

Hint: The `*` operator repeats a string, the same way it multiplies a number. How many copies does each side need, and what sits between the copies and the text?

### Question 9: `calculate_room_cost`

Write a function `calculate_room_cost` that takes three parameters: a number `width`, a number `height`, and a number `price_per_square_foot`. It should return the cost of covering a rectangular floor, which is the area multiplied by the price per square foot.

Use your `calculate_area` function from Question 1 to find the area.

```python
calculate_room_cost(5, 3, 2)
# 30
calculate_room_cost(10, 7, 1.5)
# 105.0
```

Hint: A function call resolves to the value that the function returns, so `calculate_area(5, 3)` can be used anywhere the number `15` could be used. If `calculate_area` printed its answer instead of returning it, the function call would resolve to `None` and the multiplication would raise a `TypeError`.

### Question 10: `is_vowel`

Write a function `is_vowel` that takes one parameter: a string `letter` containing a single character. It should return `True` if the letter is one of `a`, `e`, `i`, `o`, or `u` in either uppercase or lowercase, and `False` otherwise.

```python
is_vowel("a")
# True
is_vowel("E")
# True
is_vowel("z")
# False
```

Hint: The `in` operator checks whether a value appears inside a string, so `"b" in "abc"` is `True`. Think about what string you want to check the letter against, and whether it needs both cases.

## Modify

### Question 11: `return` vs `print`

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

### Question 12: `greet`

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

### Question 13: Fix our mess of a function

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
