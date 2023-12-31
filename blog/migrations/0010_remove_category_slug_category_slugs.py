# Generated by Django 4.2.4 on 2023-09-04 13:14

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_category_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.AddField(
            model_name='category',
            name='slugs',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, null=True, populate_from='name', unique=True),
        ),
    ]
