# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 09:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, validators=[django.core.validators.MaxLengthValidator(32)], verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()], verbose_name='e-mail')),
                ('subject', models.CharField(blank=True, max_length=32, verbose_name='Тема')),
                ('message', models.CharField(max_length=255, validators=[django.core.validators.MaxLengthValidator(255)], verbose_name='Сообщение')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('is_reply', models.BooleanField(default=False, verbose_name='Отвечено')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='HeadPicture',
            fields=[
                ('title', models.CharField(max_length=255, null=True)),
                ('interval', models.IntegerField(default=5000)),
                ('priority', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(upload_to='head/')),
            ],
        ),
        migrations.CreateModel(
            name='OurTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='team/')),
            ],
        ),
    ]
