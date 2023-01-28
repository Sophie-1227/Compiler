import global_

line_num = 69 #zaczynamy od 69 bo w pierwszej linijce zawsze będzie skok do main'a, a kolejne to library
j = 0

class Translator:
    code = []

    def generate_code(self,lista):
        global line_num
        self.code.append("SET 1")
        self.code.append("STORE 1")
        self.code.append("JUMP ma1n")
        self.generate_ready_library()
        self.get_procedure()
        self.code.append("HALT")
        # self.find_main()

    def get_var_names(self, procedure):
        result=[]
        for var in global_.list_of_variables:
            if var.startswith(procedure):
                result.append(var)
        return result

    def generate_ready_library(self):
        #Equal evaluation - line 3
        self.code.append("SET 1")
        self.code.append("ADD 3")
        self.code.append("SUB 4")
        self.code.append("JPOS 8")
        self.code.append("JUMPI 7")
        self.code.append("SUB 1")
        self.code.append("JZERO 11")
        self.code.append("JUMPI 7")
        self.code.append("JUMPI 8")
        #Not Equal evaluation - line 12
        self.code.append("SET 1")
        self.code.append("ADD 3")
        self.code.append("SUB 4")
        self.code.append("JZERO 18")
        self.code.append("SUB 1")
        self.code.append("JPOS 19")
        self.code.append("JUMPI 8")
        self.code.append("JUMPI 7")
        #Greater evaluation - line 20
        self.code.append("LOAD 3")
        self.code.append("SUB 4")
        self.code.append("JPOS 24")
        self.code.append("JUMPI 7")
        self.code.append("JUMPI 8")
        #Greater/Equal evaluation - line 25
        self.code.append("SET 1")
        self.code.append("ADD 3")
        self.code.append("SUB 4")
        self.code.append("JPOS 30")
        self.code.append("JUMPI 8")
        self.code.append("JUMPI 2")
        #Multiplication - line 31
        self.code.append("LOAD 4")
        self.code.append("STORE 6")
        self.code.append("STORE 5")
        self.code.append("SET 1")
        self.code.append("STORE 4")
        self.code.append("SET 38")
        self.code.append("STORE 2")
        self.code.append("JUMP 20")
        self.code.append("LOAD 6")
        self.code.append("ADD 7")
        self.code.append("STORE 6")
        self.code.append("LOAD 4")
        self.code.append("ADD 1")
        self.code.append("JUMP 20")
        #Division - line 45
        self.code.append("SET 1")
        self.code.append("SUB 1")
        self.code.append("STORE 6")
        self.code.append("SET 50")
        self.code.append("STORE 2")
        self.code.append("JUMP 25")
        self.code.append("LOAD 3")
        self.code.append("SUB 4")
        self.code.append("STORE 3")
        self.code.append("LOAD 6")
        self.code.append("ADD 1")
        self.code.append("STORE 6")
        self.code.append("JUMP 25")
        #Modulo - line 58
        self.code.append("LOAD 59")
        self.code.append("STORE 2")
        self.code.append("JUMP 25")
        self.code.append("LOAD 3")
        self.code.append("SUB 4")
        self.code.append("STORE 3")
        self.code.append("JUMP 25")
        #Addition - line 65
        self.code.append("LOAD 3")
        self.code.append("ADD 4")
        self.code.append("JUMPI 2")
        #Subtraction - line 68
        self.code.append("LOAD 3")
        self.code.append("SUB 4")
        self.code.append("JUMPI 2")

    def get_procedure(self):
        for instruction in global_.instructions:
            if instruction[0] == "procedure":
                global_.procedureStart.append([instruction[1], len(self.code)])
                var_names = self.get_var_names(instruction[0])
                self.translate(instruction[2], instruction[1], var_names)
            else:
                var_names = self.get_var_names("ma1n")
                global_.procedureStart.append([instruction[1], len(self.code)])
                self.translate(instruction[1], "ma1n", var_names)

    def translate(self, block, procedure_name, var_names):
        global j
        for command in block:
            if command[0] == "proc":
                for k in range(len(var_names)-1):
                    self.code.append("SET "+str(global_.list_of_variables.index(str(str(procedure_name) +"_"+ str(command[2][k])))))
                    self.code.append("STORE " + str(global_.list_of_variables.index(str(str(command[1])+"_"+str(command[2][k])))))
                self.code.append("SET " + str(len(self.code)+4))
                self.code.append("STORE " + str(global_.list_of_variables.index(str(str(procedure_name) +"_1ump"))))
                self.code.append("JUMP " + str(self.get_line_number(command[1])))
            elif command[0] == "read":
                self.code.append("GET "+ str(global_.list_of_variables.index(str(str(procedure_name) +"_"+str(command[1])))))
            elif command[0] == "write":
                self.code.append("PUT "+ str(global_.list_of_variables.index(str(str(procedure_name) +"_"+str(command[1])))))
            elif command[0] == "assign":
                if not command[2][1].isnumeric():
                    if procedure_name == "ma1n":
                        self.code.append("LOAD " + str(global_.list_of_variables.index(str(procedure_name) + "_" + str(command[2][1]))))
                    else:
                        self.code.append("LOADI " + str(global_.list_of_variables.index(str(procedure_name) + "_" + str(command[2][1]))))
                else:
                    self.code.append("SET " + str(command[2][1]))
                self.code.append("STORE 3")
                if not command[2][2].isnumeric():
                    if procedure_name == "ma1n":
                        self.code.append("LOAD " + str(global_.list_of_variables.index(str(procedure_name) + "_" + str(command[2][2]))))
                    else:
                        self.code.append("LOADI " + str(global_.list_of_variables.index(str(procedure_name) + "_" + str(command[2][2]))))
                else:
                    self.code.append("SET " + str(command[2][2]))                    
                self.code.append("STORE 4")
                self.code.append("SET " + str(len(self.code)+3))
                self.code.append("STORE 2") 
                self.calculate(command[2], procedure_name)
                self.code.append("STORE " + str(global_.list_of_variables.index(procedure_name+"_"+str(command[1]))))
            elif command[0] == "while":
                j+=1
                self.code.append("SET " + str(len(self.code)+2))
                global_.procedureStart.append("good"+str(j-1))
                self.code.append("STORE " + str(global_.procedureStart.index("good"+str(j-1)))) 
                self.evaluate(command[1], procedure_name)
                self.translate(command[2],procedure_name, var_names)
                self.code.append("SET " + str(len(self.code)+3))
                global_.procedureStart.append("bad"+str(j-1))
                self.code.append("STORE " + str(global_.procedureStart.index("bad"+str(j-1))))
                self.code.append("JUMPI "+ str(global_.procedureStart.index("good"+str(j-1))))
            elif command[0] == "if":
                self.code.append("SET " + str(len(self.code)+2))
                self.code.append("STORE <if"+str(j-1)+">")
                self.evaluate(command[1], procedure_name)
                self.translate(command[2],procedure_name,var_names)
            elif command[0] == "ifelse":
                self.code.append("SET " + str(len(self.code)+2))
                self.code.append("STORE <if"+str(j-1)+">")
                self.evaluate(command[1], procedure_name)
                self.translate(command[2], procedure_name, var_names)
                self.translate(command[3], procedure_name, var_names)
            elif command[0] == "repeat":
                self.code.append("SET " + str(len(self.code)+2))
                self.code.append("STORE <repeat"+str(j-1)+">")
                self.translate(command[1],procedure_name, var_names)
                self.evaluate(command[2], procedure_name)
                self.code.append("JUMPI <repeat>")

    def calculate(self, equation, procedure_name):
        if equation[0] == "add":
            self.code.append("JUMP 65")
        elif equation[0] == "sub":
            self.code.append("JUMP 68")
        elif equation[0] == "mul":
            self.code.append("JUMP 31")
        elif equation[0] == "div":
            self.code.append("JUMP 45")
        elif equation[0] == "mod":
            self.code.append("JUMP 58")

    def evaluate(self, condition, procedure_name):
        if not condition[1].isnumeric():
            if procedure_name == "ma1n":
                self.code.append("LOAD " + str(global_.list_of_variables.index(str(procedure_name) + "_" + str(condition[1]))))
            else:
                self.code.append("LOADI " + str(global_.list_of_variables.index(str(procedure_name) + "_" + str(condition[1]))))
        else:
            self.code.append("SET " + str(condition[1]))
        self.code.append("STORE 3")
        if not condition[2].isnumeric():
            if procedure_name == "ma1n":
                self.code.append("LOAD " + str(global_.list_of_variables.index(str(procedure_name) + "_" + str(condition[2]))))
            else:
                self.code.append("LOADI " + str(global_.list_of_variables.index(str(procedure_name) + "_" + str(condition[2]))))
        else:
            self.code.append("SET " + str(condition[2]))                    
        self.code.append("STORE 4")
        if condition[0] == "eq":
            self.code.append("LOAD " + str(global_.procedureStart.index(str("good")+str(j-1))))
            self.code.append("ADD 8")
            self.code.append("STORE 8")
            self.code.append("LOAD <bad"+str(j-1)+">") # + str(global_.list_of_variables.index(str("bad")+str(j-1))))
            self.code.append("STORE 7")
            self.code.append("JUMP 3")
        elif condition[0] == "neq":
            self.code.append("LOAD " + str(global_.procedureStart.index(str("good")+str(j-1))))
            self.code.append("ADD 10")
            self.code.append("STORE 8")
            self.code.append("LOAD <bad"+str(j-1)+">") # + str(global_.list_of_variables.index(str("bad")+str(j-1))))
            self.code.append("STORE 7")
            self.code.append("JUMP 12")
        elif condition[0] == "gt":
            self.code.append("LOAD " + str(global_.procedureStart.index(str("good")+str(j-1))))
            self.code.append("ADD 10")
            self.code.append("STORE 8")
            self.code.append("LOAD <bad"+str(j-1)+">") # + str(global_.list_of_variables.index(str("bad")+str(j-1))))
            self.code.append("STORE 7")
            self.code.append("JUMP 20")
        elif condition[0] == "geq":
            self.code.append("LOAD " + str(global_.procedureStart.index(str("good")+str(j-1))))
            self.code.append("ADD 10")
            self.code.append("STORE 8")
            self.code.append("LOAD <bad"+str(j-1)+">") # + str(global_.list_of_variables.index(str("bad")+str(j-1))))
            self.code.append("STORE 7")
            self.code.append("JUMP 25")

    def get_line_number(self, name):
        for i in range(len(global_.procedureStart)):
            for j in range(len(global_.procedureStart[0])):
                if global_.procedureStart[i][j] == name:
                    return global_.procedureStart[i][1]
                
    # def find_main(self):
    #     self.code.replace("ma1n", global_.list_of_variables[global_.list_of_variables.index("ma1n_1ump")])