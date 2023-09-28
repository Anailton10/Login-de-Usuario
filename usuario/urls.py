from django.urls import path
from usuario import views


urlpatterns = [
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('validação/', views.validação, name='validação'),
    path('recuperar/', views.recuperar, name='recuperar'),
]
