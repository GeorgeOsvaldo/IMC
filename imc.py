# Aquí se pide la cantidad de personas
personas = int(input("personas: "))

# El valor de personas tiene que ser mayor a 0, si no, no se calculará nada
while personas > 0:
    nombre = input("Introduzca Nombre(s): ")
    apellido_paterno = input("Introduzca apellido paterno: ")
    apellido_materno = input("Introduzca apellido materno: ")
    
    # Se pide la edad del usuario
    e = int(input("Su edad en años por favor: "))
    
    # La altura se pide en metros, por lo que se usará un float
    a = float(input("Su altura en metros por favor: "))
    
    # Esto es para indicar que est (estatura) es = a (altura)
    est = a
    
    # De la misma manera que la altura, se usará un float para la masa
    m = float(input("Su masa en kilogramos por favor: "))
    
    # Cálculo del IMC: masa (en kg) entre la estatura (en metros) elevada al cuadrado
    IMC = m / est**2
    
    # Le decimos si es menor o mayor de edad
    if e < 18:
        print("Usted es menor de edad")
    else:
        print("Usted es mayor de edad")

    # Ahora mostraremos su IMC + su nombre
    print("IMC: " + str(IMC))

    nombre_completo = nombre + " " + apellido_paterno + " " + apellido_materno

    # Hacemos las distintas validaciones
    if IMC >= 0 and IMC <= 15.99:
        print(nombre_completo + ": Delgadez severa")
    elif IMC >= 16.00 and IMC <= 16.99:
        print(nombre_completo + ": Delgadez moderada")
    elif IMC >= 17.00 and IMC <= 18.49:
        print(nombre_completo + ": Delgadez leve")
    elif IMC >= 18.50 and IMC <= 24.99:
        print(nombre_completo + ": Normal")
    elif IMC >= 25.00 and IMC <= 29.99:
        print(nombre_completo + ": Sobrepeso")
    elif IMC >= 30.00 and IMC <= 34.99:
        print(nombre_completo + ": Obesidad leve")
    elif IMC >= 35.00 and IMC <= 39.00:
        print(nombre_completo + ": Obesidad media")
    else:
        print(nombre_completo + ": Obesidad mórbida")

    # Por cada persona a la que le pedimos los datos debemos restarle una
    personas -= 1 
  
