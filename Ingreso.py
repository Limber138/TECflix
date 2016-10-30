#ingreso de usuarios

#Selección entre usuario o administrador.


usuarios0= {}
usuarios2= {"King": "PandOso123"}

contador = 0
while contador==0:
    usuario = int(input("0 para registrarse como usuario, 1 para ingresar como usuario y 2 para ingresar como administrador, 3 para salir"))
    while usuario == 0:
        x = str(input("Digite su nombre de usuario"))
        y = input("Digite su contraseña")
        usuarios0[x] = y
        print("Su usuario ha sido creado exiosamente")
        print ("su nombre de usuario es : ", x )
        print("su contraseña es :", usuarios0[x])
        usuario= int(input("Digite 1 para ingrear, Digite 0 para cambiar los datos"))


    while usuario ==1:
        nombre = input("Digite su nombre de usuario")
        contra = input("Digite su contraseña")
        if contra == usuarios0[nombre]:
            print ("Wow your code is working")

        else:
            print("Contraseña equivocada")

    while usuario == 2:
        nombre = input("Digite su nombre de usuario de administrador")
        contraseña = input("Digite su contraseña")

        if contraseña == usuarios2[nombre]:
            eleccion = int(input("Si desea agregar otro administrador digite 1"))
            if eleccion == 1:
                x = str(input("Digite su nombre de usuario"))
                y = input("Digite su contraseña")
                usuarios2[x] = y
                print("Su usuario ha sido creado exiosamente")
                print("su nombre de usuario es : ", x)
                print("su contraseña es :", usuarios2[x])
                print("Este usuario es permanente, no olvide sus usuario ni contraseña")



        else:
            print ("Contaseña equivocada")

    if usuario == 3:
        print("Gracias por su visita")
        contador = 1

    else:
        print("Por favor ingrese nuevamente")
