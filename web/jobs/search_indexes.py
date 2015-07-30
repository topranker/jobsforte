import datetime
from django.utils import timezone
from haystack import indexes
from jobs.models import Job

class JobIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)
	title = indexes.CharField(model_attr='title')
	organisation = indexes.CharField(model_attr='organisation')
	level = indexes.CharField(model_attr='level')
	employment_type = indexes.CharField(model_attr='employment_type')
	experience = indexes.CharField(model_attr='experience')
	location = indexes.CharField(model_attr='location')
	source = indexes.CharField(model_attr='source')
	url = indexes.CharField(model_attr='url')
	created = indexes.DateTimeField(model_attr='created')

	def get_model(self):
		return Job

	def index_queryset(self, using=None):
		"""Used when the entire index for model is updated."""
		return self.get_model().objects.filter(created__lte=timezone.now())