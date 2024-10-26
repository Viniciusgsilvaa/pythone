# Generated by Django 5.1.2 on 2024-10-25 17:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_dislikes_post_likes_votopost'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='reputacao',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('texto', models.TextField()),
                ('votos_positivos', models.IntegerField(default=0)),
                ('votos_negativos', models.IntegerField(default=0)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='blog.pergunta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pergunta',
            name='melhor_resposta',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='melhor_resposta_da_pergunta', to='blog.resposta'),
        ),
        migrations.CreateModel(
            name='VotoResposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('tipo_voto', models.CharField(choices=[('positivo', 'Positivo'), ('negativo', 'Negativo')], max_length=8)),
                ('respostas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votos', to='blog.resposta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]