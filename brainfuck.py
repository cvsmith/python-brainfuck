# Brainfuck interpreter in python

guide = dict()
guide['>'] = 'ptr += 1'
guide['<'] = 'ptr -= 1'
guide['+'] = 'array[ptr] += 1'
guide['-'] = 'array[ptr] -= 1'
guide['.'] = 'print array[ptr]'
guide[','] = 'array[ptr] = int(raw_input(">"))'
guide['['] = ('if array[ptr] == 0:\n'
              '    while code[i] != "]":\n'
              '        i += 1')
guide[']'] = ('if array[ptr] != 0:\n'
              '    while code[i] != "[":\n'
              '        i -= 1')

array = [0 for i in xrange(8)]
array[0] = 1
ptr = 0

code = ">>[-]<<[->>+<<]" # Moves value at current cell two cells right

i = 0
while i < len(code):
    cmd = code[i]
    exec(guide[cmd])
    i += 1

print array