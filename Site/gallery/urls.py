"""Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url

urlpatterns = [
    url(r'^main/', 'gallery.views.main_page', name='main_page'),
    url(r'^send-comment/', 'gallery.views.send_comment', name='send_comment'),
    url(r'^get-comments/', 'gallery.views.get_comments', name='get_comments'),
    url(r'^delete-comment/(?P<id_comment>[0-9]+)$', 'gallery.views.delete_comment', name='delete_comment'),
    url(r'^get-edit-form/(?P<id_comment>[0-9]+)$', 'gallery.views.get_edit_form', name='get_edit_form'),
    url(r'^edit-comment/(?P<id_comment>[0-9]+)$', 'gallery.views.edit_comment', name='edit_comment'),
]
