# Generated by Django 3.2 on 2021-04-30 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('Matricula', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Marca', models.CharField(max_length=255)),
                ('Modelo', models.CharField(max_length=255)),
                ('Rate', models.DecimalField(decimal_places=1, max_digits=1)),
                ('Descripcion', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('Usuario', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=25)),
                ('Nombre', models.CharField(max_length=25)),
                ('Apellidos', models.CharField(max_length=25)),
                ('Nacionalidad', models.CharField(max_length=25)),
                ('Celular', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=25)),
                ('Rate', models.DecimalField(decimal_places=1, max_digits=1)),
                ('Direccion', models.CharField(max_length=25)),
                ('Categoria', models.CharField(max_length=25)),
                ('Web', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=25)),
                ('Direccion', models.CharField(max_length=25)),
                ('Categoria', models.CharField(max_length=25)),
                ('Rate', models.DecimalField(decimal_places=1, max_digits=1)),
                ('Descripcion', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SitioTuristico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=25)),
                ('Direccion', models.CharField(max_length=25)),
                ('Rate', models.DecimalField(decimal_places=1, max_digits=1)),
                ('Categoria', models.CharField(max_length=25)),
                ('Descripcion', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('Barrio', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('Centro', models.CharField(max_length=255)),
                ('Crespo', models.CharField(max_length=255)),
                ('Marbella', models.CharField(max_length=255)),
                ('Cabrero', models.CharField(max_length=255)),
                ('Bocagrande', models.CharField(max_length=255)),
                ('CastilloGrande', models.CharField(max_length=255)),
                ('ElLaguito', models.CharField(max_length=255)),
                ('LaBoquilla', models.CharField(max_length=255)),
                ('Manzanillo', models.CharField(max_length=255)),
                ('SanFelipe', models.CharField(max_length=255)),
                ('LaPopa', models.CharField(max_length=255)),
                ('Manga', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=25)),
                ('Categoria', models.CharField(max_length=25)),
                ('Rate', models.DecimalField(decimal_places=1, max_digits=1)),
                ('Descripcion', models.TextField(max_length=500)),
                ('Duracion', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('Usuario', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=25)),
                ('Nombre', models.CharField(max_length=25)),
                ('Apellidos', models.CharField(max_length=25)),
                ('Celular', models.IntegerField()),
                ('Rate', models.DecimalField(decimal_places=1, max_digits=1)),
                ('Rol', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Reseña',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rate', models.DecimalField(decimal_places=1, max_digits=1)),
                ('Descripcion', models.TextField(max_length=500)),
                ('Auto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HeroicaTour_DB.auto')),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HeroicaTour_DB.cliente')),
                ('Hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HeroicaTour_DB.hotel')),
                ('Restaurante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HeroicaTour_DB.restaurante')),
                ('SitioTuristico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HeroicaTour_DB.sitioturistico')),
                ('Tour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HeroicaTour_DB.tour')),
                ('Trabajador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HeroicaTour_DB.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Preferencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Presupuesto', models.IntegerField()),
                ('Acompañantes', models.IntegerField()),
                ('Alojamiento', models.BooleanField(default=False)),
                ('Auto', models.BooleanField(default=False)),
                ('Duracion', models.IntegerField()),
                ('Cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HeroicaTour_DB.cliente')),
            ],
        ),
    ]