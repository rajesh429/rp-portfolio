# Generated by Django 3.2.9 on 2021-12-01 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_rename_technology_project_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
    ]