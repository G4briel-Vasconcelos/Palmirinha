# Generated by Django 5.0.3 on 2024-04-02 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReceitaApp', '0002_receita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='dificuldade',
            field=models.CharField(blank=True, choices=[('Facil', 'Facil'), ('Moderado', 'Moderado'), ('Dificil', 'Dificil')], max_length=10, null=True),
        ),
    ]