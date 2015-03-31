from django.conf.urls import patterns, include, url
from app1.views import search
from app1.views import getpost
from app1.views import index, register, tag, ask, login, question
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_ivankov.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', index, name='index'),
	url(r'^register/$', register, name='register'),
	url(r'^tag/(?P<tag>\w+)/$', tag, name='tag'),
	url(r'^ask/$', ask, name='ask'),
	url(r'^login/$', login, name='login'),
	url(r'^question/(?P<question>\d+)/$', question, name='question'),
    url(r'^search/$', search, name='search'),
	url(r'^getpost/(\w+)/$', getpost, name='getpost'),
    url(r'^admin/', include(admin.site.urls)),
)
