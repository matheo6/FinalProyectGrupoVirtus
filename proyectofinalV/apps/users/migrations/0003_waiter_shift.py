# Generated by Django 5.0.3 on 2024-06-06 02:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_bill_final_cost_bill_tip_percent'),
        ('users', '0002_alter_user_first_name_alter_waiter_charge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Waiter_Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.restaurant')),
                ('waiter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.waiter')),
            ],
        ),
    ]
