# Generated by Django 4.2.7 on 2024-03-08 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_workrequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workrequest',
            name='assigned_engineer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='requesting_engineer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='work_description',
            field=models.TextField(max_length=255),
        ),
    ]
