# Generated by Django 4.2.5 on 2023-10-02 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_kardex_estado_alter_categoria_cod_grupo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='cod_categoria',
            new_name='categoria',
        ),
        migrations.AlterField(
            model_name='inventario',
            name='frecuencia',
            field=models.DecimalField(decimal_places=3, default=1.0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='kardex',
            name='guia',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='kardex',
            name='movimiento',
            field=models.PositiveIntegerField(choices=[(1, 'Entrada'), (2, 'Salida')]),
        ),
        migrations.AlterField(
            model_name='kardex',
            name='observacion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kardex',
            name='orden_compra',
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
    ]
