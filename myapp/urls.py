from django.urls import path
from .views import UsuarioListCreate, UsuarioDetail

urlpatterns = [
    path('usuarios/', UsuarioListCreate.as_view(), name='usuario-list-create'),
    path('usuarios/<int:id>/', UsuarioDetail.as_view()),
]
