# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-18 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('wiki_id', models.IntegerField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=255)),
                ('attribution', models.TextField(null=True)),
                ('background', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('design', models.TextField(null=True)),
                ('human_practice', models.TextField(null=True)),
                ('modeling', models.TextField(null=True)),
                ('notebook', models.TextField(null=True)),
                ('protocol', models.TextField(null=True)),
                ('result', models.TextField(null=True)),
                ('safety', models.TextField(null=True)),
                ('keywords', models.TextField(null=True)),
                ('track', models.TextField(null=True)),
                ('part_favorite', models.TextField(null=True)),
                ('part_normal', models.TextField(null=True)),
            ],
            options={
                'db_table': 'team_wiki',
                'managed': False,
            },
        ),
    ]
