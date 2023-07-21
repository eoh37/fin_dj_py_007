def pedir_informacion():
    # Pedir al usuario su Id (número de nómina)
    id_usuario = input("Ingrese su número de nómina: ")

    # Pedir al usuario su nombre
    nombre_usuario = input("Ingrese su nombre: ")

    # Preguntar al usuario la cantidad de videos que subirá
    cantidad_videos = input("Ingrese la cantidad de videos que desea subir: ")

    return id_usuario, nombre_usuario, cantidad_videos


def capturar_videos(cantidad_videos):
    videos = []
    for i in range(int(cantidad_videos)):
        # Capturar información de cada video
        print(f"\nInformación del video {i+1}:")
        titulo = input("Ingrese el título del video: ")
        nombre = input("Ingrese el nombre del video: ")
        extension = input("Ingrese la extensión del video: ")
        tamaño = input("Ingrese el tamaño del video (en MB): ")

        videos.append((titulo, nombre, extension, tamaño))
    
    return videos


def validar_formato(cadena, tipo):
    # Validar formato de la cadena según el tipo especificado
    if tipo == "id":
        if not cadena.isalnum():
            return "Nómina en formato incorrecto. Debe capturar solo números y letras."

    elif tipo == "nombre":
        if not cadena.isalpha():
            return "Nombre de usuario en formato incorrecto. Debe capturar solo letras."

    elif tipo == "cantidad":
        if not cadena.isdigit():
            return "Cantidad de videos en formato incorrecto. Debe capturar solo números."

    elif tipo == "titulo" or tipo == "nombre" or tipo == "extension":
        if not cadena.isalnum():
            return f"{tipo.capitalize()} del video en formato incorrecto. Debe capturar solo números y letras."

    elif tipo == "tamaño":
        if not cadena.isdigit():
            return "Tamaño del video en formato incorrecto. Debe capturar solo números."
        if float(cadena) < 0 or float(cadena) > 3:
            return "El archivo no debe pesar más de 3 MB."

    return None


def validar_capturas(id_usuario, nombre_usuario, cantidad_videos, videos):
    # Validar cada captura de información del usuario
    errores = []
    error = validar_formato(id_usuario, "id")
    if error:
        errores.append(error)

    error = validar_formato(nombre_usuario, "nombre")
    if error:
        errores.append(error)

    error = validar_formato(cantidad_videos, "cantidad")
    if error:
        errores.append(error)

    for video in videos:
        error = validar_formato(video[0], "titulo")
        if error:
            errores.append(error)

        error = validar_formato(video[1], "nombre")
        if error:
            errores.append(error)

        error = validar_formato(video[2], "extension")
        if error:
            errores.append(error)

        error = validar_formato(video[3], "tamaño")
        if error:
            errores.append(error)

    return errores


def mostrar_validaciones(errores):
    # Mostrar los mensajes de validación
    for error in errores:
        print(error)


def guardar_informacion(id_usuario, nombre_usuario, cantidad_videos, videos):
    # Guardar la información en el archivo salida.txt
    with open("salida.txt", "w") as archivo:
        archivo.write(f"{id_usuario} | {nombre_usuario} | {cantidad_videos} | ")
        for video in videos:
            archivo.write(" | ".join(video) + " | ")
        archivo.write("\n")


def primera_etapa():
    while True:
        id_usuario, nombre_usuario, cantidad_videos = pedir_informacion()

        print(f"\nBienvenido {nombre_usuario},")
        print(f"Tu número de nómina es {id_usuario} y estás intentando subir {cantidad_videos} videos.")

        confirmacion = input("¿Es correcta la información? (Sí/No): ")

        if confirmacion.lower() == "si":
            videos = capturar_videos(cantidad_videos)
            errores = validar_capturas(id_usuario, nombre_usuario, cantidad_videos, videos)

            if errores:
                mostrar_validaciones(errores)
            else:
                guardar_informacion(id_usuario, nombre_usuario, cantidad_videos, videos)
                print("Información guardada correctamente en salida.txt.")
                break

        elif confirmacion.lower() == "no":
            salir = input("¿Desea salir del sistema? (Sí/No): ")
            if salir.lower() == "si":
                print("Muchas gracias por haber usado nuestro sistema. ¡Hasta pronto!")
                break

        print("")

        
primera_etapa()
