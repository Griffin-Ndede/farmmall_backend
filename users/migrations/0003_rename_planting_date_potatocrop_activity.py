# Generated by Django 5.1.1 on 2024-09-25 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_region_potatocrop_county'),
    ]

    operations = [
        migrations.RenameField(
            model_name='potatocrop',
            old_name='planting_date',
            new_name='activity',
        ),
    ]