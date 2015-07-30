from django.contrib import admin
from jobs.models import Job

class JobAdmin(admin.ModelAdmin):
	ordering = ['created']
	list_display = ['title', 'organisation', 'location', 'experience', 'employment_type', 'salary', 'approved',]
	list_filter = ['approved','source','created']
	

admin.site.register(Job, JobAdmin)
