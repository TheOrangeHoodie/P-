import sys
from tokenizer import Tokenizer

class WrongUseException(Exception):
    def __init__(self):
        super().__init__("Wrong use! Correct use... \npython3 main.py <filePath>")

class Compiler:
    def __init__(self, args):
        self.args = args
        if len(args) != 2:
            raise WrongUseException()
        self.fileContents = None
        with open(args[1], "rt") as file:
            self.fileContents = file.read()
        
    def run(self):
        tokenizerObj = Tokenizer(self.fileContents)
        for object in tokenizerObj.tokenize():
            print(object.type)
            print(object.value)



if __name__ == "__main__":
    args = sys.argv
    compiler = Compiler(args)
    compiler.run()
