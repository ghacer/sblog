# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150720_1420'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-is_top', '-id']},
        ),
        migrations.AddField(
            model_name='post',
            name='is_top',
            field=models.BooleanField(default=False, verbose_name='\u7f6e\u9876'),
        ),
    ]
