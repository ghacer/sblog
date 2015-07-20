from django.conf.urls import url
import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^post/(?P<pk>\d+)/$', views.post, name='post'),
	url(r'^category/(?P<pk>\d+)/$', views.category, name='category'),
#	url(r'^about$', views.about, name='about'),
]
