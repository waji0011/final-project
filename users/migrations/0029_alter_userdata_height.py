# Generated by Django 4.1.2 on 2023-05-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_alter_userdata_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
