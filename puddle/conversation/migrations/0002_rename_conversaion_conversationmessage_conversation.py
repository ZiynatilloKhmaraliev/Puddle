# Generated by Django 5.0.1 on 2024-01-30 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='conversaion',
            new_name='conversation',
        ),
    ]
