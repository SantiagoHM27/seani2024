# Generated by Django 5.0.2 on 2024-02-22 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stage',
            options={'verbose_name': 'etapa', 'verbose_name_plural': 'etapas'},
        ),
        migrations.AlterField(
            model_name='stage',
            name='application_date',
            field=models.DateField(verbose_name='Fecha de Aplicacion'),
        ),
    ]