# Generated by Django 3.1.7 on 2021-03-05 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=500)),
                ('short_url', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]