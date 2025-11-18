
#2

from django.db import models
from django.contrib.auth.models import User 


#3

from django.contrib import admin
from .models import Post
admin.site.register (Post)

#4

from django.shortcuts import render, redirect
from .models import Post 
from django.contrib.auth.decorators import login_required


#5
from django.contrib import admin
from django.urls import path
from posts.views import feed, subir_post, like 

#7
from django.conf import settings
from django.conf.urls.static import static




class Post(models.Model):
    usuario = models.ForeignKey (User, on_delete=models.CASCADE)
    imagen = models.ImageField (upload_to="post/")
    descripcion = models.TextField (black = True)
    fecha = models.DateTimeField (auto_now_add= True)



def __str__ (self):
    return (f"{self.usuario.username} - {self.fecha}")




def subir_post (request):
    if request.method == "POST":
        imagen =  request.FILES ["imagen"]
        descripcion = request.POST.get ("descripcion", "")
        
        Post.objects.create(autor=request.user, imagen = imagen, descripcion = descripcion)
        return redirect ("feed" "")
    return render (request, "subir.html")


def feed (requet):
    posts = Post.objects.all ().order_by("-fecha")
    return render (request, "feed.html",{"posts": posts})


def like (request, id):
    post = Post.objects.get (id=id)
    post.likes += 1
    post.save()
    return redirect ("feed")


urlpatterns = [path('admin/', admin.site.urls),
               path('', feed, name = "feed"),
               path('subir/', subir_post, name = "subir"),
               path('like/<int:id>/', like, name = "like")]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)