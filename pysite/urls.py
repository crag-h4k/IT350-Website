from django.contrib import admin
from django.urls import path

from django.views.generic.base import RedirectView

urlpatterns = [
    path('secure-admin-login/', admin.site.urls, name='admin'),
    path('admin/', RedirectView.as_view(url='/'))
]

#changing site header and title
admin.site.site_header = 'Dane Morgan\'s Secure Admin Page'
admin.site.site_title = 'Dane Morgan\'s Site Admin Page'
