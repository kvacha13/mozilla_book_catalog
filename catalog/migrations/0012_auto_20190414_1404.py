# Generated by Django 2.1.7 on 2019-04-14 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20190414_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='language_name',
            field=models.CharField(blank=True, choices=[('Eng', 'English'), ('Geo', 'Georgian'), ('Rus', 'Russian')], default='Eng', help_text='Book language availability', max_length=20),
        ),
    ]
