# Generated by Django 3.2.8 on 2021-10-17 20:59

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
                ('surname', models.CharField(max_length=20, verbose_name='Отчество')),
                ('patronymic', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Номер телефона')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название склада')),
                ('adress', models.CharField(max_length=300, verbose_name='Адресс склада')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Autoparts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invent_number', models.CharField(max_length=127, verbose_name='Инвентарный номер')),
                ('number', models.IntegerField(verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=0, max_digits=5, verbose_name='Цена')),
                ('car_for_using', models.CharField(max_length=255, verbose_name='Техника для использования')),
                ('date_of_supply', models.DateField(verbose_name='Дата поступления')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('return_detail', models.BooleanField(verbose_name='Возвращено')),
                ('accepr_from_top', models.BooleanField(verbose_name='Подтверждение свыше')),
                ('contactor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='monitoring.contactor', verbose_name='Ответственный')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='monitoring.status', verbose_name='Статус')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='monitoring.warehouse', verbose_name='Склад')),
            ],
        ),
    ]
