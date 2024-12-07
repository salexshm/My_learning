from django.db import models
from django.contrib.auth.models import User


class Tariff(models.Model):
    class Meta:
        verbose_name = "Тарифный план"
        verbose_name_plural = "Тарифный план"

    name = models.CharField(max_length=12, blank=False)
    price = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return f"{self.name}"


class Device(models.Model):
    class Meta:
        verbose_name = "Устройство"
        verbose_name_plural = "Устройство"

    ip_address = models.CharField(max_length=15, blank=False)
    name = models.CharField(max_length=12, blank=False)
    mac = models.CharField(max_length=17, blank=False)

    def __str__(self):
        return f"{self.ip_address}"


class District(models.Model):
    class Meta:
        verbose_name = "Район"
        verbose_name_plural = "Район"

    name = models.CharField(max_length=12, verbose_name='Район', blank=True)

    def __str__(self):
        return self.name


class Street(models.Model):
    class Meta:
        verbose_name = "Улица"
        verbose_name_plural = "Улица"

    district = models.ForeignKey(District, verbose_name='Район', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Улица', max_length=100)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профиль"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, verbose_name='Телефон', blank=True)
    address = models.ForeignKey(Street, verbose_name='Улица', on_delete=models.CASCADE, blank=True, null=True)
    home_number = models.CharField(max_length=4, verbose_name='Номер дома', blank=True)
    flat_number = models.CharField(max_length=4, verbose_name='Квартира', blank=True)
    tariff = models.ForeignKey(Tariff, verbose_name='Тарифный план', on_delete=models.CASCADE, blank=True, null=True)
    device = models.OneToOneField(Device, verbose_name='Устройство', on_delete=models.CASCADE, blank=True, null=True)
