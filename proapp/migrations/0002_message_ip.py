# Generated by Django 2.1 on 2018-08-28 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='ip',
            field=models.TextField(default='127.0.0.1'),
            preserve_default=False,
        ),
    ]
