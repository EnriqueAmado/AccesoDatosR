from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='usuarios')

    def __str__(self):
        return self.nombre
