# Generated by Django 3.0.6 on 2020-05-15 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graceBackend', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': 'Entry', 'verbose_name_plural': 'Entries'},
        ),
        migrations.RemoveField(
            model_name='entry',
            name='owner',
        ),
        migrations.AddField(
            model_name='entry',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
