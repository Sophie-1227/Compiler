from sly import Lexer, Parser
import global_
import sys
from translator import Translator

class MyLexer(Lexer):
    tokens = {IDENTIFIER, NUM,
            PROCEDURE, IS, VAR, END, BEGIN, PROGRAM,
            IF, THEN, ELSE, ENDIF,
            WHILE, DO, ENDWHILE,
            REPEAT, UNTIL,
            READ, WRITE,
            GETS, NEQ, GEQ, LEQ, EQ, GT, LT}
    literals = {'+', '-', '*', '/', '%', ',', ';', '(', ')', ' , '}
    ignore = ' \t'

    ignore_comment = r'[[][^]]*[]]'


    @_(r'\n+')
    def ignore_newline(self, t):
        global_.line_number+=1


    def error(self, t):
        raise Exception(f"Illegal character '{t.value[0]}'")

    PROCEDURE   = r"PROCEDURE"
    IS          = r"IS"
    VAR         = r"VAR"
    BEGIN       = r"BEGIN"
    PROGRAM     = r"PROGRAM"
    IF          = r"IF"
    THEN        = r"THEN"
    ELSE        = r"ELSE"
    ENDWHILE    = r"ENDWHILE"
    ENDIF       = r"ENDIF"
    END         = r"END"
    WHILE       = r"WHILE"
    DO          = r"DO"
    REPEAT      = r"REPEAT"
    UNTIL       = r"UNTIL"
    READ        = r"READ"
    WRITE       = r"WRITE"

    GETS = r":="
    NEQ = r"!="
    GEQ = r">="
    LEQ = r"<="
    EQ = r"="
    GT = r">"
    LT = r"<"
    IDENTIFIER = r"[_a-z]+"
    NUM = r'\d+'


class MyParser(Parser):    
    tokens = MyLexer.tokens
    new_var_lock = True
    code = None
    tmpVariables = []

    @_('procedures main')
    def program_all(self, p):

        global_.list_of_variables = ["acc","1","tmp1","tmp2","multi","tmp3"]+global_.list_of_variables

        if p[0] != None:
            global_.instructions = [p[0],p[1]]
            return [p[0],p[1]]
        else:
            global_.instructions = [p[1]]
            return [p[1]]

    @_('procedures PROCEDURE proc_head IS VAR declarations BEGIN commands END')
    def procedures(self, p):
        duplicates = duplicatesFinder(p[2][1]+p[5])
        if len(duplicates) > 0:
            print("ERROR: Secondary declaration of variables = ", duplicates)

        global_.procedure_names.append([p[2][0],len(p[2][1])])
        global_.list_of_variables.append("1ump")
        for i in range(len(global_.list_of_variables)):
            if not ' ' in global_.list_of_variables[i]: # if varName one word concat name of procedure in front
                global_.list_of_variables[i] = global_.procedure_names[-1][0] + " " + global_.list_of_variables[i]
        if p[0] != None:
            return p[0]+["PROCEDURE" , p[2][0] , p[7]]# p[5],
        else:
            return ["PROCEDURE" , p[2][0] , p[7]]# p[5],

    @_('procedures PROCEDURE proc_head IS BEGIN commands END')
    def procedures(self, p):
        duplicates = duplicatesFinder(p[2][1])
        if len(duplicates) > 0:
            print("ERROR: Secondary declaration of variables = ", duplicates)

        global_.procedure_names.append([p[2][0],len(p[2][1])])
        global_.list_of_variables.append("1ump")
        for i in range(len(global_.list_of_variables)):
            if not ' ' in global_.list_of_variables[i]: # if varName one word concat name of procedure in front
                global_.list_of_variables[i] = global_.procedure_names[-1][0] + " " + global_.list_of_variables[i]
        if p[0] != None:
            return p[0]+["PROCEDURE" , p[2][0] , p[5]]
        else:
            return ["PROCEDURE" , p[2][0] , p[5]]

    @_('empty')
    def procedures(self, p):
        return

    @_('PROGRAM IS VAR declarations BEGIN commands END')
    def main(self, p):
        duplicates = duplicatesFinder(p[3])
        if len(duplicates) > 0:
            print("ERROR: Secondary declaration of variables = ", duplicates)

        global_.procedure_names.append(["ma1n",])
        global_.list_of_variables.append("1ump")
        for i in range(len(global_.list_of_variables)):
            if not ' ' in global_.list_of_variables[i]: # if varName one word concat name of procedure in front
                global_.list_of_variables[i] = global_.procedure_names[-1][0] + " " + global_.list_of_variables[i]
        return ["PROGRAM" , p[3] , p[5]]

    @_('PROGRAM IS BEGIN commands END')
    def main(self, p):
        global_.procedure_names.append(["ma1n",])
        global_.list_of_variables.append("1ump")
        for i in range(len(global_.list_of_variables)):
            if not ' ' in global_.list_of_variables[i]: # if varName one word concat name of procedure in front
                global_.list_of_variables[i] = global_.procedure_names[-1][0] + " " + global_.list_of_variables[i]
        return ["PROGRAM" , p[3]]

    @_('commands command')
    def commands(self, p):
        return p[0] + [p[1]]

    @_('command')
    def commands(self, p):
        return [p[0]]

    @_('IDENTIFIER GETS expression ";"')
    def command(self, p):
        return "ASSIGN" , [p[0]] , [p[2]]

    @_('IF condition THEN commands ELSE commands ENDIF')
    def command(self, p):
        return ["IFELSE", p[1], p[3], p[5]]

    @_('IF condition THEN commands ENDIF')
    def command(self, p):
        return ["IF", [p[1], p[3]]]

    @_('WHILE condition DO commands ENDWHILE')
    def command(self, p):
        return ["WHILE", [p[1]], [p[3]]]

    @_('REPEAT commands UNTIL condition ";"')
    def command(self, p):
        return ["REPEAT", p[1], p[3]]

    @_('proc_head ";"')
    def command(self, p):
        fuckup = True
        for i in global_.procedure_names:
            if p[0][0] == i[0]:
                fuckup = False
        if fuckup:
            print("ERROR. Undeclared procedure = ", p[0][0], " in line ", global_.line_number)
            return SyntaxError

        fuckup = True
        for i in global_.procedure_names:
            if p[0][0] == i[0] and len(p[0][1]) == i[1]:
                fuckup = False
        if fuckup:
            print("ERROR. Wrong number of arguments ", p[0][0], " ", p[0][1], " in line ", global_.line_number)
            return SyntaxError
        else:
            return ["PROC", p[0][0], p[0][1]]

    @_('READ IDENTIFIER ";"')
    def command(self, p):
        return ["READ", p[1]]

    @_('WRITE value ";"')
    def command(self, p):
        return ["WRITE", p[1]]

    @_('IDENTIFIER "(" declarations ")"')
    def proc_head(self, p):
        return p[0], p[2]

    @_('declarations "," IDENTIFIER')
    def declarations(self, p):
        if not  p[2] in global_.list_of_variables:
            global_.list_of_variables.append(p[2])
        return p[0] + [p[2]]

    @_('IDENTIFIER')
    def declarations(self, p):
        if not  p[0] in global_.list_of_variables:
            global_.list_of_variables.append(p[0])
        return [p[0]]

    @_('value')
    def expression(self, p):
        return p[0]

    @_('value "+" value')
    def expression(self, p):
        return "add", p[0], p[2]

    @_('value "-" value')
    def expression(self, p):
        return "sub", p[0], p[2]

    @_('value "*" value')
    def expression(self, p):
        return "mul", p[0], p[2]

    @_('value "/" value')
    def expression(self, p):
        return "div", p[0], p[2]

    @_('value "%" value')
    def expression(self, p):
        return "mod", p[0], p[2]

    @_('value EQ value')
    def condition(self, p):
        return "eq", p[0], p[2]

    @_('value NEQ value')
    def condition(self, p):
        return "ne", p[0], p[2]

    @_('value LT value')
    def condition(self, p):
        return "gt", p[2], p[0]

    @_('value GT value')
    def condition(self, p):
        return "gt", p[0], p[2]

    @_('value LEQ value')
    def condition(self, p):
        return "ge", p[2], p[0]

    @_('value GEQ value')
    def condition(self, p):
        return ["ge", p[0], p[2]]

    @_('NUM')
    def value(self, p):
        return p[0]

    @_('IDENTIFIER')
    def value(self, p):
        if not p[0] in global_.list_of_variables:
            print("ERROR. Undeclared variable = ", p[0], " in line ", global_.line_number)
            return SyntaxError
        else:
            return p[0]

    @_('')
    def empty(self, p):
        pass


def duplicatesFinder(myList):
    newList = [] # empty list to hold unique elements from the list
    dupList = [] # empty list to hold the duplicate elements from the list
    for i in myList:
        if i not in newList:
            newList.append(i)
        else:
            dupList.append(i)
    return dupList


def main():

    if len(sys.argv)!=3:
        print("io error")
        return

    lex = MyLexer()
    pars = MyParser()

    with open(sys.argv[1]) as in_f:
        text = in_f.read()

    pars.parse(lex.tokenize(text))

    print(global_.list_of_variables)

    print(global_.instructions)

    code = Translator()
    code.generate_code(global_.instructions)

    with open(sys.argv[2], 'w') as out_f:
        for line in code.code:
            print(line, file=out_f)

main()