# Generated by Django 4.2.1 on 2023-05-30 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
