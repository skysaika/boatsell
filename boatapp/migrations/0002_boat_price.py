# Generated by Django 4.2.3 on 2023-07-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boatapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boat',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='цена'),
        ),
    ]