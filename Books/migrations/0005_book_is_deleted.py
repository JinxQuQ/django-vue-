# Generated by Django 4.2.1 on 2023-05-31 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0004_book_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
