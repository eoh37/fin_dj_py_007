from django.db import models

# Create your models here.
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    id = models.CharField(max_length=10, primary_key=True)

class Video(models.Model):
    nombre_video = models.CharField(max_length=50)
    extension_video = models.CharField(max_length=5)
    tamano_video = models.DecimalField(max_digits=10, decimal_places=2)

class UsuarioVideo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
