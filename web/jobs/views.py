from django.core.paginator import Paginator
from django.shortcuts import render
from jobs.models import Job
from jobs.forms import JobsSearchForm


def index(request):
	jobs_list = Job.objects.filter(approved = True).order_by('created')
	paginator = Paginator(jobs_list, 25)

	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1
	
	try:
		jobs = paginator.page(page)
	except(EmptyPage, InvalidPage):
		jobs = paginator.page(paginator.num_pages)
	context = {'jobs': jobs}
	template = 'jobs/index.html'
	return render(request, template, context)

def jobs(request):
	form = JobsSearchForm(request.GET)
	jobs = form.search()
	contact = {'jobs', jobs}
	template = 'search/search.html'
	return render(request, template, context)

def contact(request):
	context = locals()
	template = 'contact.html'
	return render(request, template, context)

def about(request):
	context = locals()
	template = 'about.html'
	return render(request, template, context)

def faq(request):
	context = locals()
	template = 'faq.html'
	return render(request, template, context)