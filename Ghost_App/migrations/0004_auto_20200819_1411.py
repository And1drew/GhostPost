# Generated by Django 3.1 on 2020-08-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ghost_App', '0003_auto_20200819_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boastorroast',
            name='is_boast',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
