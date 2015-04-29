# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='controlasistencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dias', models.CharField(max_length=30)),
                ('horas', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='proyectos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cod', models.CharField(max_length=30)),
                ('detalles_proyecto', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TareasEncargadas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nro_encargados', models.CharField(max_length=2)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('cod', models.ForeignKey(to='tablas.proyectos')),
            ],
        ),
        migrations.CreateModel(
            name='trabajadores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='tareasencargadas',
            name='nombres',
            field=models.ForeignKey(to='tablas.trabajadores'),
        ),
        migrations.AddField(
            model_name='controlasistencia',
            name='nombres',
            field=models.ForeignKey(to='tablas.trabajadores'),
        ),
    ]
