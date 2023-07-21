from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from ckeditor.fields import RichTextField

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    USER_TYPES = (
        ('Aprendiz', 'Aprendiz'),
        ('Instructor', 'Instructor'),
        ('Coordinacion', 'Coordinación'),
        ('Bienestar', 'Bienestar'),
    )
    username = None
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name='customuser_set' # Puedes cambiar el nombre si lo deseas
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_set' # Puedes cambiar el nombre si lo deseas
    )

    def __str__(self):
        return f"{self.email} - {self.user_type}"

class Instructor(models.Model):
    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructores"

    documento = models.IntegerField(primary_key=True)
    nombres_intructor = models.CharField(max_length=45)
    apellidos_instructor = models.CharField(max_length=45)
    email_institucional = models.CharField(max_length=50)
    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.nombres_intructor} {self.apellidos_instructor}"

class Coodinacion(models.Model):
    class Meta:
        verbose_name = "Coodinacion"
        verbose_name_plural = "Coordinaciones"

    id_coordinacion = models.IntegerField(primary_key=True, unique=True)
    nombre_coordinacion = models.CharField(max_length=45, choices=[('Teleinformatica', 'Teleinformatica')])

    def __str__(self):
        return self.nombre_coordinacion

class Programa(models.Model):
    class Meta:
        verbose_name = "Programa"
        verbose_name_plural = "Programas"

    id_programa = models.IntegerField(primary_key=True)
    nombre_programa = models.CharField(max_length=45, choices=[('ADSO', 'ADSO')])
    coordinacion_programa = models.ForeignKey(Coodinacion, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre_programa}"

class Horario(models.Model):
    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"

    fecha = models.DateField()
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField()
    salon = models.IntegerField()
    jornada = models.CharField(max_length=10, choices=[('Diurna', 'Diurna'), ('Tarde', 'Tarde'), ('Nocturna', 'Nocturna')])
    asignatura = models.CharField(max_length=45)


    def __str__(self):
        return f"{self.fecha}"

class Ficha(models.Model):
    class Meta:
        verbose_name = "Ficha"
        verbose_name_plural = "Fichas"

    id_ficha = models.IntegerField(primary_key=True)
    horario_ficha = models.ManyToManyField(Horario)
    instructor_ficha = models.ManyToManyField(Instructor)
    nivel_formacion = models.CharField(max_length=20)
    programa_ficha = models.ForeignKey(Programa, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_ficha}"

class Aprendiz(models.Model):
    GENERO_CHOICES = (
        ("Masculino", "Masculino"),
        ("Femenino", "Femenino"),
        ("Homosexual", "Homosexual"),
        ("Bisexsual", "Bisexsual"),
        ("Transexual", "Transexual"),
    )

    documento_aprendiz = models.IntegerField(primary_key=True)
    tipo_documento = models.CharField(max_length=20, choices=[('Cedula','Cedula de ciudadania'),('Tarjeta','Tarjeta de identidad')])
    nombres_aprendiz = models.CharField(max_length=45)
    apellidos_aprendiz = models.CharField(max_length=45)
    email_personal_aprendiz = models.CharField(max_length=45)
    email_institucional_aprendiz = models.CharField(max_length=45)
    numero_celular = models.IntegerField()
    genero_aprendiz = models.CharField(max_length=10, choices=GENERO_CHOICES)
    ficha_aprendiz = models.ForeignKey(Ficha, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "Aprendiz"
        verbose_name_plural = "Aprendices"
        ordering = ('-nombres_aprendiz',)

    def __str__(self):
        return f"{self.nombres_aprendiz} {self.apellidos_aprendiz}"
    
class Novedad(models.Model):
    ESTADO_NOVEDAD_CHOICES = (
        (True, 'Aceptada'),
        (False, 'No aceptada'),
    )

    class Meta:
        verbose_name = 'Novedad'
        verbose_name_plural = 'Novedades'

    aprendiz = models.ForeignKey(Aprendiz, on_delete=models.CASCADE)
    id_novedad  = models.AutoField(primary_key=True)
    tipo_novedad = models.CharField(max_length=10,choices=[('Calamidad', 'Calamidad domestica'), ('Medica', 'Novedad medica')])
    observaciones = RichTextField(max_length=30, default='')
    archivo_adjunto = models.FileField(upload_to='pdfs/')
    estado_novedad = models.BooleanField(default=False, choices=ESTADO_NOVEDAD_CHOICES)

    def __str__(self):
        return f'{self.tipo_novedad} {self.id_novedad}'
    
class Asistencia(models.Model):
    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"

    ESTADO_ASISTENCIA_CHOICES = (
    ('Asiste', 'Asiste'),
    ('Falla', 'Falla'),
    ('Novedad', 'Novedad'),
    )

    aprendiz = models.ForeignKey(Aprendiz, on_delete=models.CASCADE)
    fecha = models.DateField()
    estado_asistencia = models.CharField(max_length=10, choices=ESTADO_ASISTENCIA_CHOICES)
    novedad = models.OneToOneField(Novedad, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.aprendiz} - {self.fecha} - {self.estado_asistencia}"

    # novedad = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)