from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to="pictures/contact_log/")
    
    
    # def __str__(self) -> str:
    #     if self.last_name == "":
    #         return f"{self.name}, {self.position}"
    #     return f"{self.name} {self.last_name}, {self.position}"
# Create your models here.
