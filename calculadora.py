#Calculadora
print('***Super Calculadora***')
operando1 = operando2 = 0
salir= False
while not salir:
    print('''Operaciones que puedes realizar:
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir''')
    opcion= int(input('¿Qué operación deseas realizar?: '))
    if opcion==1:
        operando1= float(input('Ingresa el primer número: '))
        operando2= float(input('Ingresa el segundo número: '))
        print(f'El resultado de la suma es: {operando1+operando2}\n')
    elif opcion==2:
        operando1= float(input('Ingresa el primer número: '))
        operando2= float(input('Ingresa el segundo número: '))
        print(f'El resultado de la resta es: {operando1-operando2}\n')
    elif opcion==3:
        operando1= float(input('Ingresa el primer número: '))
        operando2= float(input('Ingresa el segundo número: '))
        print(f'El resultado de la multiplicación es: {operando1*operando2}\n')
    elif opcion==4:
        operando1= float(input('Ingresa el primer número: '))
        operando2= float(input('Ingresa el segundo número: '))
        if operando2!=0:
            print(f'El resultado de la división es: {operando1/operando2}\n')
        else:
            print('No se puede dividir entre 0\n')
    elif opcion==5:
        print('Gracias por utilizar la calculadora, hasta luego!')
        salir= True
    else:
        print('Opción no válida, intenta de nuevo\n')
