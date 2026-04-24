variables = {}

def evaluate(expr):
    function = {
        'turncloak': lambda s: s[::-1],
    }
    return eval(expr, function, variables)

def run_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if not line:
            i += 1
            continue

        if line.startswith('stark'):
            rest = line[len('stark'):].strip()
            name, value = rest.split('=', 1)

            name = name.strip()
            value = value.strip()   

            if value == 'lannister()':
                user_input = input()
                variables[name] = int(user_input) if user_input.isdigit() else user_input
            else:
                try:
                    variables[name] = evaluate(value)
                except:
                    variables[name] = value.strip('"')


        elif line.startswith('dracarys'):
            content = line[len('dracarys'):].strip()

            try:
                print(evaluate(content))
            except:
                print(content.strip('"'))  

        elif line.startswith('win'):
            condition = line[len('win'):].strip()

            if not evaluate(condition):
                while i < len(lines) and not lines[i].strip().startswith(('die','dany')):
                    i += 1
            
        elif line.startswith('die'):
            while i < len(lines) and not lines[i].strip().startswith('dany'):
                i += 1
        
        elif line.startswith('dany'):
            pass
        i += 1
run_file('is_even.txt')