# Generated by Django 5.1 on 2024-09-28 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=15)),
                ('cargo', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
