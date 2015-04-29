# -*- coding: utf-8 -*-
from django.core.context_processors import csrf
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse, Http404
import json, datetime

questions = [
	{'id': 1, 'title': u'Как на луну', 'content': u'читай тут ->',
		'tags': ['moon', 'howto'], 'created': datetime.datetime.now()},
	{'id': 2, 'title': u'Как на луну', 'content': u'читай тут ->',
		'tags': ['moon', 'howto'], 'created': datetime.datetime.now()},
	{'id': 3, 'title': u'Как на луну', 'content': u'читай тут ->',
		'tags': ['moon', 'howto'], 'created': datetime.datetime.now()},
]
def index(request):
	context = {
		'questions': questions
	}
	return render(request, 'index.html', context)
def register(request):
	return render(request, 'signup.html', {})
def tag(request, tag):
	return render(request, 'index.html', {'tag': tag})
def login(request):
	return render(request, 'login.html', {})
def ask(request):
	return render(request, 'ask.html', {})
def question(request, question):
	return render(request, 'question.html', {'question': int(question)})
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
def search2(request):
	try:
		var = int(request.GET.get('var', ''))
	except ValueError:
		var = 1
#		raise Http404
	data = {
		'query': request.GET.get('query'),
		'var': var,
	}
	return HttpResponse(json.dumps(data), content_type='application/json')
def add(request):
	return HttpResponse(request.POST.get('pass'))
