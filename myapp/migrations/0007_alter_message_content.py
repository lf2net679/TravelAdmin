# Generated by Django 5.1.1 on 2024-10-11 16:05

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_message_quoted_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
