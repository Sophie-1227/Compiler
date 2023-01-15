from symbol_table import Variable
import global_
#from kompilator import MyLexer, MyParser

line_num = 1

class Translator:

    def writing():
        a = global_.list_of_variables
        return a

    def __init__(self, commands):
        self.commands = commands
        self.code = []
        self.iterators = []

    def tarnslate(self):
        self.translate_commands(self.commands)
        self.code.append("HALT")
    
    def translate_commands(self, commands):
        for command in commands:
            if command[0] == "write":
                pass
            elif command[0] == "read":
                pass
            elif command[0] == "assign":
                pass
            elif command[0] == "if":
                pass
            elif command[0] == "ifelse":
                pass
            elif command[0] == "while":
                pass
            elif command[0] == "repeat":
                pass

    def calculate_expressions(self, expressions):
        for expression in expressions:
            if expression[0] == "constant":
                pass
            elif expression[0] == "id":
                pass
            elif expression[0] == "add":
                pass
            elif expression[0] == "sub":
                pass
            elif expression[0] == "mul":
                pass
            elif expression[0] == "div":
                pass
            elif expression[0] == "mod":
                pass

    def eval_condition(self, condition):
        pass