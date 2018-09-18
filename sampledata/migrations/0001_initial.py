# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('user_id', models.IntegerField(verbose_name='User_id', primary_key=True, serialize=False)),
                ('email_id', models.EmailField(verbose_name='Email id', max_length=100)),
                ('password', models.IntegerField(verbose_name='Password')),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.CreateModel(
            name='Onlineregister',
            fields=[
                ('ID', models.IntegerField(verbose_name='ID', primary_key=True, serialize=False)),
                ('firstName', models.CharField(verbose_name='First Name', max_length=100)),
                ('lastName', models.CharField(verbose_name='Last Name', max_length=100)),
                ('email', models.EmailField(verbose_name='Email id', max_length=100)),
                ('zipcode', models.IntegerField(verbose_name='Zipcode')),
                ('sex', models.CharField(verbose_name='Sex', max_length=10)),
                ('birth', models.DateTimeField(verbose_name='Date of Birth')),
                ('password', models.IntegerField(verbose_name='Password')),
            ],
            options={
                'db_table': 'onlineregister',
            },
        ),
    ]
