# Generated by Django 4.0 on 2021-12-12 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='province',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]