from django.db import models
from django.contrib.auth.models import User
# Create your models here.

TIPOS = (
         ("libro", "Libro"),
         ("pelicula", "Pelicula")
)


class Post(models.Model):
    usuario = models.ForeignKey (User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    imagen = models.ImageField (upload_to="post/")
    descripcion = models.TextField (blank = True)
    fecha = models.DateTimeField (auto_now_add= True)
    likes =  models.IntegerField (default= 0)           #reacciones 
    dislikes = models.IntegerField (default= 0)
    triste = models.IntegerField (default= 0)
    bien = models.IntegerField (default= 0)
    calificacion = models.IntegerField (default= 0)        #calificacion 


    def __str__ (self):
      return (f"{self.usuario.username} - {self.fecha}")
