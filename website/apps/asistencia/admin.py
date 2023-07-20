from django.contrib import admin
from .models import (
    Instructor,
    Coodinacion,
    Asistencia,
    Programa,
    Horario,
    Ficha,
    Aprendiz,
    Novedad,
    CustomUser
)

# Admin para el modelo Instructor
class InstructorAdmin(admin.ModelAdmin):
    list_display = (
        "documento",
        "nombres_intructor",
        "apellidos_instructor",
        "email_institucional",
    )
    list_display_links = ("documento", "nombres_intructor", "apellidos_instructor")


# Admin para el modelo Coodinacion
class CoodinacionAdmin(admin.ModelAdmin):
    list_display = ("id_coordinacion", "nombre_coordinacion")
    list_display_links = ("id_coordinacion", "nombre_coordinacion")


# Admin para el modelo Asistencia
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ("fecha", "estado_asistencia")
    list_display_links = ("fecha", "estado_asistencia")


# Admin para el modelo Programa
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ("id_programa", "nombre_programa", "coordinacion_programa")
    list_display_links = ("id_programa", "nombre_programa", "coordinacion_programa")


# Admin para el modelo Horario
class HorarioAdmin(admin.ModelAdmin):
    list_display = ("fecha", "hora_entrada", "hora_salida", "salon", "jornada")
    list_display_links = ("fecha", "hora_entrada", "hora_salida", "salon", "jornada")


# Admin para el modelo Ficha
class FichaAdmin(admin.ModelAdmin):
    list_display = ("id_ficha", "nivel_formacion", "programa_ficha")
    list_display_links = (
        "id_ficha",
        "nivel_formacion",
        "programa_ficha",
    )


# Admin para el modelo Aprendiz
class AprendizAdmin(admin.ModelAdmin):
    list_display = (
        "documento_aprendiz",
        "tipo_documento",
        "nombres_aprendiz",
        "apellidos_aprendiz",
        "email_personal_aprendiz",
        "email_institucional_aprendiz",
        "numero_celular",
        "genero_aprendiz",
        "ficha_aprendiz",
    )
    list_display_links = (
        "documento_aprendiz",
        "tipo_documento",
        "nombres_aprendiz",
        "apellidos_aprendiz",
        "email_personal_aprendiz",
        "email_institucional_aprendiz",
        "numero_celular",
        "genero_aprendiz",
        "ficha_aprendiz",
    )

class NovedadAdmin(admin.ModelAdmin):
    list_display = ('id_novedad', 'aprendiz', 'tipo_novedad', 'estado_novedad')
    list_display_links = ('id_novedad', 'aprendiz', 'tipo_novedad')

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_type', 'is_staff', 'is_superuser')
    list_filter = ('user_type', 'is_staff', 'is_superuser')
    search_fields = ('email', 'user_type')


# Registra el modelo y la vista de administrador correspondiente
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Novedad, NovedadAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Coodinacion, CoodinacionAdmin)
admin.site.register(Asistencia, AsistenciaAdmin)
admin.site.register(Programa, ProgramaAdmin)
admin.site.register(Horario, HorarioAdmin)
admin.site.register(Ficha, FichaAdmin)
admin.site.register(Aprendiz, AprendizAdmin)
