from django.conf.urls import patterns,url,static
from rango import views
from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = patterns('',url(r'^$',views.index,name='index'),
                       url(r'^about',views.about,name='about'),
                       url(r'^add_category/$', views.add_category, name='add_category'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
                       url(r'^restricted/', views.restricted, name='restricted'),
                       url(r'^goto/', views.track_url, name='goto'),
                       url(r'^add_profile/', views.register_profile, name='register_profile'),
                       url(r'^profile/', views.profile, name='profile'),
                       )

if not settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
