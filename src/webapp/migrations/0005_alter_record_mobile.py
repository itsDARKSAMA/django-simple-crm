# Generated by Django 5.0.7 on 2024-09-13 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_record_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='mobile',
            field=models.CharField(max_length=13),
        ),
    ]