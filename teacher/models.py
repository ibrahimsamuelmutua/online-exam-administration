from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator

from django.contrib.auth.models import User


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/Teacher/', null=True, blank=True)
    address = models.EmailField(max_length=40, null=False, blank=False)
    mobile = models.CharField(max_length=20, null=False)
    status = models.BooleanField(default=False)
    salary = models.PositiveIntegerField(null=True)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name
