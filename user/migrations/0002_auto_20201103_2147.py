# Generated by Django 3.1.3 on 2020-11-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]