# Generated by Django 3.2.8 on 2021-10-17 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0010_alter_autopart_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status_code',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=5, unique=True),
        ),
    ]
