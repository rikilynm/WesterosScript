import sys
from westeros_functions import evaluate

variables = {}


def run_lines(lines):
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if not line:
            i += 1
            continue

        # variable assignment
        if line.startswith("stark"):
            rest = line[len("stark"):].strip()
            name, value = rest.split("=", 1)

            name = name.strip()
            value = value.strip()

            if value == "lannister()":
                user_input = input()
                variables[name] = int(user_input) if user_input.isdigit() else user_input
            else:
                variables[name] = evaluate(value, variables)

        # print
        elif line.startswith("dracarys"):
            content = line[len("dracarys"):].strip()
            print(evaluate(content, variables))

        # if / else
        elif line.startswith("win"):
            condition = line[len("win"):].strip()

            true_block = []
            false_block = []

            i += 1

            while i < len(lines):
                block_line = lines[i].strip()

                if block_line == "die":
                    i += 1
                    break

                if block_line == "dany":
                    break

                true_block.append(lines[i])
                i += 1

            while i < len(lines):
                block_line = lines[i].strip()

                if block_line == "dany":
                    break

                false_block.append(lines[i])
                i += 1

            if evaluate(condition, variables):
                run_lines(true_block)
            else:
                run_lines(false_block)

        # loop
        elif line.startswith("baratheon"):
            condition = line[len("baratheon"):].strip()

            loop_block = []

            i += 1

            while i < len(lines):
                block_line = lines[i].strip()

                if block_line == "dany":
                    break

                loop_block.append(lines[i])
                i += 1

            while evaluate(condition, variables):
                run_lines(loop_block)

        i += 1


def run_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    run_lines(lines)


if len(sys.argv) < 2:
    print("Usage: python main.py filename.txt")
else:
    run_file(sys.argv[1])