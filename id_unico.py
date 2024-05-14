#Generador ID Unico
from random import randint

print('***Sistema Generador ID Unico***')

nombre= input('Ingresa tu nombre: ')
nombre_2 = nombre[0:2].upper()
apellido = input('Ingresa tu apellido: ')
apellido_2 = apellido[0:2].upper()
anio = input('Ingresa tu año de nacimiento (YYYY): ')
anio_2 = anio[2:4]
#4digitos aleatorios
aleatorio = randint(0,9999)

id_unico = f'{nombre_2}{apellido_2}{anio_2}{aleatorio}'
print(f'''\nHola {nombre}{apellido}!
Tu ID unico generado por el sistema es: {id_unico}
Gracias por utilizar el sistema, hasta luego!''')