from django.db import models
from datetime import date

from django.urls import reverse


class chop(models.Model):
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Телохранители"
        verbose_name_plural = "Телохранители"


class Men(models.Model):
    title = models.CharField("Название", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    name = models.ManyToManyField(chop, verbose_name="Телохранитель", related_name="Men_chop")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Men_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"