# Generated by Django 5.1.2 on 2024-11-06 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='book_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
