# Generated by Django 5.0.3 on 2024-06-05 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bills',
            new_name='Bill',
        ),
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='Tables',
            new_name='Table',
        ),
    ]
