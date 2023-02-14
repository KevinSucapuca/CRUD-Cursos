from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(primary_key=True,  max_length=6)
    nombre = models.CharField(max_length=100)
    creditos = models.PositiveBigIntegerField()
    
    def __str__(self):
        text = "{0}({1})"
        return text.format(self.nombre, self.creditos)
        
    

    
