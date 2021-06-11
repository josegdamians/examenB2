from django.db import models

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apat = models.CharField(max_length=50)
    amat = models.CharField(max_length=50)
    fechanacimiento = models.DateField()
    correo = models.CharField(max_length=50)
    genero = models.CharField(max_length=1)
    telefono = models.CharField(max_length=12)
    celular = models.CharField(max_length=10)
    fechaingreso = models.DateField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " " + self.apat + " " + self.amat