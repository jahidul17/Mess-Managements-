from django.db import models
from django.contrib.auth.models import User

class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True)

    district = models.CharField(max_length=50,null=True,blank=True)
    thana = models.CharField(max_length=50,null=True,blank=True)
    address = models.TextField(null=True,blank=True)

    guardian_name = models.CharField(max_length=100)
    guardian_phone = models.CharField(max_length=15)

    seat_number = models.CharField(max_length=10, unique=True)
    join_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.full_name


