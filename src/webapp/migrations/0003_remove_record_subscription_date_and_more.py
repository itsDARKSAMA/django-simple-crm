# Generated by Django 5.0.7 on 2024-09-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_record_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='subscription_date',
        ),
        migrations.AlterField(
            model_name='record',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
