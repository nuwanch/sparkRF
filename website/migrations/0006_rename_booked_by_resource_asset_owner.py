# Generated by Django 4.2.7 on 2024-01-03 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_record'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='booked_by',
            new_name='asset_owner',
        ),
    ]
