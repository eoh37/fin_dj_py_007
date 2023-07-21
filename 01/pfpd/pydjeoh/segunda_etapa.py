class Persona:
    def __init__(self):
        self.nombre = ""
        self.id = ""

    def capturar_nombre(self):
        self.nombre = input("Ingrese su nombre: ")

    def capturar_id(self):
        self.id = input("Ingrese su número de nómina: ")

    def imprimir_nombre(self):
        print("Nombre: ", self.nombre)

    def imprimir_id(self):
        print("Número de nómina: ", self.id)


class Videos:
    def __init__(self):
        self.nombre_video = ""
        self.extension_video = ""
        self.tamano_video = ""

    def capturar_nombre_video(self):
        self.nombre_video = input("Ingrese el nombre del video: ")

    def capturar_extension_video(self):
        self.extension_video = input("Ingrese la extensión del video: ")

    def capturar_tamano_video(self):
        self.tamano_video = input("Ingrese el tamaño del video (en megas): ")

    def imprimir_nombre_video(self):
        print("Nombre del video: ", self.nombre_video)

    def imprimir_extension_video(self):
        print("Extensión del video: ", self.extension_video)

    def imprimir_tamano_video(self):
        print("Tamaño del video: ", self.tamano_video)


def guardar_informacion(persona, videos):
    with open("salida2.txt", "w") as archivo:
        archivo.write(f"{persona.id} | {persona.nombre} | {len(videos)} | ")
        for video in videos:
            archivo.write(" | ".join(video) + " | ")
        archivo.write("\n")


def segunda_etapa():
    persona = Persona()
    videos = []

    persona.capturar_nombre()
    persona.capturar_id()

    print("\nInformación de la Persona:")
    persona.imprimir_nombre()
    persona.imprimir_id()

    confirmacion = input("\n¿Es correcta la información? (Sí/No): ")

    if confirmacion.lower() == "si":
        cantidad_videos = int(input("\nIngrese la cantidad de videos que desea subir: "))

        for i in range(cantidad_videos):
            print(f"\nCapturando información del Video {i+1}:")
            video = Videos()
            video.capturar_nombre_video()
            video.capturar_extension_video()
            video.capturar_tamano_video()
            videos.append([video.nombre_video, video.extension_video, video.tamano_video])

        print("\nInformación de la Persona:")
        persona.imprimir_nombre()
        persona.imprimir_id()

        print("\nInformación de los Videos:")
        for i, video in enumerate(videos):
            print(f"\nVideo {i+1}:")
            print("Nombre: ", video[0])
            print("Extensión: ", video[1])
            print("Tamaño: ", video[2])

        guardar_informacion(persona, videos)
        print("\nInformación guardada correctamente en salida2.txt.")

    elif confirmacion.lower() == "no":
        salir = input("¿Desea salir del sistema? (Sí/No): ")
        if salir.lower() == "si":
            print("\nMuchas gracias por haber usado nuestro sistema. ¡Hasta pronto!")


segunda_etapa()
