from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models


class ShapeA(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField()

    def __str__(self):
        return f'name: {self.name}, size: {self.size}'


class ShapeB(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField()

    def __str__(self):
       return f'name: {self.name}, size: {self.size}'


@receiver(pre_save, sender=ShapeA)
def my_callback(sender, instance, *args, **kwargs):
    if instance.size == 5:
        new_obj = ShapeB(name=instance.name, size=instance.size)
        new_obj.save()
