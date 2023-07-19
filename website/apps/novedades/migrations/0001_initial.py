# Generated by Django 4.2.3 on 2023-07-19 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asistencia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Novedad',
            fields=[
                ('id_novedad', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo_novedad', models.CharField(max_length=20)),
                ('observaciones', models.TextField(max_length=300)),
                ('archivo_adjunto', models.FileField(upload_to='pdfs/')),
                ('estado_novedad', models.BooleanField(default=False)),
                ('documento_aprendiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.aprendiz')),
            ],
            options={
                'verbose_name': 'Novedad',
                'verbose_name_plural': 'Novedades',
            },
        ),
    ]