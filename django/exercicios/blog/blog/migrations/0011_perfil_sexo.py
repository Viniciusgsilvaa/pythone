# Generated by Django 5.1.2 on 2024-11-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_perfil_reputacao_alter_perfil_usuario_pergunta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='sexo',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=100, null=True),
        ),
    ]