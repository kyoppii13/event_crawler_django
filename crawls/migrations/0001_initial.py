# Generated by Django 2.0.3 on 2018-04-04 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crawl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('url', models.URLField()),
                ('address', models.TextField()),
                ('img_url', models.URLField()),
                ('date', models.CharField(max_length=10)),
            ],
        ),
    ]
