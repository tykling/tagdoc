from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    ### admin site
    url(r'^admin/', include(admin.site.urls)),
)
