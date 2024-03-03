class type:
    S = 0
    U = 1
    Z = 2
    A = 3
    B = 4
    a = 5
    b = 6
    qe = 7
    bottom = 8

path = "input.txt"

def syn_analyzer(prog_text):
    stck = []
    i = 0
    stack_top = 0

    stck.append(type.S)

    prog_chars = prog_text + '\n'
    while i < len(prog_chars):
        if stck:
            stack_top = stck[-1]
        else:
            return False

        current_symbol = prog_chars[i]
        if stack_top == type.S:
            if current_symbol == 'a':
                stck.pop()
                stck.extend([type.bottom, type.U, type.Z])
            elif current_symbol == '[':
                stck.pop()
                stck.extend([type.bottom, type.U, type.Z])
            elif current_symbol == '\n':
                stck.pop()
            else:
                print("Error in rule S")
                return False
        elif stack_top == type.U:
            if current_symbol == 'a' or current_symbol == 'b':
                stck.pop()
                stck.extend([type.bottom, type.U, type.Z])
            elif current_symbol == '\n':
                stck.pop()
            else:
                return False
        elif stack_top == type.Z:
            if current_symbol == 'a':
                stck.pop()
                stck.extend([type.b, type.A])
                i += 1
            elif current_symbol == '[':
                stck.pop()
                stck.extend([type.qe, type.a, type.B, type.b])
                i += 1
            else:
                return False
        elif stack_top == type.A:
            if current_symbol == 'a':
                stck.pop()
                stck.extend([type.b, type.A])
                i += 1
            elif current_symbol == 'b':
                stck.pop()
            else:
                return False
        elif stack_top == type.B:
            if current_symbol == 'a':
                stck.pop()
            elif current_symbol == 'b':
                stck.pop()
                stck.extend([type.a, type.B])
                i += 1
            else:
                return False
        elif stack_top == type.a:
            if current_symbol == 'a':
                stck.pop()
                i += 1
            else:
                return False
        elif stack_top == type.b:
            if current_symbol == 'b':
                stck.pop()
                i += 1
            else:
                return False
        elif stack_top == type.qe:
            if current_symbol == ']':
                stck.pop()
                i += 1
            else:
                return False
        elif stack_top == type.bottom:
            if current_symbol == '\n':
                return True
            else:
                return False

    return False

def main():
    with open(path, 'r') as file:
        open_file_text = file.read()
    
    if syn_analyzer(open_file_text):
        print("Данная Цепь валидна")

    else:
            print("Данная цепь не валидна!")


if __name__ == "__main__":
    main()