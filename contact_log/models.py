from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Rank(models.Model):
    class Meta:
        verbose_name = "Rank"
        verbose_name_plural = "Ranks"
    
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.name}'

class Contact(models.Model):
    name = models.CharField(max_length=50)
    rank = models.ForeignKey(
        Rank,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    picture = models.ImageField(blank=True, upload_to="pictures/contact_log/")
    creating_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    
    
    # def __str__(self) -> str:
    #     if self.last_name == "":
    #         return f"{self.name}, {self.position}"
    #     return f"{self.name} {self.last_name}, {self.position}"
# Create your models here.
