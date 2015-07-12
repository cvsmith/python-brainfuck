# Brainfuck interpreter in python

class Brainfuck:

    def __init__(self):
        self.guide = self.make_guide()
    
    def make_guide(self):
        guide = dict()

        guide['>'] = self.inc_ptr
        guide['<'] = self.dec_ptr
        guide['+'] = self.inc_byte
        guide['-'] = self.dec_byte
        guide['.'] = self.output
        guide[','] = self.input
        guide['['] = self.jump_forward
        guide[']'] = self.jump_back

        return guide

    def inc_ptr(self):
        if self.arr_ptr == len(self.arr) - 1:
            self.arr.append(0)
        self.arr_ptr += 1

    def dec_ptr(self):
        if self.arr_ptr == 0:
            self.arr.insert(0, 0)
        else:
            self.arr_ptr -= 1

    def inc_byte(self):
        self.arr[self.arr_ptr] += 1

    def dec_byte(self):
        self.arr[self.arr_ptr] -= 1

    def output(self):
        print chr(self.arr[self.arr_ptr]),

    def input(self):
        self.arr[self.arr_ptr] = int(raw_input(">"))

    def jump_forward(self):
        depth = 1
        if self.arr[self.arr_ptr] == 0:
            while depth != 0:
                self.cmd_ptr += 1
                cmd = self.code[self.cmd_ptr]
                if cmd == '[':
                    depth += 1
                elif cmd == ']':
                    depth -= 1

    def jump_back(self):
        depth = 1
        if self.arr[self.arr_ptr] != 0:
            while depth != 0:
                self.cmd_ptr -= 1
                cmd = self.code[self.cmd_ptr]
                if cmd == ']':
                    depth += 1
                elif cmd == '[':
                    depth -= 1

    def run(self, code, trace=False):
        self.arr = [0]
        self.arr_ptr = 0
        self.cmd_ptr = 0
        self.code = code
        while self.cmd_ptr < len(self.code):
            cmd = self.code[self.cmd_ptr]
            if trace: print self.arr, self.arr_ptr, cmd
            self.guide[cmd]()
            self.cmd_ptr += 1

        return self.arr

brainfuck = Brainfuck()

# Takes input, moves it two cells right
print brainfuck.run(",>>[-]<<[->>+<<]", trace=True)

# Hello World!
print brainfuck.run("++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.",
                   trace=False)
