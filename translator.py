from symbol_table import Variable
import global_

line_num = 62 #zaczynamy od 62 bo w pierwszej linijce zawsze będzie skok do main'a, a kolejne to library
location = None

class Translator:

    def writing():
        a = global_.list_of_variables
        return a

    def __init__(self, commands):
        self.commands = commands
        self.code = []

    def generate_ready_library(self):
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
        #Multiplication
        self.code.append("LOAD 4")
        self.code.append("STORE 6")
        self.code.append("STORE 7")
        self.code.append("SET 1")
        self.code.append("STORE 4")
        self.code.append("SET 36")
        self.code.append("STORE 2")
        self.code.append("JUMP 17")
        self.code.append("LOAD 6")
        self.code.append("ADD 7")
        self.code.append("STORE 6")
        self.code.append("LOAD 4")
        self.code.append("ADD 1")
        self.code.append("JUMP 17")
        #Division
        self.code.append("SET 1")
        self.code.append("SUB 1")
        self.code.append("STORE 6")
        self.code.append("SET 48")
        self.code.append("STORE 2")
        self.code.append("JUMP 22")
        self.code.append("LOAD 3")
        self.code.append("SUB 4")
        self.code.append("STORE 3")
        self.code.append("LOAD 6")
        self.code.append("ADD 1")
        self.code.append("STORE 6")
        self.code.append("JUMP 22")
        #Modulo
        self.code.append("LOAD 58")
        self.code.append("STORE 2")
        self.code.append("JUMP 22")
        self.code.append("LOAD 3")
        self.code.append("SUB 4")
        self.code.append("STORE 3")
        self.code.append("JUMP 22")

    def generate_code(self, lista):
        self.code.append("JUMPI " + str(global_.list_of_variables.index("ma1n 1ump")))
        Translator.generate_ready_library(self)
        for block in lista:
            if block[0] == 'procedure':
                location = block[1]
                self.code.append("SET " + str(line_num+3))
                self.code.append("STORE " + str(global_.list_of_variables.index(str(lista[1])+" 1ump")))
                line_num += 2
                Translator.generate_code(self, block)
            elif block[0] == 'program':
                location = "ma1n"
                self.code.append("SET " + str(line_num+3))
                self.code.append("STORE " + str(global_.list_of_variables.index("ma1n 1ump")))
                line_num += 2
                Translator.generate_code(self, block)
            elif block[0] == 'proc':
                location = block[1]
                self.code.append("SET " + str(line_num+4))
                self.code.append("STORE 2")
                self.code.append("JUMPI " + str(global_.list_of_variables.index(str(block[1]) + " 1ump")))
                line_num += 3
                Translator.generate_code(self, block)
            elif block[0] == 'read':
                self.code.append("GET " + str(global_.list_of_variables.index(str(location) + str(block[1]))))
                line_num += 1
                Translator.generate_code(self, block)
            elif block[0] == 'write':
                self.code.append("PUT " + str(global_.list_of_variables.index(str(location) + str(block[1]))))
                line_num += 1
                Translator.generate_code(self, block)
            elif block[0] == 'assign':
                Translator.generate_code(self, block)
                self.code.append("STORE " + str(global_.list_of_variables.index(str(location) + str(block[1]))))
                line_num += 1
            elif block[0] == 'add':
                self.code.append("LOAD " + str(global_.list_of_variables.index(str(location) + str(block[1]))))
                self.code.append("ADD " + str(global_.list_of_variables.index(str(location) + str(block[2]))))
                line_num += 2
            elif block[0] == 'sub':
                self.code.append("LOAD " + str(global_.list_of_variables.index(str(location) + str(block[1]))))
                self.code.append("SUB " + str(global_.list_of_variables.index(str(location) + str(block[2]))))
                line_num += 2
            elif block[0] == 'mul':
                self.code.append("LOAD " + str(global_.list_of_variables.index(str(location) + str(block[1]))))
                self.code.append("STORE 3")
                self.code.append("LOAD " + str(global_.list_of_variables.index(str(location) + str(block[1]))))
                self.code.append("STORE 4")
                self.code.append("SET " + str(line_num+7))
                self.code.append("JUMP 28")
                line_num += 6
            elif block[0] =='div':
                self.code.append("LOAD " + str(global_.list_of_variables.index(str(location) + str(block[1]))))
                self.code.append("STORE 3")
                self.code.append("LOAD " + str(global_.list_of_variables.index(str(location) + str(block[1]))))
                self.code.append("STORE 4")
                self.code.append("SET " + str(line_num+7))
                self.code.append("JUMP 42")
                line_num += 6   
            elif block[0] == 'mod':
                self.code.append("LOAD " + str(global_.list_of_variables.index(str(location) + str(block[1]))))
                self.code.append("STORE 3")
                self.code.append("LOAD " + str(global_.list_of_variables.index(str(location) + str(block[1]))))
                self.code.append("STORE 4")
                self.code.append("SET " + str(line_num+7))
                self.code.append("JUMP 55")
                line_num += 6
            elif block[0] == 'if':
                pass                                  
