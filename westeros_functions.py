def get_value(token, variables):
    token = token.strip()

    if token.startswith('"') and token.endswith('"'):
        return token[1:-1]

    if token.isdigit():
        return int(token)

    if token in variables:
        return variables[token]

    raise Exception(f"Undefined variable: {token}")


def addition(left, right):
    return left + right


def subtraction(left, right):
    return left - right


def multiplication(left, right):
    return left * right


def division(left, right):
    return left / right


def modulo(left, right):
    return left % right


def turncloak(value):
    return str(value)[::-1]


def compare(left, operator, right):
    if operator == "==":
        return left == right
    elif operator == "!=":
        return left != right
    elif operator == "<":
        return left < right
    elif operator == ">":
        return left > right
    elif operator == "<=":
        return left <= right
    elif operator == ">=":
        return left >= right

    raise Exception(f"Unknown comparison operator: {operator}")


def do_math(left, operator, right):
    if operator == "+":
        return addition(left, right)
    elif operator == "-":
        return subtraction(left, right)
    elif operator == "*":
        return multiplication(left, right)
    elif operator == "/":
        return division(left, right)
    elif operator == "%":
        return modulo(left, right)

    raise Exception(f"Unknown math operator: {operator}")


def evaluate(expr, variables):
    expr = expr.strip()

    # turncloak(word)
    if expr.startswith("turncloak(") and expr.endswith(")"):
        inside = expr[len("turncloak("):-1].strip()
        value = evaluate(inside, variables)
        return turncloak(value)

    # comparisons first
    for operator in ["==", "!=", "<=", ">=", "<", ">"]:
        if operator in expr:
            left, right = expr.split(operator, 1)
            left_value = evaluate(left, variables)
            right_value = evaluate(right, variables)
            return compare(left_value, operator, right_value)

    # math second
    for operator in ["+", "-", "*", "/", "%"]:
        if operator in expr:
            left, right = expr.split(operator, 1)
            left_value = evaluate(left, variables)
            right_value = evaluate(right, variables)
            return do_math(left_value, operator, right_value)

    return get_value(expr, variables)