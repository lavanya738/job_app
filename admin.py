from django.contrib import admin
from .models import JobListing

# Register your models here.
class JobListingAdm(admin.ModelAdmin):
    list_display=['title','description']
    
admin.site.register(JobListing,JobListingAdm)
