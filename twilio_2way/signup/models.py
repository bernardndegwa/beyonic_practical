from django.db import models


class PhoneEmail(models.Model):
    text = models.TextField(default='')
