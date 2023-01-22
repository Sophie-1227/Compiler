import global_

line_num = 63 #zaczynamy od 63 bo w pierwszej linijce zawsze będzie skok do main'a, a kolejne to library
location = None

class Translator:
    code = []

    def generate_code(self,lista):
        global line_num
        #line 1
        print("JUMPI " + str(global_.list_of_variables.index("ma1n 1ump")))
        Translator.generate_ready_library(self)
        Translator.generate_inner_code(self, lista)
        print("HALT")

    def generate_ready_library(self):
        #Equal evaluation - line 2
        print("SET 1")
        print("ADD 3")
        print("SUB 4")
        print("JPOS 6")
        print("JUMPI i")
        print("SUB 1")
        print("JZERO 9")
        print("JUMPI i")
        print("JUMPI 2")
        #Not Equal evaluation - line 11
        print("SET 1")
        print("ADD 3")
        print("SUB 4")
        print("JZERO 16")
        print("SUB 1")
        print("JPOS i")
        print("JUMPI 2")
        #Greater evaluation - line 18
        print("LOAD 3")
        print("SUB 4")
        print("JPOS 21")
        print("JUMPI i")
        print("JUMPI 2")
        #Greater/Equal evaluation - line 23
        print("SET 1")
        print("ADD 3")
        print("SUB 4")
        print("JPOS 27")
        print("JUMPI i")
        print("JUMPI 2")
        #Multiplication - line 29
        print("LOAD 4")
        print("STORE 6")
        print("STORE 7")
        print("SET 1")
        print("STORE 4")
        print("SET 36")
        print("STORE 2")
        print("JUMP 17")
        print("LOAD 6")
        print("ADD 7")
        print("STORE 6")
        print("LOAD 4")
        print("ADD 1")
        print("JUMP 17")
        #Division - line 43
        print("SET 1")
        print("SUB 1")
        print("STORE 6")
        print("SET 48")
        print("STORE 2")
        print("JUMP 22")
        print("LOAD 3")
        print("SUB 4")
        print("STORE 3")
        print("LOAD 6")
        print("ADD 1")
        print("STORE 6")
        print("JUMP 22")
        #Modulo - line 56
        print("LOAD 59")
        print("STORE 2")
        print("JUMP 22")
        print("LOAD 3")
        print("SUB 4")
        print("STORE 3")
        print("JUMP 22")
        #Addition - line 63
        print("LOAD 3")
        print("ADD 4")
        print("JUMPI 2")
        #Subtraction - line 66
        print("LOAD 3")
        print("SUB 4")
        print("JUMPI 2")

    def generate_inner_code(self, lista):
        global line_num
        global location
        for block in lista:
            for inst in block:
                if block[0] == 'PROCEDURE':
                    location = block[1]
                    print("SET " + str(line_num+3)+" PROCEDURE")
                    print("STORE " + str(global_.list_of_variables.index(str(location)+" 1ump")))
                    line_num += 2
                    Translator.generate_inner_code(self, inst)
                elif block[0] == 'PROGRAM':
                    location = "ma1n"
                    print("SET " + str(line_num+3)+" PROGRAM")
                    print("STORE " + str(global_.list_of_variables.index("ma1n 1ump")))
                    line_num += 2
                    Translator.generate_inner_code(self, inst)
                elif block[0] == 'PROC':
                    location = block[1]
                    print("SET " + str(line_num+4)+" PROC")
                    print("STORE 2")
                    print("JUMPI " + str(global_.list_of_variables.index(str(block[1]) + " 1ump")))
                    line_num += 3
                    Translator.generate_inner_code(self, inst)
                elif block[0] == 'READ':
                    print("GET " + str(global_.list_of_variables.index(str(location) + " " + str(block[1]))))
                    line_num += 1
                    Translator.generate_inner_code(self, inst)
                elif block[0] == 'WRITE':
                    print("PUT " + str(global_.list_of_variables.index(str(location) + " " + str(block[1]))))
                    line_num += 1
                    Translator.generate_inner_code(self, inst)
                elif block[0] == 'ASSIGN':
                    Translator.generate_inner_code(self, inst)
                    print("STORE " + str(global_.list_of_variables.index(str(location) + " " + str(block[1]))))
                    line_num += 1
                elif block[0] == 'add':
                    if not block[1].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1]))))
                    else:
                        print("SET " + str(block[1]))
                    print("STORE 3")
                    if not block[2].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[2]))))
                    else:
                        print("SET " + str(block[2]))                    
                    print("STORE 4")
                    print("SET " + str(line_num+7))
                    print("STORE 2")
                    line_num += 7
                elif block[0] == 'sub':
                    if not block[1].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1]))))
                    else:
                        print("SET " + str(block[1]))
                    print("STORE 3")
                    if not block[2].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[2]))))
                    else:
                        print("SET " + str(block[2]))                    
                    print("STORE 4")
                    print("SET " + str(line_num+7))
                    print("STORE 2")
                    line_num += 7
                elif block[0] == 'mul':
                    if not block[1].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1]))))
                    else:
                        print("SET " + str(block[1]))
                    print("STORE 3")
                    if not block[2].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[2]))))
                    else:
                        print("SET " + str(block[2]))                    
                    print("STORE 4")
                    print("SET " + str(line_num+8))
                    print("STORE 2")
                    print("JUMP 28")
                    line_num += 7
                elif block[0] =='div':
                    if not block[1].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1]))))
                    else:
                        print("SET " + str(block[1]))
                    print("STORE 3")
                    if not block[2].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[2]))))
                    else:
                        print("SET " + str(block[2]))                    
                    print("STORE 4")                    
                    print("SET " + str(line_num+8))
                    print("STORE 2")
                    print("JUMP 42")
                    line_num += 7 
                elif block[0] == 'mod':
                    if not block[1].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1]))))
                    else:
                        print("SET " + str(block[1]))
                    print("STORE 3")
                    if not block[2].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[2]))))
                    else:
                        print("SET " + str(block[2]))                    
                    print("STORE 4")
                    print("SET " + str(line_num+8))
                    print("STORE 2")
                    print("JUMP 55")
                    line_num += 7
                elif block[0] == 'eq':
                    if not block[1].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1][1]))))
                    else:
                        print("SET " + str(block[1]))
                    print("STORE 3")
                    if not block[2].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1][2]))))
                    else:
                        print("SET " + str(block[2]))                    
                    print("STORE 4")
                    print("STORE 4")
                    print("SET " + str(line_num+8))
                    print("STORE 2")
                    print("JUMP 1")
                    line_num += 7           
                elif block[0] == 'neq':
                    if not block[1].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1][1]))))
                    else:
                        print("SET " + str(block[1]))
                    print("STORE 3")
                    if not block[2].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1][2]))))
                    else:
                        print("SET " + str(block[2]))                    
                    print("STORE 4")
                    print("SET " + str(line_num+8))
                    print("STORE 2")
                    print("JUMP 10")
                    line_num += 7  
                elif block[0] == 'gr':
                    if not block[1].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1][1]))))
                    else:
                        print("SET " + str(block[1]))
                    print("STORE 3")
                    if not block[2].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1][2]))))
                    else:
                        print("SET " + str(block[2]))                    
                    print("STORE 4")
                    print("SET " + str(line_num+8))
                    print("STORE 2")
                    print("JUMP 17")
                    line_num += 7 
                elif block[0] == 'geq':
                    if not block[1].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1][1]))))
                    else:
                        print("SET " + str(block[1]))
                    print("STORE 3")
                    if not block[2].isnumeric():
                        print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1][2]))))
                    else:
                        print("SET " + str(block[2]))                    
                    print("STORE 4")
                    print("SET " + str(line_num+8))
                    print("STORE 2")
                    print("JUMP 22")
                    line_num += 7 
                elif block[0] == 'WHILE':
                    print("SET "+ str(line_num + 8))
                    print("STORE 2")
                    # print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1]))))
                    # print("STORE 3")
                    # print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[2]))))
                    # print("STORE 4")
                    Translator.generate_inner_code(self, block[0][1])
                    print("SET "+ str(line_num + 10))
                    print("STORE 2")
                    Translator.generate_inner_code(self, inst[1])
                    print("JUMP " + str(line_num + 7))
                    line_num += 9
                elif block[0] == 'IF':
                    print("SET "+ str(line_num + 7))
                    print("STORE 2")
                    print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[1]))))
                    print("STORE 3")
                    print("LOAD " + str(global_.list_of_variables.index(str(location) + " " + str(block[2]))))
                    print("STORE 4")
                    Translator.generate_inner_code(self, inst) #alternatywnie swich case dla expressions
                print(inst)