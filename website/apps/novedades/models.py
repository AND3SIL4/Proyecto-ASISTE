from django.db import models
from apps.asistencia.models import Aprendiz

# Create your models here.
class Novedad(models.Model):
    class Meta:
      verbose_name = 'Novedad'
      verbose_name_plural = 'Novedades'


    documento_aprendiz = models.ForeignKey(Aprendiz, on_delete=models.CASCADE)
    id_novedad  = models.IntegerField(primary_key=True)
    tipo_novedad = models.CharField(max_length=20)
    observaciones = models.TextField(max_length=300)
    archivo_adjunto = models.FileField(upload_to='pdfs/')
    estado_novedad = models.BooleanField(default=False)
    
    def __str__(self):
      return f'{self.tipo_novedad} {self.id_novedad}'