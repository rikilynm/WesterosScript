# WesterosScript

WesterosScript is a Game of Thrones-themed interpreted programming language built in Python.

The language uses themed keywords like `dracarys`, `stark`, `lannister()`, `win`, `die`, and `dany` to execute programs.

---

## Features

WesterosScript supports:

- Variables
- Integers and strings
- User input
- Output
- Arithmetic operations
- Conditional statements (if/else)
- Custom built-in functions

---

## Keywords

| Keyword | Meaning |
|---------|---------|
| `stark` | Declare or assign a variable |
| `dracarys` | Print output |
| `lannister()` | Take user input |
| `win` | Start an if condition |
| `die` | Start an else block |
| `dany` | End an if/else block |
| `turncloak()` | Reverse a string |

---

## Operators

Supported operators:

- `+` addition
- `-` subtraction
- `*` multiplication (also repeats strings)
- `/` division
- `%` modulo
- `==` equal
- `!=` not equal
- `<`, `>`, `<=`, `>=`

---

## How to Run

1. Make sure Python is installed.

2. Run the interpreter:

python main.py

---

## Syntax examples

---

# Variables

stark x = 5
stark name = "Jon Snow"

---

# User Input

dracarys "Send a raven:"
stark raven = lannister()

---

# Output

dracarys "Winter is Coming"
dracarys raven

---

# Operations

stark a = 5
stark b = 3
stark sum = a + b
stark diff = a - b
stark product = a * b
stark remainder = a % b

# Reversing Strings

stark word = "winter"
stark flipped = turncloak(word)
dracarys flipped

---

# If / Else Statement

stark number = 4

win number % 2 == 0
    dracarys "loyal"
die
    dracarys "traitor"
dany

# Loop

stark symbol = "*"
stark count = 5
stark result = symbol * count
dracarys result

---

# Example Programs

helloworld.txt        → prints a message
cat.txt               → echoes user input
multiply.txt          → multiplies two numbers
repeater.txt          → repeats a character
reverse_string.txt    → reverses input
is_palindrome.txt     → checks palindrome
is_even.txt           → checks if a number is even

---

# Theme

dracarys → fire / output
stark → declaration
lannister() → receiving input
win / die → conditional outcomes
dany → ends a block
turncloak() → reversing (switching sides)

---

# Author

Rikilyn Maldonado

