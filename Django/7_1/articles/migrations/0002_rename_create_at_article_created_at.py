# Generated by Django 4.2.11 on 2024-03-31 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='create_at',
            new_name='created_at',
        ),
    ]
