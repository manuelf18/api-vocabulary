from django.urls import path
from vocabulario import views

urlpatterns = [
    path('', views.read_vocabulario_list),
    path('palabra_dia', views.random_palabra_view),
    path('insertar_palabra', views.create_palabra),
    path('buscar_palabra',views.get_all_by_palabra)

    
]