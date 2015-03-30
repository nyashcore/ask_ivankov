from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime

def index(request):
	return render(request, 'index.html', {})
def register(request):
	return render(request, 'signup.html', {})
def tag(request, tag):
	return render(request, 'index.html', {'tag': tag})
def login(request):
	return render(request, 'login.html', {})
def ask(request):
	return render(request, 'ask.html', {})
def question(request, question):
	return render(request, 'question.html', {'question': question})
def search(request):
	message = ''
	var = request.GET.getlist('one')
	for item in var:
		message += item
		message += ' '
	return HttpResponse(message)
def getpost(request, tag):
	greeting = 'Hello, World!'
	get_params = request.GET.items()
	post_params = request.POST.items()
	return render(request, 'getpost.html', {'tag': tag, 'greeting': greeting, 'get_params': get_params, 'post_params': post_params})
