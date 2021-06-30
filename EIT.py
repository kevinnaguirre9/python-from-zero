'''Realiza una función llamada area_rectangulo(base, altura) que devuelva el área del
rectangulo a partir de una base y una altura. Calcula el área de un rectángulo de 15
de base y 10 de altura.'''

def area_rectangulo(base:float, altura:float):
  area = base * altura
  return area

result = area_rectangulo(15, 10)
print('El área es:', result)


'''Realiza una función llamada relacion(a, b) que a partir de dos números cumpla lo
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


'''. Realiza una función llamada intermedio(a, b) que a partir de dos números, devuelva
su punto intermedio. Cuando lo tengas comprueba el punto intermedio entre -12 y
24.'''

def intermedio(a, b):
  p_intermedio = (a + b) / 2
  return p_intermedio

p_int = intermedio(-12, 24)
print(p_int)


'''Realiza una función llamada recortar(numero, minimo, maximo) que reciba tres
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



'''Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si
la dirección es válida o no, valiéndose de una función para decidirlo. Una dirección
se considerará válida si contiene el símbolo "@"'''

def validate_email():
  email = input("Please, enter your email: ")
  if '@' in email:
    print('Valid email') 
  else:
    print('Invalid email') 
  
validate_email()


'''Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma
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


'''Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma
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
  

'''Requerir al usuario que ingrese un número entero e informar si es primo o no,
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


'''Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de
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


