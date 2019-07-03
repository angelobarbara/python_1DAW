#Módulo Op_bas.
# -*- coding: utf-8 -*-

# Función que suma los dos parametros y devuelve el resultado.
def sumar(a,b):
    return a + b

#Función que resta los dos parametros y devuelve el resultado.
def restar(a,b):
    return a - b

#Función que multiplica los parámetros y delvuelve el resultado.
def multiplicar(a,b):
    return a * b

#Función que divide los parámetros (numerador, denominador) y devuelve
#el resultado. Lanza una excepción en caso de división por cero.
#El código de esa excepción mostrará el mensaje 'ERROR: No se puede dividir
#por cero' y lanzará una excepción del tipo ZeroDivisionError.
def dividir(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("\nNo se puede dividir por cero")
