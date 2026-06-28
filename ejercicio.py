import random
usuarios={
    "Admin":"admin00",
    "Kari":"123"
}

def conau():
    caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    longitud=int(input("Introduce la longitud de tu contraseña: "))
    cge=""
    for i in range(longitud):
        cge+=random.choice(caracteres)
    print("Contraseña generada:",cge)
    return cge

ver=input("Elige un modo: 0-crear contraseña neuva, 1-Ingresar contraseña existente:\n")
while ((ver!='0') and (ver!='1')):
    ver=input("Símbolo no válido. Elija 0 o 1. (0 crear contraseña, mientras que 1 permite el acceso) \n")

if  ver=="1":
    usu=input("Ingresa el nombre de usuario: ")
    if usu not in usuarios:
        print("Usuario no encontrado")
    else:
        acc=input("Ingrese contraseña:")
        if acc!=usuarios[usu]:
            print("¡Contraseña incorrecta!")
        else:
            print("Bienvenido",usu)
            print(usuarios)
    
else:
    print("Se requiere autorización del administrador")
    adm=input("Ingrese usuario del administrador: ")
    if adm!=list(usuarios.keys())[0]:
        print("Acceso denegado")
    else:
        pas=input("Ingresa la contraseña: ")
        if pas!=usuarios[adm]:
            print("Contraseña incorrecta")
        else:
            nueusu=input("Escriba el nuevo usuario: ")
            ocon=input("¿Quieres generar una contraseña automática? 0-No, 1-Sí:\n")
            while ocon!="0" and ocon!="1":
                ocon=input("Opción no válida. Elige 0 o 1: ")
            if ocon=="1":
                nuecontra=conau()
            else:
                nuecontra=input("Escribe la nueva contraseña: ")
            if len(nuecontra) > 0 and len(nueusu) > 0:
                usuarios[nueusu]=nuecontra
                print("¡Tu usuario y contraseña se ha guardado correctamente!")
                print(usuarios)
