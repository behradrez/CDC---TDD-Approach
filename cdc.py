import sys

def split_complex(arg):
    terms = arg.split()
    if len(terms) == 3:
        real = float(terms[0])
        img = float(terms[2].replace('j',''))
        if terms[1] == '-': img *= -1
        return (real, img)    
    elif len(terms) == 1:
        return (float(terms[0]), 0)

def format_result(result_tuple):
    res = f"{result_tuple[0]:0g}"
    if result_tuple[1] < 0:
        res += f" - j{abs(result_tuple[1]):0g}"
    else:
        res += f" + j{abs(result_tuple[1]):0g}"

    return res

def parse_input_and_push_stack(curr_input, stack):
    if not curr_input:
        return
    term = ''.join(curr_input).strip()
    if '+j' in term:
        term = f"{term.split('+j')[0]} + j{term.split('+j')[1]}"
    elif '-j' in term:
        term = f"{term.split('-j')[0]} - j{term.split('-j')[1]}"
    curr_input.clear()
    stack.append(split_complex(term.strip()))

def perform_stack_operation(stack, op):
    if len(stack) < 2:
        raise Exception("Error: Stack underflow")
    a = stack.pop()
    b = stack.pop()
    if op == 'add':
        res = (a[0] + b[0], a[1] + b[1])
    elif op == 'sub':
        res = (b[0] - a[0], b[1] - a[1])
    elif op == 'mul':
        real = b[0]*a[0] - b[1]*a[1]
        img = b[0]*a[1] + b[1]*a[0]
        res = (real, img)
    elif op == 'div':
        denom = a[0]**2 + a[1]**2
        if denom == 0:
            raise Exception("Error: Division by zero")
        real = (b[0]*a[0] + b[1]*a[1]) / denom
        img = (b[1]*a[0] - b[0]*a[1]) / denom
        res = (real, img)
    stack.append(res)

def calc(args):
    stack = []
    curr_input = []
    for arg in args:
        arg = arg.strip().lower()
        if "push" in arg:
            parse_input_and_push_stack(curr_input, stack)
        elif "pop" in arg:
            break 
        elif arg in ['add', 'sub', 'mul', 'div']:
            parse_input_and_push_stack(curr_input, stack)
            perform_stack_operation(stack, op=arg.strip().lower())
        elif 'delete' in arg:
            parse_input_and_push_stack(curr_input, stack)
            if not stack:
                raise Exception("Error: Stack underflow")
            stack.pop()
        else:
            curr_input.append(arg)

    parse_input_and_push_stack(curr_input, stack)
    if not stack:
        raise Exception("Error: Stack underflow")
    return format_result(stack.pop())

if __name__ == "__main__":
    print(calc(sys.argv[1:]))