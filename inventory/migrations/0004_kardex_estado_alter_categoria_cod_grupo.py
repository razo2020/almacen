# Generated by Django 4.2.5 on 2023-09-27 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_remove_categoria_ch_tipo_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kardex',
            name='estado',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='cod_grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.categoria', verbose_name='categoria'),
        ),
    ]
