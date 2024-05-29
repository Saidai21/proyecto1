# Generated by Django 4.1.2 on 2024-05-29 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id_admin', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('contrasena_encriptada', models.CharField(max_length=100)),
                ('permiso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_catg', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('contrasena', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id_factura', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('total', models.IntegerField()),
                ('cliente', models.ForeignKey(db_column='id_cliente', on_delete=django.db.models.deletion.CASCADE, to='alumnos.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='FacturaProducto',
            fields=[
                ('id_fact_prod', models.AutoField(primary_key=True, serialize=False)),
                ('factura', models.ForeignKey(db_column='id_factura', on_delete=django.db.models.deletion.CASCADE, to='alumnos.factura')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_prod', models.CharField(max_length=100)),
                ('descripcion_prod', models.CharField(max_length=100)),
                ('catg_prod', models.IntegerField()),
                ('categoria', models.ForeignKey(db_column='id_categoria', on_delete=django.db.models.deletion.CASCADE, to='alumnos.categoria')),
            ],
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
        migrations.AddField(
            model_name='facturaproducto',
            name='producto',
            field=models.ForeignKey(db_column='id_producto', on_delete=django.db.models.deletion.CASCADE, to='alumnos.producto'),
        ),
    ]
