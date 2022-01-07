# Generated by Django 4.0 on 2022-01-07 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0002_alter_directory_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directory',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='directories.directory'),
        ),
        migrations.AlterField(
            model_name='directory',
            name='path',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='directory',
            name='text',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]