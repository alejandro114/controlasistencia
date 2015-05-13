from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'controlasistencia.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^trabajadores/$', 'tablas.views.index'),
    url(r'^proyectos/$','tablas.views.index2'),
    url(r'^controlasistencia/$','tablas.views.index3'),
    url(r'^tareasencargadas/$','tablas.views.index4'),
]
