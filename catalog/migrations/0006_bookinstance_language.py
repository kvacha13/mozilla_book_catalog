# Generated by Django 2.1.7 on 2019-04-14 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20190414_1315'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinstance',
            name='language',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
    ]
