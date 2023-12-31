# Generated by Django 4.2.4 on 2023-09-04 13:10

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_news_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='name', unique=True),
        ),
    ]
