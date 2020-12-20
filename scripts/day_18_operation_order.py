import re

with open("inputs/day_18_operation_order_input.txt", "r") as input:
    lines = input.read().rstrip().split('\n')

# part 1
def calculateValueOfExpression(expression):
    total = 0
    operation = None
    prev_number = None
    for s in expression.split(' '):
        if s.isnumeric():
            if operation is None:
                total = int(s)
            elif operation == '*':
                total = total * int(s)
            elif operation == '+':
                total = total + int(s)
        elif s == '*':
            operation = '*'
        elif s == '+':
            operation = '+'
        else:
            raise Exception("string not handled in 'expression'")

    return(total)


def calculatelineValue(line):
    expression = line
    while True:
        pattern = '.*\\(([\\d * +]+)\\).*'
        matches = re.search(pattern, expression)
        if matches is not None:
            inner_expression = matches.group(1)
            inner_expression_value = calculateValueOfExpression(inner_expression)
            expression = expression.replace(
                '(' + inner_expression + ')',
                str(inner_expression_value)
            )
        else:
            return(calculateValueOfExpression(expression))


print(sum([calculatelineValue(l) for l in lines]))
# 15285807527593

# part 2
def removeParenthesisFromSingleValueIfAny(expression):
    pattern_d_in_parenthesis = '.*(\\((\\d+)\\)).*'
    matches_d_in_parenthesis = re.search(pattern_d_in_parenthesis, expression)
    if matches_d_in_parenthesis is not None:
        expression = expression.replace(
            matches_d_in_parenthesis.group(1), matches_d_in_parenthesis.group(2)
        )

    return(expression)


def calculatelineValue(line):
    expression = line
    while True:
        # print(expression)
        expression = removeParenthesisFromSingleValueIfAny(expression)

        pattern_addition = '(\\d+ \\+ \\d+)'
        matches_addition = re.search(pattern_addition, expression)
        if matches_addition is not None:
            addition_expression = matches_addition.group(1)
            addition_value = calculateValueOfExpression(addition_expression)
            expression = expression.replace(
                addition_expression, str(addition_value)
            )
        else:
            pattern = '.*\\(([\\d * +]+)\\).*'
            matches = re.search(pattern, expression)
            if matches is not None:
                inner_expression = matches.group(1)
                inner_expression_value = calculateValueOfExpression(inner_expression)
                expression = expression.replace(
                    '(' + inner_expression + ')', str(inner_expression_value)
                )
            else:
                return(calculateValueOfExpression(expression))


print(sum([calculatelineValue(l) for l in lines]))
# 461295257566346
