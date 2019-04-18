# Generated by Django 2.1.7 on 2019-04-15 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_auto_20190415_1804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)", max_length=200)),
            ],
        ),
    ]