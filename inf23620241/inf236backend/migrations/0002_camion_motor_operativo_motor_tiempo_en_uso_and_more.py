# Generated by Django 4.2.11 on 2024-04-25 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inf236backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='motor',
            name='operativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='motor',
            name='tiempo_en_uso',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='AsignacionMotorCamion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asignacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_desasignacion', models.DateTimeField(blank=True, null=True)),
                ('camion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inf236backend.camion')),
                ('motor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inf236backend.motor')),
            ],
        ),
    ]
