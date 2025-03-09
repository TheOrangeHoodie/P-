from tokenTypes import TokenTypes

class Token:
    def __init__(self, type, value = None):
        self.type = type,
        if value != None:
            self.value = value
        else:
            self.value = None

class Tokenizer():
    def __init__(self, code):
        self.index = 0
        self.code = code
        pass

    def tokenize(self):
        tokenList = []
        buf = ""
        while self._checkNextChar() != None:
            if self._checkNextChar().isalpha():
                buf += self._consume()
                while self._checkNextChar() != None and self._checkNextChar().isalnum():
                    buf += self._consume()

                if buf == "exit":
                    tokenList.append(Token(TokenTypes._exit.value))
                    buf = ""
                    continue
                else:
                    print("Invalid keyword:", buf)
                    exit(1)
            elif self._checkNextChar().isdigit():
                buf += self._consume()
                while self._checkNextChar() != None and self._checkNextChar().isdigit():
                    buf += self._consume()
                
                tokenList.append(Token(TokenTypes.int_lit.value, buf))
                buf = ""
                continue
            elif self._checkNextChar() == ";":
                self._consume()
                tokenList.append(Token(TokenTypes.semi.value))
                continue
            elif self._checkNextChar().isspace():
                self._consume()
                continue
            else:
                print("Invalid keyword:", buf)
                exit(1)
            
        
        return tokenList
                    

    def _checkNextChar(self, spaces = 1):
        if len(self.code) >= self.index + spaces:
            return self.code[self.index]
        else:
            return None
        
        
    def _consume(self):
        self.index += 1
        return self.code[self.index - 1]
