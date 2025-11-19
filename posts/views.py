from django.shortcuts import render , redirect
from .models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.


def feed (request):
    posts = Post.objects.all ().order_by("-fecha")
    return render (request, "index.html",{"posts": posts})


#login_required


def subir_post (request):
    if request.method == "POST":
        imagen =  request.FILES ["imagen"]
        descripcion = request.POST.get ("descripcion", "")
        tipo = request.POST.get ("tipo", "")
        if tipo not in ["libro", "pelicula"]:                        #solo permite libros o peliculas
            return render (request, "subir.html", {
                "error": "Solo puedes subir contenido sobre libros o peliculas." })
        Post.objects.create(usuario=request.user, imagen = imagen, descripcion = descripcion, tipo = tipo)
        return redirect ("feed")
    return render (request, "subir.html")


def reaccion (request, id, tipo):
    post = Post.objects.get (id=id)
    if tipo == "like":
        post.likes += 1
    elif tipo == "dislike":
        post.dislikes += 1
    elif tipo == "triste":
        post.triste += 1
    elif tipo == "bien":
        post.bien += 1

    post.save()
    return redirect ("feed")



def calificar (request, id):
    post = Post.objects.get (id=id)
    if request.method == "POST":
        try:
            numero = int(request.POST.get("numero"))
        except:
            return redirect ("feed") #si no es numero, no hace nada
        if 1 <= numero <= 5: 
            post.calificacion = numero 
            post.save ()
    return redirect ("feed")
