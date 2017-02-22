from django.conf.urls import url
from django.views.generic import RedirectView
from . import views

urlpatterns = [
	# /usage/
    url(r'^$', views.index, name='index'),

    # /usage/convert-to-text/
    url(r'^convert-to-text/$', views.usage, name='convert-to-text'),
    # /usage/contact/
    url(r'^contact/$', views.contact, name='contact'),
    # /usage/installation/
    url(r'^installation/$', views.installation, name='installation'),
    # /usage/convert/
    url(r'^convert/$', views.convert.as_view(), name='convert'),
    # /usage/<file_id>/
    url(r'^convert/(?P<file_id>[0-9]+)/$', views.convertor, name='convertor'),
]