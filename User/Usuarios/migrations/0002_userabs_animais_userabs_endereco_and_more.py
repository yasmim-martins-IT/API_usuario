# Generated by Django 5.1.7 on 2025-03-28 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userabs',
            name='animais',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userabs',
            name='endereco',
            field=models.CharField(default='Endereço não informado', max_length=255),
        ),
        migrations.AlterField(
            model_name='userabs',
            name='telefone',
            field=models.IntegerField(default=0),
        ),
    ]
