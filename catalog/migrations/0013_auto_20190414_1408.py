# Generated by Django 2.1.7 on 2019-04-14 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20190414_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='language_name',
            field=models.CharField(choices=[('English', 'English'), ('Georgina', 'Georgian'), ('Russian', 'Russian')], help_text='Book language availability', max_length=20),
        ),
    ]
