# Generated by Django 3.2.6 on 2021-08-16 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_homemodel_home_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homemodel',
            name='home_image',
            field=models.ImageField(default='default.png', upload_to='home_images/'),
        ),
    ]
