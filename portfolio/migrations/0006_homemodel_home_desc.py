# Generated by Django 3.2.6 on 2021-08-16 06:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_homemodel_home_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='homemodel',
            name='home_desc',
            field=ckeditor.fields.RichTextField(default='Enter Description here'),
        ),
    ]