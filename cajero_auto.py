print('***Cajero Automatico***')
saldo= 1000.10 #saldo inicial
salir= False
while not salir:
    print(f'''Operaciones que puedes realizar:
    1. Consultar saldo
    2. Retirar dinero
    3. Depositar dinero
    4. Salir''')
    opcion= int(input('¿Qué operación deseas realizar?: '))
    if opcion==1:
        print(f'Tu saldo actual es: ${saldo:.2f}\n')
    elif opcion==2:
        retiro= float(input('¿Cuánto dinero deseas retirar?: '))
        #validacion
        if retiro<=saldo:
            saldo-= retiro
            print(f'Has retirado: ${retiro}')
            print(f'Tu saldo actual es: ${saldo:.2f}\n')
        else:
            print(f'No tienes dinero suficiente, tu saldo es: ${saldo:.2f}\n')
    elif opcion==3:
        deposito= float(input('¿Cuánto dinero deseas depositar?: '))
        saldo+= deposito
        print(f'Has depositado: ${deposito}')
        print(f'Tu saldo actual es: ${saldo:.2f}\n') 
    elif opcion==4:
        print('Gracias por utilizar el cajero automático, hasta luego!')
        salir= True
    else:
        print('Opción no válida, intenta de nuevo\n')
        