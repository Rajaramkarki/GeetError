# Generated by Django 3.2.3 on 2021-06-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210608_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='song_genre',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
