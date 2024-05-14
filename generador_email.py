#Generador de emails

print('***Sistema Generador de Emails***')
nombre= input('\nIngresa tu nombre: ')
apellido= input('Ingresa tu apellido: ')
email_gen= f'{nombre.lower()}.{apellido.lower()}@gmail.com'
print(f'''\nHola {nombre} {apellido}!''')
print(f'Tu email generado por el sistema es: {email_gen}')
