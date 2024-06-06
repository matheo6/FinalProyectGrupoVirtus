# Generated by Django 5.0.3 on 2024-06-04 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('cost_per_unit', models.IntegerField()),
                ('all_restaurants', models.BooleanField(default=False)),
            ],
        ),
    ]
