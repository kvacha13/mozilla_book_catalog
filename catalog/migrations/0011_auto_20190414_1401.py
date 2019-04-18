# Generated by Django 2.1.7 on 2019-04-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20190414_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='language_name',
            field=models.CharField(blank=True, choices=[('Eng', 'English'), ('Geo', 'Georgian'), ('Rus', 'Russian')], default='Eng', help_text='Book language availability', max_length=1),
        ),
    ]