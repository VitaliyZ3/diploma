# Generated by Django 3.2.8 on 2021-10-17 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0014_alter_status_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autopart',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='monitoring.status', verbose_name='Статус'),
        ),
    ]
