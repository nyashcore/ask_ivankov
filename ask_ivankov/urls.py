from django.conf.urls import patterns, include, url
from app1.views import hello
from app1.views import current_datetime
from app1.views import search
from app1.views import getpost
from app1.views import index
from app1.views import page
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_ivankov.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', index),
    url(r'^hello/$', hello),
	url(r'^page/$', page),
    url(r'^time/$', current_datetime),
    url(r'^search/$', search),
	url(r'^getpost/$', getpost),
    url(r'^admin/', include(admin.site.urls)),
)
