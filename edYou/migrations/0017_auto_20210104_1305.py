# Generated by Django 3.1.3 on 2021-01-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edYou', '0016_auto_20210104_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='img',
            field=models.ImageField(upload_to='photos/%Y/%m/%d'),
        ),
    ]
