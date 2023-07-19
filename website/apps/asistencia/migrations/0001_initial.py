# Generated by Django 4.2.3 on 2023-07-19 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id_asistencia', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('estado_asistencia', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Asistencia',
                'verbose_name_plural': 'Asistencias',
            },
        ),
        migrations.CreateModel(
            name='Coodinacion',
            fields=[
                ('id_coordinacion', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre_coordinacion', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Coodinacion',
                'verbose_name_plural': 'Coordinaciones',
            },
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora_entrada', models.TimeField()),
                ('hora_salida', models.TimeField()),
                ('salon', models.IntegerField()),
                ('jornada', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('documento', models.IntegerField(max_length=20, primary_key=True, serialize=False)),
                ('nombres_intructor', models.CharField(max_length=45)),
                ('apellidos_instructor', models.CharField(max_length=45)),
                ('email_institucional', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Instructor',
                'verbose_name_plural': 'Instructores',
            },
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id_programa', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_programa', models.CharField(max_length=45)),
                ('coordinacion_programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.coodinacion')),
            ],
            options={
                'verbose_name': 'Programa',
                'verbose_name_plural': 'Programas',
            },
        ),
        migrations.CreateModel(
            name='Ficha',
            fields=[
                ('id_ficha', models.IntegerField(primary_key=True, serialize=False)),
                ('nivel_formacion', models.CharField(max_length=20)),
                ('horario_ficha', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='asistencia.horario')),
                ('instructor_ficha', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='asistencia.instructor')),
                ('programa_ficha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.programa')),
            ],
            options={
                'verbose_name': 'Ficha',
                'verbose_name_plural': 'Fichas',
            },
        ),
        migrations.CreateModel(
            name='Aprendiz',
            fields=[
                ('documento_aprendiz', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_documento', models.CharField(max_length=20)),
                ('nombres_aprendiz', models.CharField(max_length=45)),
                ('apellidos_aprendiz', models.CharField(max_length=45)),
                ('email_personal_aprendiz', models.CharField(max_length=45)),
                ('email_institucional_aprendiz', models.CharField(max_length=45)),
                ('numero_celular', models.IntegerField(max_length=10)),
                ('genero_aprendiz', models.CharField(max_length=1)),
                ('asistencia', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='asistencia.asistencia')),
                ('ficha_aprendiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.ficha')),
            ],
            options={
                'verbose_name': 'Aprendiz',
                'verbose_name_plural': 'Aprendices',
            },
        ),
    ]