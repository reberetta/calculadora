def soma(numero1: float, numero2:float)->float:
    if valida_float(numero1) and valida_float(numero2): 
        soma = numero1 + numero2
        return soma

def sub(numero1: float, numero2:float)->float:
    if valida_float(numero1) and valida_float(numero2): 
        sub = numero1 - numero2
        return sub

def mult(numero1: float, numero2:float)->float:
    if valida_float(numero1) and valida_float(numero2): 
        mult = numero1 * numero2
        return mult

def div(numero1: float, numero2:float)->float:
    if valida_float(numero1) and valida_float(numero2): 
        if(numero2 != 0):
            div = numero1 / numero2
            return div
        print("Não é possível dividir por 0!")


def valida_float(numero:float)->bool:
    if isinstance(numero, float):
        return True
    raise ValueError(f'Valor informado {numero} não é numérico')
#
#option = 1
#
#while option:
#
#    numero1 = (input("Informe o primeiro valor: "))
#    operation = input("Informe a operacao desejada (+, -, *, /):")
#    numero2 = (input("Informe o segundo valor: "))
#
#    try:
#        if operation == "+":
#            print(f'{numero1} + {numero2} = {soma(numero1, numero2)}')
#        elif(operation == "-"):
#            print(f'{numero1} - {numero2} = {sub(numero1, numero2)}')
#        elif(operation == "*"):
#            print(f'{numero1} * {numero2} = {mult(numero1, numero2)}')
#        elif(operation == "/"):
#            print(f'{numero1} / {numero2} = {div(numero1, numero2)}')
#        else:
#            print("Operacao inválida!")
#    except ValueError as error:
#        print(error)
#
#    option = int(input("Deseja continuar? (1 - Sim / 0 - Não)"))