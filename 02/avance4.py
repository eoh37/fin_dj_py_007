# Importar las librerías necesarias
import tkinter as tk
from tkinter import messagebox

# Clase que define la interfaz gráfica
class VideoUploaderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pro-Gol Watch")
        self.geometry("400x300")

        # Definir variables de control
        self.id_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.cantidad_var = tk.StringVar()
        self.videos = []

        # Crear y configurar widgets
        tk.Label(self, text="ID (Número de nómina):").pack()
        tk.Entry(self, textvariable=self.id_var).pack()

        tk.Label(self, text="Nombre completo:").pack()
        tk.Entry(self, textvariable=self.nombre_var).pack()

        tk.Label(self, text="Cantidad de videos a subir:").pack()
        tk.Entry(self, textvariable=self.cantidad_var).pack()

        tk.Button(self, text="Aceptar", command=self.mostrar_confirmacion).pack()

    def mostrar_confirmacion(self):
        # Obtener la información ingresada por el usuario
        id_num = self.id_var.get()
        nombre = self.nombre_var.get()
        cantidad = self.cantidad_var.get()

        # Mostrar ventana emergente de confirmación
        confirmacion = messagebox.askquestion(
            "Confirmar",
            f"Bienvenido {nombre}, tu número de nómina es {id_num} y estás intentando subir {cantidad} videos. ¿Es correcta la información?",
        )

        if confirmacion == "yes":
            self.capturar_videos(int(cantidad))

    def capturar_videos(self, cantidad):
        for i in range(cantidad):
            # Lógica para capturar información de los videos
            # Puedes usar ciclos y entradas de texto para cada video

            video_titulo = input("Título del video: ")
            video_nombre = input("Nombre del video: ")
            video_extension = input("Extensión del video: ")
            video_tamano = float(input("Tamaño del video (en MB): "))

            # Validar información y agregar a la lista de videos
            # Puedes implementar las validaciones aquí

            video_info = {
                "titulo": video_titulo,
                "nombre": video_nombre,
                "extension": video_extension,
                "tamano": video_tamano,
            }
            self.videos.append(video_info)

        # Lógica para guardar los datos en la base de datos
        # Puedes usar Django ORM para interactuar con la base de datos

        # Una vez guardados los datos, mostrar mensaje de éxito
        messagebox.showinfo("Éxito", "Datos guardados correctamente.")


if __name__ == "__main__":
    app = VideoUploaderApp()
    app.mainloop()
