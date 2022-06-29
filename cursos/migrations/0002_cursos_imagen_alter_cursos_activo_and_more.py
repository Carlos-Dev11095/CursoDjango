# Generated by Django 4.0.5 on 2022-06-29 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='imagen',
            field=models.ImageField(null=True, upload_to='fotos', verbose_name='Fotografía'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='activo',
            field=models.BooleanField(verbose_name='Disponibilidad del curso'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='descripcion',
            field=models.TextField(verbose_name='Características del curso'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='duracion',
            field=models.PositiveSmallIntegerField(verbose_name='Tiempo del curso en meses'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='idcurso',
            field=models.SmallIntegerField(primary_key=True, serialize=False, verbose_name='Id del curso'),
        ),
        migrations.AlterField(
            model_name='cursos',
            name='nombre',
            field=models.TextField(max_length=30, verbose_name='Nombre del curso'),
        ),
    ]