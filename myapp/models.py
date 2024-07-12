from django.contrib.auth.models import User
from django.db import models

class Paciente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, unique=True, blank=True, null=True)
    pasaporte = models.CharField(max_length=20, unique=True, blank=True, null=True)

    def __str__(self):
        return self.usuario.username

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Establecimiento(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.servicio} - {self.fecha} {self.hora}"

class Bono(models.Model):
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.tipo

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    bonos = models.ManyToManyField(Bono, blank=True)
    medicamentos = models.ManyToManyField(Medicamento, through='DetalleCompra')
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

class Pago(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)

class Configuracion(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    notificaciones = models.BooleanField(default=True)
    cambio_contrasena = models.BooleanField(default=False)
    cambio_nombre_usuario = models.BooleanField(default=False)
    privacidad = models.CharField(max_length=100, choices=[('publico', 'Público'), ('privado', 'Privado')])
    tamano_letra = models.CharField(max_length=10, choices=[('pequeno', 'Pequeño'), ('mediano', 'Mediano'), ('grande', 'Grande')])

    def __str__(self):
        return f"Configuración de {self.paciente.usuario.username}"