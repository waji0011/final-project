# Generated by Django 4.1.2 on 2023-05-04 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0023_profile_has_submitted_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='pdf_file',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]