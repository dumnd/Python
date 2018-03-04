def postfix(expr):
    x = 0
    final = []
    operators = []
    tokens = expr.split()
    size = len(tokens)

    while x < size:
        if tokens[x] != '+' and tokens[x] != '-' and tokens[x] != '*' and tokens[x] != '/':
            final.append(tokens[x])

        elif tokens[x] == '+' or tokens[x] == '-':
            final.extend(list(reversed(operators)))
            del operators[:]
            operators.append(tokens[x])

        elif tokens[x] == '*' or tokens[x] == '/':
            operators.append(tokens[x])
        x += 1

    final.extend(operators)
    return final


equation = input("Type: ")
final_tokens = postfix(equation)
y = 0
value1 = 0
value2 = 0


while y <= len(final_tokens):
    if final_tokens[y] == "+":
        value1 = int(final_tokens[y - 1])
        value2 = int(final_tokens[y - 2])
        del final_tokens[y - 2:y + 1]
        final_tokens.insert(y - 2, value2 + value1)
        y -= 2

    elif final_tokens[y] == "-":
        value1 = int(final_tokens[y - 1])
        value2 = int(final_tokens[y - 2])
        del final_tokens[y - 2:y + 1]
        final_tokens.insert(y - 2, value2 - value1)
        y -= 2
    elif final_tokens[y] == "*":
        value1 = int(final_tokens[y - 1])
        value2 = int(final_tokens[y - 2])
        del final_tokens[y - 2:y + 1]
        final_tokens.insert(y - 2, value2 * value1)
        y -= 2

    elif final_tokens[y] == "/":
        value1 = int(final_tokens[y - 1])
        value2 = int(final_tokens[y - 2])
        del final_tokens[y - 2:y + 1]
        final_tokens.insert(y - 2, value2 / value1)
        y -= 2
    if len(final_tokens) == 1:
        break
    y += 1

print(final_tokens)










