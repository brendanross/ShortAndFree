# Generated by Django 2.2.2 on 2019-06-13 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=5)),
                ('tk', models.BooleanField(default=False)),
                ('ml', models.BooleanField(default=False)),
                ('ga', models.BooleanField(default=False)),
                ('cf', models.BooleanField(default=False)),
                ('gq', models.BooleanField(default=False)),
                ('length', models.IntegerField()),
                ('checked_date', models.DateTimeField()),
                ('created_date', models.DateTimeField()),
            ],
        ),
    ]
