# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_auto_20141026_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('slug', models.SlugField(editable=False)),
                ('summary', models.TextField(max_length=255)),
                ('content', models.TextField()),
                ('place', models.CharField(max_length=50)),
                ('start', models.DateTimeField()),
                ('finish', models.DateTimeField()),
                ('imagen', models.ImageField(upload_to=b'events')),
                ('is_free', models.BooleanField(default=True)),
                ('amount', models.DecimalField(default=0.0, max_digits=5, decimal_places=2)),
                ('views', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(to='events.Category')),
                ('organizer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='events',
            name='category',
        ),
        migrations.RemoveField(
            model_name='events',
            name='organizer',
        ),
        migrations.AlterField(
            model_name='assistant',
            name='event',
            field=models.ManyToManyField(to=b'events.Event'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='event',
            field=models.ForeignKey(to='events.Event'),
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]
