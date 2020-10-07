"""
Given a String contianing just the characters '[]{}()' determine if the input is valid.
Return True if valid, otherwise False
An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets ust be closed in the correct order, with its corresponding open-clsoe bracket.
    3. A valid string is considered valid.


brackets = '[]{}()'  ===> True
brackets = '([]{})'  ===> True
brackets = '([]){'    ===> False
"""

def is_valid_brackets(brackets):
    if brackets == '':
        return True

    brackets_dictionary = { '(': ')', '[': ']', '{': '}' }

    stack = [] # LiFo

    for bracket in brackets:
        if bracket in brackets_dictionary:
            stack.append(bracket)
        elif brackets_dictionary[stack[-1]] == bracket:
            stack.pop()
    
    return True if len(stack) == 0 else False

brackets = '[]{}()'
print(is_valid_brackets(brackets))

brackets = '([]{})'
print(is_valid_brackets(brackets))

brackets = '([]{'
print(is_valid_brackets(brackets))


####

'''
Created on 23/09/2020
@author: Daniel
'''
class Caracteres:
    def __init__(self):
        self.cola=[]

    def inserta(self, valor):
        self.cola.append(valor)
    
    def extrae_a(self, valor):
        existe=False
        indice=0 
        if len(self.cola) == 0:
            return None

        for indice in range(len(self.cola)):
            if self.cola[indice]==valor:
                del self.cola[indice]
                existe=True
                return existe
        return existe

    def valida(self, valor):
        if len(self.cola) == 0:
            return 'Vacía'

        if valor=='{':
            if self.extrae_a('}')==True:
                self.extrae_a(valor)
        elif valor=='(':          
            if self.extrae_a(')')==True:
                self.extrae_a(valor)
        elif valor=='[':           
            if self.extrae_a(']')==True:
                self.extrae_a(valor)

    def es_vacía(self):
        return len(self.cola)==0

    def __str__(self):
        cadena=''
        for elemento in(self.cola):
            cadena=cadena+str(elemento) + ''
        return cadena

##EJECUTA EL PROGRAMA
cadena='([]){'
caracter=Caracteres()

#Llena lista
for i in range(len(cadena)):
    caracter.inserta(cadena[i])

#Valida lista
for i in range(len(cadena)):
    caracter.valida(cadena[i])

#Resultados   
print(caracter.es_vacía())
print("Lista:" , caracter)
