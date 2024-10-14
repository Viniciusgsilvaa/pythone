# Generated by Django 5.1.2 on 2024-10-14 10:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('bio', models.TextField()),
                ('localizacao', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seguidor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('seguidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seguidores', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seguindo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('usuario', 'seguidor')},
            },
        ),
    ]
