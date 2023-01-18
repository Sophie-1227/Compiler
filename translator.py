from symbol_table import Variable
import global_
#from kompilator import MyLexer, MyParser

line_num = 28 #zaczynamy od 28 bo w pierwszej linijce zawsze będzie skok do main'a, a kolejne to library

class Translator:

    def writing():
        a = global_.list_of_variables
        return a

    def __init__(self, commands):
        self.commands = commands
        self.code = []

    def generate_code(self):
        self.code.append("JUMPI " + str(global_.list_of_variables.index("ma1n 1ump")))
        for instruction in global_.instructions:
            block = list(instruction)
            if block[0] == 'procedure':
                self.code.append("SET " + str(line_num+1))
                self.code.append("STORE " + str(global_.list_of_variables.index(str(block[1])+" 1ump")))
                line_num += 2
            elif block[0] == 'program':
                self.code.append("SET " + str(line_num+1))
                self.code.append("STORE " + str(global_.list_of_variables.index("ma1n 1ump"))) #ewentualnie hard code nazwy funkcji jako main czy coś w tym stylu
                line_num += 2
            elif block[0] == 'if':
                pass
            elif block[0] == 'ifelse':
                pass

        self.code.append("HALT")

    #a i b będą przekazywane w funkcji generate_code 
    def generate_ready_library(self, a, b):
        pass
        #Equal evaluation
        self.code.append("SET 1")
        self.code.append("ADD 3")
        self.code.append("SUB 4")
        self.code.append("JPOS 6")
        self.code.append("JUMPI i")
        self.code.append("SUB 1")
        self.code.append("JZERO 9")
        self.code.append("JUMPI i")
        self.code.append("JUMPI 2")
        #Not Equal evaluation
        self.code.append("SET 1")
        self.code.append("ADD 3")
        self.code.append("SUB 4")
        self.code.append("JZERO 16")
        self.code.append("SUB 1")
        self.code.append("JPOS i")
        self.code.append("JUMPI 2")
        #Greater evaluation
        self.code.append("LOAD 3")
        self.code.append("SUB 4")
        self.code.append("JPOS 21")
        self.code.append("JUMPI i")
        self.code.append("JUMPI 2")
        #Greater/Equal evaluation
        self.code.append("SET 1")
        self.code.append("ADD 3")
        self.code.append("SUB 4")
        self.code.append("JPOS 27")
        self.code.append("JUMPI i")
        self.code.append("JUMPI 2")



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