# Generated by Django 4.1.2 on 2023-05-04 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_contact_fullname_userdata_fullname'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='has_submitted_video',
            field=models.BooleanField(default=False),
        ),
    ]
