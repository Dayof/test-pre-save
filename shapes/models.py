from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db import models


class ShapeB(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField()

    def __str__(self):
       return f'name: {self.name}, size: {self.size}'


class ShapeA(models.Model):
    shapes_b = models.ManyToManyField(ShapeB, blank=True)
    name = models.CharField(max_length=200)
    size = models.IntegerField()

    def __str__(self):
        return f'name: {self.name}, size: {self.size}'


class ShapeC(models.Model):
    shapes_b_id = models.ForeignKey(ShapeB, on_delete=models.CASCADE)


@receiver(pre_save, sender=ShapeA)
def callback_create_shapeb(sender, instance, *args, **kwargs):
    if instance.size == 5:
        new_obj = ShapeB(name=instance.name, size=instance.size)
        new_obj.save()


@receiver(post_save, sender=ShapeB)
def callback_create_shapec(sender, instance, *args, **kwargs):
    new_obj = ShapeC.objects.create(shapes_b_id=instance)
    new_obj.save()
