# Generated by Django 2.1.7 on 2019-04-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20190415_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='language_name',
            field=models.CharField(choices=[('English', 'English'), ('Georgina', 'Georgian'), ('Russian', 'Russian')], help_text='Book language availability', max_length=13, primary_key=True, serialize=False),
        ),
    ]
