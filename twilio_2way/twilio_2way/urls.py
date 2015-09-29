from django.conf.urls import patterns, include, url
from django.contrib import admin
from signup import views

urlpatterns = patterns('',
    url(r'^$', 'signup.views.home_page', name='home_page'),
    # url(r'^blog/', include('blog.urls')),

   # url(r'^admin/', include(admin.site.urls)),
)

