from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)


class Task(models.Model):
    title = models.CharField(max_length=255, help_text="Task Title")
    description = models.CharField(max_length=500, help_text="Task Description")
    ddate = models.DateField(default=now(), help_text="YYYY-MM-DD")
    CHOICES = [('1', 'Pending'), ('2', 'In Process'), ('3', 'Completed')]
    status = models.CharField(max_length=1, choices=CHOICES, default='1')
    assigned_to = models.CharField(max_length=255)
    task_by = models.CharField(max_length=255)

    class Meta:
        db_table = 'Task'



