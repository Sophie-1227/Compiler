import global_

line_num = 69 #zaczynamy od 69 bo w pierwszej linijce zawsze będzie skok do main'a, a kolejne to library

class Translator:
    code = []

    def generate_code(self,lista):
        global line_num
        #line 1
        self.code.append("JUMP ma1n")
        #self.generate_ready_library()
        self.get_procedure()
        self.code.append("HALT")

    def get_var_names(self, procedure):
        result=[]
        for var in global_.list_of_variables:
            if var.startswith(procedure):
                result.append(var)
        return result

    def generate_ready_library(self):
        #Equal evaluation - line 2
        self.code.append("SET 1")
        self.code.append("ADD 3")
        self.code.append("SUB 4")
        self.code.append("JPOS 6")
        self.code.append("JUMPI i")
        self.code.append("SUB 1")
        self.code.append("JZERO 9")
        self.code.append("JUMPI i")
        self.code.append("JUMPI 2")
        #Not Equal evaluation - line 11
        self.code.append("SET 1")
        self.code.append("ADD 3")
        self.code.append("SUB 4")
        self.code.append("JZERO 16")
        self.code.append("SUB 1")
        self.code.append("JPOS i")
        self.code.append("JUMPI 2")
        #Greater evaluation - line 18
        self.code.append("LOAD 3")
        self.code.append("SUB 4")
        self.code.append("JPOS 21")
        self.code.append("JUMPI i")
        self.code.append("JUMPI 2")
        #Greater/Equal evaluation - line 23
        self.code.append("SET 1")
        self.code.append("ADD 3")
        self.code.append("SUB 4")
        self.code.append("JPOS 27")
        self.code.append("JUMPI i")
        self.code.append("JUMPI 2")
        #Multiplication - line 29
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
        #Division - line 43
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
        #Modulo - line 56
        self.code.append("LOAD 59")
        self.code.append("STORE 2")
        self.code.append("JUMP 22")
        self.code.append("LOAD 3")
        self.code.append("SUB 4")
        self.code.append("STORE 3")
        self.code.append("JUMP 22")
        #Addition - line 63
        self.code.append("LOAD 3")
        self.code.append("ADD 4")
        self.code.append("JUMPI 2")
        #Subtraction - line 66
        self.code.append("LOAD 3")
        self.code.append("SUB 4")
        self.code.append("JUMPI 2")

    def get_procedure(self):
        for instruction in global_.instructions:
            if instruction[0] == "procedure":
                var_names = self.get_var_names(instruction[0])
                self.translate(instruction[2], instruction[1], var_names)
            else:
                var_names = self.get_var_names("ma1n")
                self.translate(instruction[1], "ma1n", var_names)

    def translate(self, block, procedure_name, var_names):
        for command in block:
            if command[0] == "proc":
                #i = 0
                for var in var_names:
                    self.code.append("SET @command[2][i]")
                    self.code.append("STORE @" + var)
                self.code.append("SET line number")
                self.code.append("STORE " + str(global_.list_of_variables.index(str(str(procedure_name) +"_1ump"))))
                self.code.append("JUMP " + procedure_name)
            elif command[0] == "read":
                self.code.append("GET "+ str(global_.list_of_variables.index(str(str(procedure_name) +"_"+str(command[1])))))
            elif command[0] == "write":
                self.code.append("PUT "+ str(global_.list_of_variables.index(str(str(procedure_name) +"_"+str(command[1])))))
            elif command[0] == "assign":
                self.code.append("SET line number")
                self.code.append("STORE " + str(global_.list_of_variables.index(str(str(procedure_name) +"_1ump"))))
                self.calculate(command[1], procedure_name)
            elif command[0] == "while":
                pass
            elif command[0] == "if":
                pass
            elif command[0] == "ifelse":
                pass
            elif command[0] == "repeat":
                pass

    def calculate(self, equation, procedure_name):
        if equation[0] == "add":
            if not equation[1].isnumeric():
                self.code.append("LOAD " + str(global_.list_of_variables.index(str(procedure_name) + "_" + str(equation[1]))))
            else:
                self.code.append("SET " + str(equation[1]))
            self.code.append("STORE 3")
            if not equation[2].isnumeric():
                self.code.append("LOAD " + str(global_.list_of_variables.index(str(procedure_name) + "_" + str(equation[2]))))
            else:
                self.code.append("SET " + str(equation[2]))                    
            self.code.append("STORE 4")
        elif equation[0] == "sub":
            pass
        elif equation[0] == "mul":
            pass
        elif equation[0] == "div":
            pass
        elif equation[0] == "mod":
            pass

    def evaluate(self, condition, procedure_name):
        if condition[0] == "eq":
            pass
        elif condition[0] == "neq":
            pass
        elif condition[0] == "gt":
            pass
        elif condition[0] == "geq":
            pass