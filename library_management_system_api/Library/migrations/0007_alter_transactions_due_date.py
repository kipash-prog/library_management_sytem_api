# Generated by Django 5.1.3 on 2024-12-19 18:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0006_transactions_due_date_transactions_penalty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='due_date',
            field=models.DateField(default=datetime.datetime(2025, 1, 2, 18, 49, 34, 503692, tzinfo=datetime.timezone.utc)),
        ),
    ]
