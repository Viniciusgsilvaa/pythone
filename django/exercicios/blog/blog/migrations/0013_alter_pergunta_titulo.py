# Generated by Django 5.1.2 on 2024-11-05 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_pergunta_melhor_resposta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='titulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titulo', to='blog.perfil'),
        ),
    ]
