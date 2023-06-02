# Generated by Django 4.2.1 on 2023-06-02 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('preco', models.FloatField(verbose_name='Preço')),
                ('ingredientes', models.CharField(max_length=150, verbose_name='Ingredientes')),
                ('quantidade', models.IntegerField(default=1, verbose_name='Quantidade')),
            ],
        ),
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now_add=True)),
                ('produtos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurante.produto')),
            ],
        ),
    ]
