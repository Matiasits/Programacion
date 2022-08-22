"""Escribir una clase en python para encontrar la validez de una cadena de paréntesis, 
'(', ')', '{', '}', '['  ']. Los paréntesis deben aparecer en el orden correcto, por ejemplo "()" y "()[]{}" son validos,
pero "[)", "({[)]" y "{{{" son inválidos."""

class Validacion_parentesis():
    
    inicial_parentesis = ['(','[','{']
    
    final_parentesis = [')',']','}']
    

    def validar(self,string:str) -> bool:
        
        for c in string:
            if c in self.inicial_parentesis:
                for f in string:
                    if f == ')' or f == ']' or f == '}':
                        valido = False
                    else:
                        valido = True
        return valido


string = Validacion_parentesis()

print(string.validar("h[ol}a"))
