# Generated by Django 4.2.6 on 2023-11-16 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_hotelbooking_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='Ammount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=5),
            preserve_default=False,
        ),
    ]
