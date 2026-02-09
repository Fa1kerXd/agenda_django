from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now())
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    pictures = models.ImageField(blank=True, upload_to="pictures/%Y/%m")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"