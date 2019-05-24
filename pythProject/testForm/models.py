from django.contrib.postgres.fields import JSONField
from django.db import models

class FormDataModel(models.Model):
    data = JSONField()
    
