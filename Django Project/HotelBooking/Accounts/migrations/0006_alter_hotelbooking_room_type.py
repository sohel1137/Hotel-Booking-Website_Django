# Generated by Django 4.2.6 on 2023-10-29 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_delete_customer_hotelbooking_room_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelbooking',
            name='room_type',
            field=models.TextField(choices=[('SINGLE', 'Single'), ('DOUBLE', 'Double')]),
        ),
    ]
