usuarios={
    "Admin":"admin00",
    "Kari":"123"
}
ver=input("Elige un modo: 0-crear contraseña neuva, 1-Ingresar contraseña existente:\n")
while ((ver!='0') and (ver!='1')):
    ver=input("Símbolo no válido. Elija 0 o 1. (0 crear contraseña, mientras que 1 permite el acceso) \n")

if  ver=="1":
    usu=input("Ingresa el nombre de usuario")
    if usu not in usuarios:
        print("Usuario no encontrado")
    else:
        acc=input("Ingrese contraseña:")
        if acc!=usuarios[usu]:
            print("¡Contraseña incorrecta!")
        else:
            print("Bienvenido",usu)
    
else:
    print("Se requiere autorización del administrador")
    adm=input("Ingrese usuario del administrador: ")
    if adm!="Admin":
        print("Acceso denegado")
    else:
        pas=input("Ingresa la contraseña: ")
        if pas!=usuarios[adm]:
            print("Contraseña incorrecta")
        else:
            nueusu=input("Escriba el nuevo usuario: ")
            nuecontra=input("Escribe la nueva contraseña: ")
            if len(nuecontra) > 0 and len(nueusu) > 0:
                usuarios[nueusu]=nuecontra
                print("¡Tu contraseña y usuario se ha guardado correctamente!")
                print(usuarios)
