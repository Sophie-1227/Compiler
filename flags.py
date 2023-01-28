import global_
from translator import Translator

class Flag:
    def flag_catcher():
        code = Translator()
        code.generate_code(global_.instructions)
        for flag in global_.list_of_variables:
            if flag in code:
                pass