while True:
    print("Calculadora")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
        resultado = numero1 + numero2
        print(f"El resultado es, {resultado}")

    elif opcion == 2:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
        resultado = numero1 - numero2
        print(f"El resultado es, {resultado}")

    elif opcion == 3:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
        resultado = numero1 * numero2
        print(f"El resultado es, {resultado}")

    elif opcion == 4:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"El resultado es, {resultado}")
        else:
            print("Error: No se puede dividir entre cero")

    elif opcion == 5:
        print("Hasta luego")
        break

    else:
        print("Opción no válida. Intenta nuevamente.")