# Generated by Django 4.0 on 2022-01-07 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0004_alter_directory_parent'),
        ('images', '0009_alter_lens_lens_model_alter_image_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directories.directory'),
        ),
    ]
