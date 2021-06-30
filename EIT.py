'''1. Escribir una función en Python que, dada una lista de números, devuelva otra lista
en orden inverso. Para realizar este ejercicio se deberá utilizar un bucle o estructura
repetitiva. No se permite el uso de funciones miembro de la clase list (en especial
list.reverse()).'''

def get_reverse_list(num_list):
  reversed_list = []
  for i in range(len(num_list)-1, -1, -1):
    reversed_list.append(num_list[i])
  
  print(reversed_list)

my_list = [23, 48, 10, 15, 3, 90]
get_reverse_list(my_list)


'''Escribir una función que, dado un número entero N, devuelva una lista con todos los
números primos hasta N. Para solucionar el ejercicio debéis crear una función
auxiliar que indique si un determinado número es primo (retornando un valor
booleano).'''

def es_primo(num):
  if (num <= 1):
    return False

  for i in range(2, num):
    if(num%i == 0):
      return False
  
  return True

def obtener_primos(num):
  list_primos = []

  for i in range(num+1):
    if es_primo(i):
      list_primos.append(i)
    
  return list_primos


result = obtener_primos(100)
print(result)


'''3. Escribir una función que reciba una tupla compuesta por caracteres, y devuelva una
lista con los caracteres en mayúsculas. Debéis recorrer la tupla carácter a carácter
para realizar la conversión. Para convertir un carácter a mayúscula podéis usar el
método upper(). Por ejemplo ’a’.upper() nos devuelve ’A’.'''

def get_upper(tupla):
  char_upper = []
  for char in tupla:
    char_upper.append(char.upper())

  return char_upper

print(get_upper(('a', 'b', 'c', 'd', 'Elena')))


'''4. Convertir el texto ’ejemplo’ en una lista que contenga sus 7 caracteres. Después
convertirlo en una tupla y usando la función del ejercicio anterior obtener una lista
con el texto en mayúsculas.'''


texto = 'ejemplo'
letters_list = []

for letter in texto:
  letters_list.append(letter)

letters_tuple = tuple(letters_list)
print(get_upper(letters_tuple))



'''10. Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del
rectangulo a partir de una base y una altura. Calcula el área de un rectángulo de 15
de base y 10 de altura.'''

def area_rectangulo(base:float, altura:float):
  area = base * altura
  return area

result = area_rectangulo(15, 10)
print('El área es:', result)


'''11. Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo
siguiente:
a. Si el primer número es mayor que el segundo, debe devolver 1.
b. Si el primer número es menor que el segundo, debe devolver -1.
c. Si ambos números son iguales, debe devolver un 0.
d. Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'''

def relacion(a:float, b:float):
  if a > b:
    return 1
  elif a < b:
    return -1
  elif a == b:
    return 0

result1 = relacion(5, 10)
result2 = relacion(10, 5)
result3 = relacion(5, 5)
print(result1)
print(result2)
print(result3)


'''12. Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva
su punto intermedio. Cuando lo tengas comprueba el punto intermedio entre -12 y
24.'''

def intermedio(a, b):
  p_intermedio = (a + b) / 2
  return p_intermedio

p_int = intermedio(-12, 24)
print(p_int)


'''13. Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres
parámetros. El primero es el número a recortar, el segundo es el límite inferior y el
tercero el límite superior. La función tendrá que cumplir lo siguiente:
a. Devolver el límite inferior si el número es menor que éste
b. Devolver el límite superior si el número es mayor que éste.
c. Devolver el número sin cambios si no se supera ningún límite.
d. Comprueba el resultado de recortar 15 entre los límites 0 y 10.'''

def recortar(numero, minimo, maximo):
  if numero < minimo:
    return minimo
  elif numero > maximo:
    return maximo
  return numero

print(recortar(15, 0, 10))



'''14. Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si
la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección
se considerará válida si contiene el símbolo "@"'''

def validate_email():
  email = input("Please, enter your email: ")
  if '@' in email:
    print('Valid email') 
  else:
    print('Invalid email') 
  
validate_email()


'''15. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma
de sus dígitos (utilizando una función que realice dicha suma).'''

def sum_digits():
  while True:
    try:
      number = int(input('Please, enter a number: '))

      if number == 0:
        break

      suma = 0
      for digit in str(number):
        suma += int(digit)

      print(suma)
    
    except ValueError:
      print('Invalid input')
    
    
sum_digits()


'''16. Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma
de sus dígitos. Al finalizar, mostrar la sumatoria de todos los números ingresados y
la suma de sus dígitos'''

def sum_digits(number):
  suma = 0
  for digit in str(number):
    suma += int(digit)

  return suma

def main():
  input_numbers = []
  while True:
    try:
      number = int(input('Please, enter a number: '))

      if number == 0:
        len_numbers = len(input_numbers)
        total_sum = sum(input_numbers)
        digits_total_sum = sum_digits(total_sum)
        print('Total números ingresados:', len_numbers)
        print('Sumatoria de todos los números ingresados:', total_sum)
        print('Sumatoria de todos los números ingresados:', digits_total_sum)
        break
      
      input_numbers.append(number)
      number_digits_sum = sum_digits(number)
      print(number_digits_sum)
    
    except ValueError:
      print('Invalid input')
  
main()
  

'''17. Requerir al usuario que ingrese un número entero e informar si es primo o no,
utilizando una función booleana que lo decida.'''

def es_primo(num):
  if (num <= 1):
    return False

  for i in range(2, num):
    if(num%i == 0):
      return False
  
  return True


def main():
  try: 
    num = int(input("INGRESE UN NÚMERO: "))

    if es_primo(num):
      print("EL NÚMERO {} ES PRIMO".format(num))
    else:
      print("EL NÚMERO {} NO ES PRIMO".format(num))
  except:
      print("Error: El numero debe ser entero")


main()


'''18. Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de
ocurrencias del dígito en el número, utilizando para ello una función que calcule la
frecuencia'''

def frecuencia():
  try:
    num = int(input("INGRESE UN NÚMERO: "))
    digit = int(input("INGRESE UN DÍGITO: "))

    freq = 0
    
    for d in str(num):
      if digit == int(d):
        freq += 1
    
    print("El número de ocurrencias del dígito {} en el número {} es: {} ocurrencias".format(digit, num, freq))

  except ValueError:
    print("ERROR: El número debe ser entero")


frecuencia()


