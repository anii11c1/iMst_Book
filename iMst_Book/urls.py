from django.contrib import admin
from django.urls import path
from posts.views import feed, subir_post, reaccion, calificar
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
               path("admin/", admin.site.urls),
               path("", feed, name = "feed"),
               path("subir/", subir_post, name = "subir"),
               path ("reaccion/<int:id>/<str:tipo>/", reaccion, name = "reaccion"),  
               path ("calificar/<int:id>/", calificar, name= "calificar") 
               ]




urlpatterns += static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

