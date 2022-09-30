# Generated by Django 3.1.7 on 2021-05-08 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20210505_0528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thumb',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='house_pics'),
        ),
    ]
