# Generated by Django 3.1.3 on 2020-12-07 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edYou', '0005_auto_20201207_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='difficulty',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=12),
        ),
    ]