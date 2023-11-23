# Generated by Django 4.2.6 on 2023-10-29 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_rename_name_categeroies_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='room_type',
            field=models.CharField(choices=[('S', 'Single'), ('D', 'Double')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
