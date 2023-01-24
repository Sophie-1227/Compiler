import global_

line_num = 69 #zaczynamy od 69 bo w pierwszej linijce zawsze będzie skok do main'a, a kolejne to library
location = None

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

    def get_procedure(self):
        for instruction in global_.instructions:
            if instruction[0] == "procedure":
                var_names = self.get_var_names(instruction[0])
                self.translate(instruction[2], instruction[1], var_names)
            else:
                var_names = self.get_var_names("ma1n")
                self.translate(instruction[1], "ma1n", var_names)

    def translate(self, block, pocedure_name, var_names):
        for command in block:
            if command[0] == "proc":
                pass
            elif command[0] == "read":
                pass
            elif command[0] == "write":
                pass
            elif command[0] == "assign":
                pass
            elif command[0] == "add":
                pass
            elif command[0] == "sub":
                pass
            elif command[0] == "mul":
                pass
            elif command[0] == "div":
                pass
            elif command[0] == "mod":
                pass
            elif command[0] == "eq":
                pass
            elif command[0] == "neq":
                pass
            elif command[0] == "gt":
                pass
            elif command[0] == "geq":
                pass
            elif command[0] == "while":
                pass
            elif command[0] == "if":
                pass
            elif command[0] == "ifelse":
                pass
            elif command[0] == "repeat":
                pass
