# Generated by Django 5.0.4 on 2024-05-02 23:36

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('kind_of_establishment', models.CharField(choices=[('bar', 'Bar'), ('restaurante', 'Restaurante'), ('clube', 'Clube'), ('saloes', 'Salões de eventos')], default='bar', max_length=200)),
                ('slug', models.SlugField(max_length=200, unique_for_date='publicado')),
                ('address', models.CharField(max_length=250)),
                ('number', models.CharField(max_length=20)),
                ('neighborhood', models.CharField(max_length=200)),
                ('city_area', models.CharField(choices=[('leste', 'Leste'), ('oeste', 'Oeste'), ('norte', 'Norte'), ('sul', 'Sul'), ('centro', 'Centro')], default='centro', max_length=50)),
                ('zip_code', models.DecimalField(decimal_places=0, max_digits=8)),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('rascunho', 'Rascunho'), ('publicado', 'Publicado')], default='rascunho', max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
