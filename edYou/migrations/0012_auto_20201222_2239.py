# Generated by Django 3.1.3 on 2020-12-22 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edYou', '0011_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='text',
            new_name='content',
        ),
    ]
