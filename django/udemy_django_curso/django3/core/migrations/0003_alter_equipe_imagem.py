# Generated by Django 5.0.1 on 2024-01-30 11:14

import core.models
import stdimage.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_servico_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipe',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem'),
        ),
    ]