# Generated by Django 4.1.2 on 2023-06-28 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0051_profile_test_failed_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='retake_test',
            field=models.DateField(blank=True, null=True),
        ),
    ]
