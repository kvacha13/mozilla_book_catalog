# Generated by Django 2.1.7 on 2019-04-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20190415_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(help_text='Select an available language for this book', max_length=13, verbose_name='Language'),
        ),
    ]
