# WesterosScript

WesterosScript is a Game of Thrones-themed interpreted programming language built in Python.

It uses custom keywords like `dracarys`, `stark`, `lannister()`, `win`, `die`, `dany`, `baratheon`, and `turncloak()` to run simple programs.

---

## Features

WesterosScript currently supports:

- Variables
- Integers and strings
- User input
- Output
- Arithmetic operations
- Comparisons
- `if / else` logic
- `while`-style loops
- A custom built-in string reversal function

---

## Keywords

| Keyword | Meaning |
|---------|---------|
| `stark` | Declare or assign a variable |
| `dracarys` | Print output |
| `lannister()` | Take user input |
| `win` | Start an `if` condition |
| `die` | Start an `else` block |
| `dany` | End an `if`, `else`, or loop block |
| `baratheon` | Start a loop that repeats while a condition is true |
| `turncloak()` | Reverse a value as text |

---

## Operators

Supported operators:

- `+` addition
- `-` subtraction
- `*` multiplication
- `/` division
- `%` modulo
- `==` equal
- `!=` not equal
- `<` greater than
- `>` less than 
- `<=` less than or equal too
- `>=` greater than or equal too

---

## How to Run

Make sure Python is installed, then run:

```bash
python main.py your_file.txt
```

Example:

```bash
python main.py multiply.txt
```

---

## Syntax Examples

### Variables

```txt
stark x = 5
stark name = "Jon Snow"
```

### User Input

```txt
dracarys "Send a raven:"
stark raven = lannister()
```

### Output

```txt
dracarys "Winter is Coming"
dracarys raven
```

### Reversing Text

```txt
stark word = "winter"
stark flipped = turncloak(word)
dracarys flipped
```

Output:

```txt
retniw
```

### If / Else

```txt
stark number = 4

win number % 2 == 0
    dracarys "loyal"
die
    dracarys "traitor"
dany
```

Output:

```txt
loyal
```

### Loop

```txt
stark count = 3

baratheon count > 0
    dracarys count
    stark count = count - 1
dany
```

Output:

```txt
3
2
1
```

---

## Example Programs

### `helloworld.txt`

Code:

```txt
dracarys "Winter is Coming"

stark winter = "Winter came"
dracarys winter
```

Result:

```txt
Winter is Coming
Winter came
```

### `cat.txt`

Code:

```txt
dracarys "Send a raven: "
stark raven = lannister()
dracarys raven
```

Sample input:

```txt
Winterfell
```

Result:

```txt
Send a raven: 
Winterfell
```

### `multiply.txt`

Code:

```txt
dracarys "Name your first number"
stark a = lannister()

dracarys "Name your second"
stark b = lannister()

stark result = a * b
dracarys result
```

Sample input:

```txt
6
7
```

Result:

```txt
Name your first number
Name your second
42
```

### `repeater.txt`

Code:

```txt
dracarys "Send a sign to the realm:"
stark symbol = lannister()

dracarys "How many times shall it echo?"
stark count = lannister()

baratheon count > 0
    stark count = count - 1
    dracarys symbol
dany
```

Sample input:

```txt
*
5
```

Result:

```txt
Send a sign to the realm:
How many times shall it echo?
*
*
*
*
*
```

### `reverse.txt`

Code:

```txt
dracarys "Send a raven: "
stark raven = lannister()

stark flipped = turncloak(raven)
dracarys flipped
```

Sample input:

```txt
stark
```

Result:

```txt
Send a raven: 
krats
```

### `is_palindrome.txt`

Code:

```txt
dracarys "Are you here to bend the knee?"
stark oath = lannister()

win oath == turncloak(oath)
    dracarys "loyal"
die
    dracarys "traitor"
dany
```

Sample input:

```txt
racecar
```

Result:

```txt
Are you here to bend the knee?
loyal
```

### `is_even.txt`

Code:

```txt
dracarys "Name your number before the iron throne: "
stark number = lannister()

win number % 2 == 0
    dracarys "even"
die
    dracarys "odd"
dany
```

Sample input:

```txt
8
```

Result:

```txt
Name your number before the iron throne: 
even
```

---

## Theme

- `dracarys` = fire / output
- `stark` = declaration
- `lannister()` = receiving input
- `win / die` = conditional outcomes
- `dany` = block ending
- `baratheon` = repeated battle / looping
- `turncloak()` = reversal / switching sides

---

## Author

Rikilyn Maldonado
