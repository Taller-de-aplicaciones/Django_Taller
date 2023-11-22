# Generated by Django 4.2.4 on 2023-11-22 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20, verbose_name='AnalistaUser')),
                ('rut', models.CharField(max_length=10, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('paterno', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('materno', models.CharField(max_length=50, verbose_name='Apellido Materno')),
                ('fechaNac', models.DateField(verbose_name='Fecha Nacimiento')),
                ('sexo', models.CharField(choices=[('m', 'Masculino'), ('f', 'Femenino'), ('o', 'Otro')], default='o', max_length=1)),
            ],
            options={
                'verbose_name': 'Analista',
                'verbose_name_plural': 'Analistas',
                'db_table': 'analista',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('empresaID', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=15)),
                ('nombreEmpresa', models.CharField(max_length=255)),
                ('representanteLegal', models.CharField(max_length=255)),
                ('rutRepresentante', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Entrevistado',
            fields=[
                ('entrevistadoID', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=255)),
                ('apellidos', models.CharField(max_length=255)),
                ('rut', models.CharField(max_length=15)),
                ('fechaNacimiento', models.DateField()),
                ('ciudad', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Entrevistador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20, verbose_name='EntrevistadorUser')),
                ('rut', models.CharField(max_length=10, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('paterno', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('materno', models.CharField(max_length=50, verbose_name='Apellido Materno')),
                ('fechaNac', models.DateField(verbose_name='Fecha Nacimiento')),
                ('sexo', models.CharField(choices=[('m', 'Masculino'), ('f', 'Femenino'), ('o', 'Otro')], default='o', max_length=1)),
            ],
            options={
                'verbose_name': 'Entrevistador',
                'verbose_name_plural': 'Entrevistadores',
                'db_table': 'entrevistador',
            },
        ),
        migrations.CreateModel(
            name='Produccion',
            fields=[
                ('produccionID', models.AutoField(primary_key=True, serialize=False)),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appWeb.empresa')),
                ('entrevistado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appWeb.entrevistado')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('productoID', models.AutoField(primary_key=True, serialize=False)),
                ('nombreProducto', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('userType', models.CharField(choices=[('e', 'Entrevistador'), ('a', 'Analista')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProduccionDetalle',
            fields=[
                ('produccionDetalleID', models.AutoField(primary_key=True, serialize=False)),
                ('cantidadKg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('produccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appWeb.produccion')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appWeb.producto')),
            ],
        ),
        migrations.AddField(
            model_name='entrevistado',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appWeb.usuario'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='entrevistado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appWeb.entrevistado'),
        ),
    ]
