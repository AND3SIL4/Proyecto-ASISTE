from django.db import models

class Instructor(models.Model):
    class Meta:
        verbose_name = 'Instructor'
        verbose_name_plural = 'Instructores'

    documento = models.IntegerField(primary_key=True,max_length=20)
    nombres_intructor = models.CharField(max_length=45)
    apellidos_instructor = models.CharField(max_length=45)
    email_institucional = models.CharField(max_length=50)

    def __str__(self):
      return f'{self.nombres_intructor} {self.apellidos_instructor}'

class Coodinacion(models.Model):
    class Meta:
        verbose_name = 'Coodinacion'
        verbose_name_plural = 'Coordinaciones'

    id_coordinacion = models.IntegerField(primary_key=True, unique=True)
    nombre_coordinacion = models.CharField(max_length=45)

    def __str__(self) :
        return self.nombre_coordinacion
    
class Asistencia(models.Model):
    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
    
    id_asistencia = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    estado_asistencia = models.BooleanField()

    def __str__(self):
      return f'{self.estado_asistencia}'

class Programa(models.Model):
    class Meta:
        verbose_name = 'Programa'
        verbose_name_plural = 'Programas'

    id_programa = models.IntegerField(primary_key=True)
    nombre_programa = models.CharField(max_length=45)
    coordinacion_programa = models.ForeignKey(Coodinacion, on_delete=models.CASCADE)

    def __str__(self):
      return f'{self.nombre_programa}'
  
class Horario(models.Model):
    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    fecha = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    salon = models.IntegerField()
    jornada = models.CharField(max_length=10)

    def __str__(self):
      return f'{self.jornada}'

class Ficha(models.Model):
    class Meta:
        verbose_name = 'Ficha'
        verbose_name_plural = 'Fichas'
    
    id_ficha = models.IntegerField(primary_key=True)
    horario_ficha = models.ForeignKey(Horario, on_delete=models.DO_NOTHING)
    instructor_ficha = models.ManyToManyField(Instructor)
    nivel_formacion = models.CharField(max_length=20)
    programa_ficha = models.ForeignKey(Programa, on_delete=models.CASCADE)

    def __str__(self):
      return f'{self.id_ficha}'
    

class Aprendiz(models.Model):
  GENERO_CHOICES = (
  ('M', 'Masculino'),
  ('F', 'Femenino'),
  )
  class Meta:
      verbose_name = 'Aprendiz'
      verbose_name_plural = 'Aprendices'

  documento_aprendiz = models.IntegerField(primary_key=True)
  tipo_documento = models.CharField(max_length=20)
  nombres_aprendiz = models.CharField(max_length=45)
  apellidos_aprendiz = models.CharField(max_length=45)
  email_personal_aprendiz = models.CharField(max_length=45)
  email_institucional_aprendiz = models.CharField(max_length=45)
  numero_celular = models.IntegerField(max_length=10)
  genero_aprendiz = models.CharField(max_length=1)
  ficha_aprendiz = models.ForeignKey(Ficha, on_delete=models.CASCADE)
  asistencia = models.ForeignKey(Asistencia, on_delete=models.DO_NOTHING)

  def __str__(self):
      return f'{self.nombres_aprendiz} {self.apellidos_aprendiz}'
  
        
