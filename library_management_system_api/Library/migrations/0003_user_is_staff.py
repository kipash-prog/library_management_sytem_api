# Generated by Django 5.1.3 on 2024-12-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0002_alter_book_number_of_copies_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]