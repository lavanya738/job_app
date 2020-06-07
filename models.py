from django.db.models import (Model,TextField)

class JobListing(Model):
    title=TextField(null=True,blank=True)
    description=TextField(null=True,blank=True)
# Create your models here.
