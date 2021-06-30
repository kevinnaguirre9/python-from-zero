import numpy as np
from math import *

def menu():
     while True:
          print("1.- Sumar")
          print("2.- Restar")
          print("3.- Multiplicar")
          print("4.- Dividir")
          print("5.- Potencia")
          print("6.- Raíz")
          print("0.- Exit")

          try:
               op = int(input("Elija una opcion "))
               if op==1:
                    sumar()
               elif op==2:
                    restar()
               elif op==3:
                    multiplicar()
               elif op==4:
                    dividir()
               elif op==5:  
                    potencia()
               elif op==6:
                    raiz()
               elif op==0: 
                    break
          except ValueError:
               print("Input inválido")

def sumar():
     try:
          n1 = float(input("Enter first number: "))
          n2 = float(input("Enter second number: "))
          suma = n1+n2
          print("El resultado de {} + {} es: {} ".format(n1,n2,suma))
     except ValueError:
          print("Input inválido")
     

def restar():
     try:
          n1 = float(input("Ingrese el primer número: "))
          n2 = float(input("Ingrese el segundo número: "))
          resta = n1-n2
          print("El resultado de {} - {} es: {} ".format(n1,n2,resta))
     except ValueError:
          print("Input inválido")

def multiplicar():
     try:
          n1 = float(input("Ingrese el primer número: "))
          n2 = float(input("Ingrese el segundo número: "))
          mult = n1*n2
          print("El resultado de {} * {} es: {} ".format(n1,n2,mult))
     except ValueError:
          print("Input inválido")
     

def dividir():
     try:
          n1 = float(input("Ingrese el primer número: "))
          n2 = float(input("Ingrese el segundo número: "))
          div = n1/n2
          print("El resultado de {} / {} es: {} ".format(n1,n2,div))
     except ValueError:                  
          print("Input inválido")
     except ZeroDivisionError as zero_err:   
          print("ERROR:", zero_err)

def potencia():
     try:
          n1 = int(input("Ingrese la base: "))
          n2 = int(input("Ingrese el exponente: "))
          power = pow(n1, n2)
          print("El resultado de {} ^ {} es: {} ".format(n1,n2,power))
     except ValueError:                  
          print("Input inválido")

def raiz():
     try:
          n1 = int(input("Ingrese el radicando:"))
          n2 = int(input('Ingrese el índice:'))
          if n1 < 0 | n2 < 0:
               print('El número debería ser positivo')
          else:
               raiz = pow(n1, 1/n2)
               print("El resultado es: {} ".format(raiz))
     except ValueError:                  
          print("Input inválido")

# Lo probamos
menu()
print("Thank you for using the system")
