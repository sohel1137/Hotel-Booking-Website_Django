# Generated by Django 4.2.6 on 2023-10-14 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_hotel_cat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categeroies',
            old_name='Name',
            new_name='title',
        ),
    ]
