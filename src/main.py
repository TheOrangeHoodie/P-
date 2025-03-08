import sys

class Compiler:
    def __init__(self, args):
        self.args = args
        print(args[0])
        pass


if __name__ == "__main__":
    args = sys.argv
    compiler = Compiler()
    compiler.__init__(args)
