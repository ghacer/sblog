# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40, verbose_name='\u6587\u7ae0\u5206\u7c7b')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name='\u6807\u9898')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('is_top', models.BooleanField(default=False, verbose_name='\u7f6e\u9876')),
                ('author', models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(verbose_name='\u7c7b\u522b', to='blog.Category')),
            ],
            options={
                'ordering': ['-is_top', '-id'],
            },
        ),
    ]
