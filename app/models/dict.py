from django.db import models
from .abstract import TimestampModel
from django.utils.translation import gettext_lazy as _


class Country(TimestampModel):
    """Страна"""
    id: int
    name: str = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Страна'
    )

    class Meta:
        verbose_name_plural = _("Страны")
        verbose_name = _("Страна")

    def __str__(self):
        return self.name


class City(TimestampModel):
    """Город"""
    id: int
    name: str = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Город'
    )
    country: Country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE,
        related_name='cities',
        verbose_name='Страна'
    )

    class Meta:
        verbose_name_plural = _("Города")
        verbose_name = _("Город")

    def __str__(self):
        return self.name


class Street(TimestampModel):
    """Улица"""
    id: int
    name: str = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Улица'
    )

    class Meta:
        verbose_name_plural = _("Улицы")
        verbose_name = _("Улица")

    def __str__(self):
        return self.name


class Location(TimestampModel):
    """Локация"""
    id: int
    country: Country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        related_name='locations',
        verbose_name='Страна'
    )
    city: City = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='locations',
        verbose_name='Город',
        null=True,
        blank=True
    )
    street: Street = models.ForeignKey(
        'Street',
        on_delete=models.CASCADE,
        related_name='locations',
        verbose_name='Улица',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = _("Локации")
        verbose_name = _("Локация")

    def __str__(self):
        return f'{self.country.name}'


class Company(TimestampModel):
    """Компания"""
    id: int
    name: str = models.CharField(
        max_length=255,
        verbose_name='Компания'
    )
    company_description: str = models.TextField(
        null=False,
        blank=False,
        verbose_name='Текст компании'
    )
    website: str = models.URLField(
        null=True,
        blank=True,
        verbose_name='Веб-сайт компании'
    )
    location: Location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
        verbose_name='Локация компании'
    )

    class Meta:
        verbose_name_plural = _("Компании")
        verbose_name = _("Компания")

    def __str__(self):
        return self.name


class Technology(TimestampModel):
    """Технологии (Python, Docker, React, etc)"""
    id: int
    technology_name: str = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Технология'
    )

    class Meta:
        verbose_name_plural = _("Технологии")
        verbose_name = _("Технология")

    def __str__(self):
        return self.technology_name


class Position(TimestampModel):
    """Позиция"""
    id: int
    name: str = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Позиция'
    )

    class Meta:
        verbose_name_plural = _("Позиции")
        verbose_name = _("Позиция")

    def __str__(self):
        return self.name


class EmploymentType(TimestampModel):
    """Тип занятости"""
    id: int
    name: str = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=True,
        verbose_name='Название занятости'
    )

    class Meta:
        verbose_name_plural = _("Типы занятостей")
        verbose_name = _("Тип занятости")

    def __str__(self):
        return self.name
