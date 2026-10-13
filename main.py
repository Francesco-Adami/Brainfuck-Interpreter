mem = [0] * 30000  # Standard Brainfuck tape size
inp = input("Enter brainfuck code: ")
head = 0

def build_jump_table(code):
    stack = []
    jump_table = {}
    for index, cmd in enumerate(code):
        if cmd == '[':
            stack.append(index)
        elif cmd == ']':
            if not stack:
                raise SyntaxError("Unmatched ']' in code")
            start = stack.pop()
            jump_table[start] = index
            jump_table[index] = start
    if stack:
        raise SyntaxError("Unmatched '[' in code")
    return jump_table

def brainfuck(code):
    global head, mem
    jumps = build_jump_table(code)
    i = 0

    while i < len(code):
        cmd = code[i]

        if cmd == '+':
            # 8-bit wrap-around (0-255)
            mem[head] = (mem[head] + 1) % 256

        elif cmd == '-':
            # 8-bit wrap-around (0-255)
            mem[head] = (mem[head] - 1) % 256

        elif cmd == '>':
            head = (head + 1) % len(mem)

        elif cmd == '<':
            head = (head - 1) % len(mem)

        elif cmd == '.':
            # Print ASCII character to stdout
            print(chr(mem[head]), end="", flush=True)

        elif cmd == ',':
            # Read single character from input
            user_in = input()
            mem[head] = ord(user_in[0]) if len(user_in) > 0 else 0

        elif cmd == '[':
            # Jump forward past matching ']' if current cell is 0
            if mem[head] == 0:
                i = jumps[i]

        elif cmd == ']':
            # Jump backward to matching '[' if current cell is non-zero
            if mem[head] != 0:
                i = jumps[i]

        i += 1

    return mem

brainfuck(inp)