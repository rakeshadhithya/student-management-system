from django.db import models
from django.contrib.auth.models import AbstractUser 

class Account(AbstractUser):
    #define choices
    class Role(models.TextChoices):
        MENTOR = "MENTOR", "Mentor"    #first value for database, second value to display to user
        STUDENT = "STUDENT", "Student"
    #store choice
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)
    def __str__(self):
        return self.username
    