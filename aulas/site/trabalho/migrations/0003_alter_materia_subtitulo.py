# Generated by Django 4.1.3 on 2022-11-25 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabalho', '0002_rename_sobrenome_materia_subtitulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='subtitulo',
            field=models.TextField(blank=True),
        ),
    ]
