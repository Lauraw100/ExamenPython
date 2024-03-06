#2. Elabore un programa en Python que permita leer la información de un usuario
#Y la almacene en un diccionario.
import os
personal={}
def allDatos():   

    id=int(input('Ingrese su identificacion:\n'))
    nombre=input('Ingrese sus nombre\n')
    apellidos=input('Ingrese sus apellidos\n')
    ubicacion=input('Ingrese su ubicacion\n')
    direccion=input('Ingrese su direccion\n')
    ciudad=input('Ingrese su ciudad\n')
    longitud=input('Ingrese su longitud\n')
    latitud=input('Ingrese su latitud\n')
    email=input('Ingrese su email\n')
    edad=int(input('Ingrese su edad:\n'))
    ocupacion=input('Ingrese su ocupacion\n')

    personal={
            "id":id,
            "nombre":nombre,
            "apellidos":apellidos,
            "ubicacion":ubicacion,
            "direccion":{
                    "direccion":direccion,
                    "ciudad":ciudad,
                    "longitud":longitud,
                    "latitud":latitud
                },    
            "email":email,
            "edad":edad,
            "ocupacion":ocupacion
    }
        
    print('Datos agregados')    
    print(personal)
    os.system('pause')
