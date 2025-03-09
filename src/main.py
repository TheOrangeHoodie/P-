import sys
from tokenizer import Tokenizer
from subprocess import call
from tokenTypes import TokenTypes

class Compiler:
    def __init__(self, args):
        self.args = args
        if len(args) != 2:
            print("Wrong use! Correct use... \npython3 main.py <filePath>")
            exit(1)
        self.fileContents = None
        with open(args[1], "rt") as file:
            self.fileContents = file.read()

    def tokenToAsm(self, tokens):
        output = "global _start\n_start:\n"
        for i in range(0, len(tokens)):
            token = tokens[i]
            if token.type[0] == TokenTypes._exit.value:
                if i + 1 < len(tokens) and tokens[i + 1].type[0] == TokenTypes.int_lit.value:
                    if i + 2 < len(tokens) and tokens[i + 2].type[0] == TokenTypes.semi.value:
                        output +=  "    mov rax, 60\n"
                        output += f"    mov rdi, {tokens[i + 1].value}\n"
                        output +=  "    syscall\n"

        return output
        
    def run(self):
        tokenizerObj = Tokenizer(self.fileContents)
        asm = self.tokenToAsm(tokenizerObj.tokenize())
        with open("out.asm", "wt") as file:
            file.write(asm)

        call(["nasm", "-felf64",  "out.asm"])
        call(["ld",  "-o",  "out",  "out.o"])



if __name__ == "__main__":
    args = sys.argv
    compiler = Compiler(args)
    compiler.run()
