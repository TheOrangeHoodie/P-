class Tokenizer():
    def __init__(self, code):
        self.index = 0
        self.code = code
        pass

    def tokenize(self):
        pass

    def _checkNextChar(self, spaces = 1):
        if self.code[self.index + spaces] != None:
            return self.code[self.index + spaces]
        else:
            return False
        
    def _consume(self):
        
