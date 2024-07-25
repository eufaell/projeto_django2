# Generated by Django 5.0.7 on 2024-07-25 00:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blo_title', models.CharField(max_length=100, verbose_name='Título')),
                ('blo_subtitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='Sub-Título')),
                ('blo_description', models.TextField(verbose_name='Texto do Blog')),
                ('blo_image', models.ImageField(blank=True, null=True, upload_to='images/blog', verbose_name='Imagem de Capa')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Blogs',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=255, unique=True, verbose_name='Nome da Categoria')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('stock', models.IntegerField(blank=True, null=True, verbose_name='Quantidade em Estoque')),
                ('descricao', models.CharField(blank=True, max_length=100, null=True, verbose_name='Descrição')),
                ('pro_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.category')),
            ],
            options={
                'verbose_name': 'Produto',
                'verbose_name_plural': 'Produtos',
            },
        ),
    ]
