# Generated by Django 4.0 on 2021-12-31 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('importer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='importer',
            old_name='path',
            new_name='import_path',
        ),
    ]
