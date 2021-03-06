# Generated by Django 4.0 on 2022-01-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0008_alter_lens_lens_model_alter_camera_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lens',
            name='lens_model',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='image',
            unique_together={('filename', 'path')},
        ),
    ]
