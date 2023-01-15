from sly import Lexer, Parser
import sys
import global_
from translator import Translator

counter = 0
line_number = 1

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
        global line_number
        line_number +=1
        self.lineno += len(t.value)

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

    @_('procedures main')
    def program_all(self, p):
        self.code = Translator(p.commands)
        return self.code

    @_('procedures PROCEDURE proc_head IS VAR declarations BEGIN commands END')
    def procedures(self, p):
        global counter
        global_.procedures_names.append(p[2])
        global_.list_of_variables.append("1ump")
        counter = len(global_.list_of_variables) - counter
        for n in range (1, counter+1):
            global_.list_of_variables[-n] = str(global_.procedures_names[-1]) + " " + str(global_.list_of_variables[-n])
        counter=len(global_.list_of_variables)

    @_('procedures PROCEDURE proc_head IS BEGIN commands END')
    def procedures(self, p):
        global_.procedures_names.append(p[2])
        global_.list_of_variables.append("1ump")
        global counter
        counter = len(global_.list_of_variables) - counter
        for n in range (1, counter+1):
            global_.list_of_variables[-n] = str(global_.procedures_names[-1]) + " " + str(global_.list_of_variables[-n])
        counter=len(global_.list_of_variables)

    @_('empty')
    def procedures(self, p):
        pass

    @_('PROGRAM IS VAR declarations BEGIN commands END')
    def main(self, p):
        global_.procedures_names.append("main")
        global_.list_of_variables.append("1ump")
        global counter
        counter = len(global_.list_of_variables) - counter
        for n in range (1, counter+1):
            global_.list_of_variables[-n] = str(global_.procedures_names[-1]) + " " + str(global_.list_of_variables[-n])
        counter=len(global_.list_of_variables)

    @_('PROGRAM IS BEGIN commands END')
    def main(self, p):
        global_.procedures_names.append("main")
        global_.list_of_variables.append("1ump")
        global counter
        counter = len(global_.list_of_variables) - counter
        for n in range (1, counter+1):
            global_.list_of_variables[-n] = str(global_.procedures_names[-1]) + " " + str(global_.list_of_variables[-n])
        counter=len(global_.list_of_variables)

    @_('commands command')
    def commands(self, p):
        return p[0] + [p[1]]

    @_('command')
    def commands(self, p):
        return [p[0]]

    @_('IDENTIFIER GETS expression ";"')
    def command(self, p):
        return "assign " , p[0] , p[2]

    @_('IF condition THEN commands ELSE commands ENDIF')
    def command(self, p):
        return "ifelse", p[1], p[3], p[5]

    @_('IF condition THEN commands ENDIF')
    def command(self, p):
        return "if", p[1], p[3]

    @_('WHILE condition DO commands ENDWHILE')
    def command(self, p):
        return "while", p[1], p[3]

    @_('REPEAT commands UNTIL condition ";"')
    def command(self, p):
        return "repeat", p[1], p[3]

    @_('proc_head ";"')
    def command(self, p):
        if not p[0] in global_.procedures_names:
            print("Procedure ", p[0], " in line ", line_number, " not in procedures")
        else:
            return p.proc_head

    @_('READ IDENTIFIER ";"')
    def command(self, p):
        return "read", p[1]

    @_('WRITE value ";"')
    def command(self, p):
        return "write", p[1]

    @_('IDENTIFIER "(" declarations ")"')
    def proc_head(self, p):
        return p[0]

    @_('declarations "," IDENTIFIER')
    def declarations(self, p):
        global_.list_of_variables.append(p[2])

    @_('IDENTIFIER')
    def declarations(self, p):
        global_.list_of_variables.append(p[0])

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
        return "le", p[0], p[2]

    @_('value GEQ value')
    def condition(self, p):
        return "ge", p[0], p[2]

    @_('NUM')
    def value(self, p):
        return "constant", p[0]

    @_('IDENTIFIER')
    def value(self, p):
        global line_number
        if not p[0] in global_.list_of_variables:
            print("Undeclared identifier ", p[0], " in line ", line_number)
        else:
            return "id", p[0]

    @_('')
    def empty(self, p):
        pass

sys.tracebacklimit = 0
lex = MyLexer()
pars = MyParser()
with open(sys.argv[1]) as in_f:
    text = in_f.read()

pars.parse(lex.tokenize(text))
print(global_.procedures_names)
print(global_.list_of_variables)
Translator.calculate_expressions()
# code_gen = pars.code
# code_gen.gen_code()
# with open(sys.argv[2], 'w') as out_f:
#     for line in code_gen.code:
#         print(line, file=out_f)