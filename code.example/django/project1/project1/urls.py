from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'app1.views.main', name='main'),
    url(r'^api$', 'app1.views.api', name='api'),
    url(r'^hello/', 'app1.views.hello', name='hello'),
    url(r'^login$', 'app1.views.login', name='login'),
    url(r'^admin/', include(admin.site.urls)),
)
