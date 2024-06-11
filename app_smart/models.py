from django.db import models

# Create your models here.

class Sensor(models.Model):
    TIPO_SENSOR_CHOICE = [
        ('Temperatura', 'Temperatura'),
        ('Umidade', 'Umidade'),
        ('Contador', 'Contador'),
        ('Luminosidade', 'Luminosidade'),
    ]

    tipo = models.CharField(max_length=50, choices=TIPO_SENSOR_CHOICE)
    mac_address = models.CharField(max_length=20, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    localizacao = models.CharField(max_length=100)
    responsavel = models.CharField(max_length=100)
    unidade_medida = models.CharField(max_length=20, blank=True, null=True)
    observacao = models.TextField(blank=True)
    status_operacional = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tipo} - {self.localizacao}"
    
# model para armazenar os dados de temperatura
class TemperaturaData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    valor = models.FloatField() #valor da temp em graus celsius
    #timestamp = models.DateTimeField(auto_now_add=True) 
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"Temperatura: {self.valor} ºC - {self.timestamp}"
    
class UmidadeData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    valor = models.FloatField() #valor da temp em graus celsius
    #timestamp = models.DateTimeField(auto_now_add=True) 
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"Umidade: {self.valor} % - {self.timestamp}"

class ContadorData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    #timestamp = models.DateTimeField(auto_now_add=True) 
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"Contagem: {self.valor} % - {self.timestamp}"
    
class LuminosidadeData(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    valor = models.FloatField() #valor da temp em graus celsius
    #timestamp = models.DateTimeField(auto_now_add=True) 
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return f"Luminosidade: {self.valor} Lux - {self.timestamp}"