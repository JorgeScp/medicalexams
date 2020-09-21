from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.core.validators import RegexValidator

class Exams(models.Model):
  # STATUS = [
  #     ('active', 'Active'),
  #     ('inactive', 'Inactive')
  # ]

  # GENDER = [
  #     ('male', 'Male'),
  #     ('female', 'Female')
  # ]

  exams             = models.CharField(max_length=800)
  apply             = models.CharField(max_length=800)

  def __str__(self):
    return f'{self.exams}'

  def get_absolute_url(self):
    return reverse('exams-detail', kwargs={'pk': self.pk})
