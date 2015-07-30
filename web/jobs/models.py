from django.db import models


class Job(models.Model):
	approved = models.BooleanField(default=False)
	title = models.CharField(max_length=170, null=True, blank=True)
	level = models.CharField(max_length=130, null=True, blank=True, default='None')
	organisation = models.CharField(max_length=170, null=True, blank=True)
	industry = models.CharField(max_length=130, null=True, blank=True)
	specialization = models.CharField(max_length=170, null=True, blank=True)
	location = models.CharField(max_length=130, null=True, blank=True)
	employment_type = models.CharField(max_length=30, null=True, blank=True)
	experience = models.CharField(max_length=170, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	requirement = models.CharField(max_length=170, null=True, blank=True)
	source = models.CharField(max_length=130, null=True, blank=True)
	salary = models.CharField(max_length=50, default='Competitive', null=True, blank=True)
	created = models.DateTimeField('Date Scraped', editable=False, auto_now_add=True)
	url = models.URLField()

	def __unicode__(self):
		return self.title + " in " + self.location