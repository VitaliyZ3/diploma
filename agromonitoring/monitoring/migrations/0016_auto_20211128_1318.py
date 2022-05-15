# Generated by Django 3.2.8 on 2021-11-28 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0015_alter_autopart_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autopart',
            name='accepr_from_top',
        ),
        migrations.RemoveField(
            model_name='autopart',
            name='return_detail',
        ),
        migrations.AlterField(
            model_name='status',
            name='status_code',
            field=models.IntegerField(default=0, unique=True, verbose_name='Код Статуса'),
        ),
    ]
