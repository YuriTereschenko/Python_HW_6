# Написать программу вычисления арифметического выражения заданного строкой. Используются операции
# +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
import operator


def decomposing(expression: str):
    decomposed_expression = []
    list_of_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    arithmetic_sign = ['+', '*', '/', '-', '(', ')']
    current_value = ""
    start_position = 0
    if expression[0] == "-":  # подумать, если - после скобки
        current_value = expression[0]
        start_position = 1
    for i in expression[start_position:]:
        if i in list_of_numbers:
            current_value += i
        elif i in arithmetic_sign:
            if current_value != "":
                decomposed_expression.append(current_value)
            decomposed_expression.append(i)
            current_value = ""
        else:
            print(f"'{i}' can't be used in arithmetic expression. Please correct you expression")
            exit(0)
    decomposed_expression.append(current_value)
    return decomposed_expression


def arithmetic_operation(operation, x, y):
    match operation:
        case '+':
            result_of_operation = operator.add(x, y)
        case '-':
            result_of_operation = operator.sub(x, y)
        case '*':
            result_of_operation = operator.mul(x, y)
        case '/':
            result_of_operation = operator.truediv(x, y)
    return result_of_operation


def calculating(decomp_expres):
    for i in range(0, len(decomp_expres)):
        left_offset = 1
        right_offset = 1
        have_prio_oper = '*' in decomp_expres or '/' in decomp_expres
        ar_oper = ['+', '-', '*', '/']
        if decomp_expres[i] in ar_oper:
            j = decomp_expres[i]
            if j == '*' or j == '/' or have_prio_oper is False:
                while decomp_expres[i - left_offset] == "not_add":
                    left_offset += 1
                while decomp_expres[i + right_offset] == "not_add":
                    right_offset += 1
                a = int(decomp_expres[i - left_offset])
                b = int(decomp_expres[i + right_offset])
                decomp_expres[i] = arithmetic_operation(decomp_expres[i], a, b)
                decomp_expres[i - left_offset] = "not_add"
                decomp_expres[i + right_offset] = "not_add"
    count = 0
    for i in decomp_expres:
        if i != "not_add":
            answer = i
            count += 1
    if count != 1:
        answer = calculating(decomp_expres)
    return answer


# def calculating_brackets(decomp_expres: list):
#     is_ready = True
#     if '(' not in decomp_expres:
#         return calculating(decomp_expres)
#     for j in range(0, len(decomp_expres)):
#         if is_ready is False:
#             break
#         if decomp_expres[j] == '(':
#             for i in range(j, len(decomp_expres)):
#                 if decomp_expres[i] == ')':
#                     temp = [k for k in decomp_expres[:j]]
#                     temp.append(calculating(decomp_expres[j + 1:i]))
#                     for k in decomp_expres[i + 1:]:
#                         temp.append(k)
#                     decomp_expres = temp
#                     is_ready = False
#                     break
#     return calculating(decomp_expres)

def cal_br(decomp_expres):
    for i in range(0, len(decomp_expres)):
        if decomp_expres[i] == '(':
            n = i
    for i in range(n, len(decomp_expres)):
        if decomp_expres[i] == ')':
            k = i
            break
    temp_br = [i for i in decomp_expres[n+1:k]]
    temp_br = calculating(temp_br)
    result_br = [i for i in decomp_expres[:n]]
    result_br.append(temp_br)
    for i in decomp_expres[k+1:]:
        result_br.append(i)
    if '(' in result_br:
        return cal_br(result_br)
    else:
        return calculating(result_br)


arithmetic_expression = "(-10*(3+2))*4"
print(decomposing(arithmetic_expression))
result = decomposing(arithmetic_expression)
result = cal_br(result)
print(result)
