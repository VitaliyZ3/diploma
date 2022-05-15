from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Класс заправки
class FuelStation(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название заправки')
    adress = models.CharField(max_length=300, verbose_name='Адресс заправки')
    capacity_gas_station = models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Общий обьём заправки')
    total_fuel = models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Топлива на заправке в данный момент')
    description = models.TextField(blank=True, verbose_name='Описание')
    
    class Meta:
        verbose_name = 'АЗС'
        verbose_name_plural = 'АЗС'

    def __str__(self) -> str:
        return f'Заправка "{self.name}"'


# Класс машин, которые будут заправлятся 
class Cars(models.Model):
    number = models.CharField(max_length=15, verbose_name='Номер машини')
    tank_volume = models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Литраж бака')
    type_of_car = models.CharField(max_length=127, verbose_name='Тип машины')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'

    def __str__(self) -> str:
        return f'Машина "{self.number}"'

# Класс водителей, которые будут заправлятся
class Drivers(models.Model):
    name = models.CharField(max_length= 127, verbose_name='Имя')
    surname = models.CharField(max_length= 127, verbose_name='Отчество')
    patronymic = models.CharField(max_length= 127, verbose_name='Фамилия')
    phone_number = PhoneNumberField(null=False, blank=False, unique=True,verbose_name='Номер телефона')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

    def __str__(self) -> str:
        return f'Водитель "{self.patronymic}"'


class FuelStationRefill(models.Model):
    """
    Пополнение АЗС топливом
    ...
    """
    fuel_station = models.ForeignKey(FuelStation , on_delete=models.DO_NOTHING, verbose_name='АЗС')
    refill_volume = models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Было заправлено')
    date_of_refill = models.DateTimeField(auto_now= datetime.now(), verbose_name='Дата и время заправки' )
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Пополнение АЗС топливом'
        verbose_name_plural = 'Пополнение АЗС топливом'
        ordering = ['date_of_refill'] 

    def __str__(self) -> str:
        return f'Пополнение АЗС топливом "{self.Date_of_fuel}"'


class CarRefill(models.Model):
    """
    Заправка транспорта
    ...
    """
    fuel_station = models.ForeignKey(FuelStation , on_delete=models.DO_NOTHING, verbose_name='АЗС')
    cars =  models.ForeignKey(Cars , on_delete=models.DO_NOTHING, verbose_name='Машина')
    driver = models.ForeignKey(Drivers , on_delete=models.DO_NOTHING, verbose_name='Водитель')
    fillin_volume  = models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Было заправлено')
    date_of_fuel = models.DateTimeField(auto_now= datetime.now(), verbose_name='Дата и время заправки' )
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Заправка'
        verbose_name_plural = 'Запрвка'
        ordering = ['date_of_fuel'] 

    def __str__(self) -> str:
        return f'Заправка "{self.date_of_fuel}"'


class Warehouse(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название склада')
    adress = models.CharField(max_length=300, verbose_name='Адресс склада')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

    def __str__(self) -> str:
        return f'Склад "{self.name}"'


class Contactor(models.Model):
    name = models.CharField(max_length= 127, verbose_name='Имя')
    surname = models.CharField(max_length= 127, verbose_name='Отчество')
    patronymic = models.CharField(max_length= 127, verbose_name='Фамилия')
    phone_number = PhoneNumberField(null=False, blank=False, unique=True,verbose_name='Номер телефона')
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self) -> str:
        return f'Исполнитель "{self.surname} {self.name}"'


class Status(models.Model):
    """
    Статусы запчасти
    
    Обозначения status_code
        0 - На складе
        1 - Использовано
        2 - Списано
        3 - Возвращено
    ...
    """
    status_code = models.IntegerField(default=0, unique=True, verbose_name='Код Статуса')
    status = models.CharField(max_length=127, default='На складе')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self) -> str:
        return f'Статус "{self.status}"'


class Autopart(models.Model):
    name = models.CharField(max_length= 127, verbose_name='Название')
    invent_number = models.CharField(max_length=127, verbose_name='Инвентарный номер')
    warehouse = models.ForeignKey(Warehouse, on_delete=models.DO_NOTHING, verbose_name='Склад')
    number = models.IntegerField(verbose_name='Количество')
    price = models.DecimalField(max_digits=5, decimal_places=0, verbose_name='Цена')
    car_for_using = models.CharField(max_length=255, verbose_name='Техника для использования')
    date_of_supply = models.DateField(auto_now= datetime.now(), verbose_name='Дата поступления')
    contactor = models.ForeignKey(Contactor, on_delete=models.DO_NOTHING, verbose_name='Ответственный')
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING, verbose_name='Статус', default=Status.objects.filter(status_code=0).first().pk)
    description = models.TextField(blank=True, verbose_name='Описание')


    class Meta:
        verbose_name = 'Запчасть'
        verbose_name_plural = 'Запчасти'

    def __str__(self) -> str:
        return f'Запчасть "{self.name}"'


