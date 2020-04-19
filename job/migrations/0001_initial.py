# Generated by Django 2.2 on 2020-04-18 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(blank=True, max_length=250, null=True)),
                ('slug', models.CharField(default='', max_length=250)),
                ('epoch', models.CharField(default='', max_length=250)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('company', models.CharField(default='', max_length=250)),
                ('position', models.CharField(default='', max_length=250)),
                ('description', models.CharField(default='', max_length=250)),
                ('url', models.CharField(default='', max_length=250)),
                ('visible', models.BooleanField(default=False)),
            ],
        ),
    ]
