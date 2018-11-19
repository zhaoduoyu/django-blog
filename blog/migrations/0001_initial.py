# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-11-17 12:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('date_time', models.DateField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('digest', models.TextField(blank=True, null=True)),
                ('view', models.BigIntegerField(default=0)),
                ('comment', models.BigIntegerField(default=0)),
                ('picture', models.CharField(max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u4f5c\u8005')),
            ],
            options={
                'ordering': ['-date_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u6587\u7ae0\u7c7b\u578b')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('last_mod_time', models.DateTimeField(auto_now=True, verbose_name='\u4fee\u6539\u65f6\u95f4')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': '\u6587\u7ae0\u7c7b\u578b',
                'verbose_name_plural': '\u6587\u7ae0\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('source_id', models.CharField(max_length=25, verbose_name='\u6587\u7ae0id\u6216source\u540d\u79f0')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='\u8bc4\u8bba\u65f6\u95f4')),
                ('user_name', models.CharField(max_length=25, verbose_name='\u8bc4\u8bba\u7528\u6237')),
                ('url', models.CharField(max_length=100, verbose_name='\u94fe\u63a5')),
                ('comment', models.CharField(max_length=500, verbose_name='\u8bc4\u8bba\u5185\u5bb9')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=30, verbose_name='\u6807\u7b7e\u540d')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='\u6587\u7ae0\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
