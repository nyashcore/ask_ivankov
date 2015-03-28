from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def index(request):
	return render(request, 'index.html', {})
def page(request):
	hello = 'Hello, World'
	return render(request, 'page.html', {'hello': hello})  
def hello(request):
	message = request.get_host()
	return HttpResponse(message)
def current_datetime(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('current_datetime.html', c)
def search(request):
	message = ''
	var = request.GET.getlist('one')
	for item in var:
		message += item
		message += ' '
	return HttpResponse(message)
def getpost(request):
	greeting = 'Hello, World!'
	get_params = request.GET.items()
	post_params = request.POST.items()
	return render(request, 'getpost.html', {'greeting': greeting, 'get_params': get_params, 'post_params': post_params})
