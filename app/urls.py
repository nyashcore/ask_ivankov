from django.conf.urls import patterns, url

urlpatterns = patterns('app.views',
	url(r'^$', 'index', name='index'),
	url(r'^register/$', 'register', name='register'),
	url(r'^tag/(?P<tag>\w+)/$', 'tag', name='tag'),
	url(r'^ask/$', 'ask', name='ask'),
	url(r'^login/$', 'login', name='login'),
	url(r'^question/(?P<question>\d+)/$', 'question', name='question'),
	url(r'^add/$', 'add', name='add'),
    url(r'^search/$', 'search', name='search'),
	url(r'^search2/$', 'search2'),
	url(r'^getpost/(\w+)/$', 'getpost', name='getpost'),
)
