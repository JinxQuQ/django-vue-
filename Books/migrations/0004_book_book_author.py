# Generated by Django 4.2.1 on 2023-05-31 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0003_alter_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_author',
            field=models.CharField(default='unknown', max_length=50),
        ),
    ]