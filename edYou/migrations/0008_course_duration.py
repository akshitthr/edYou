# Generated by Django 3.1.3 on 2020-12-07 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edYou', '0007_auto_20201207_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.CharField(default='none', max_length=12),
            preserve_default=False,
        ),
    ]