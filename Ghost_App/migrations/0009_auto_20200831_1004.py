# Generated by Django 3.1 on 2020-08-31 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ghost_App', '0008_boastorroast_vote_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boastorroast',
            name='description',
            field=models.CharField(max_length=240),
        ),
    ]