from django.contrib import admin
from CookieSessionApp import views
from django.urls import path, re_path 


urlpatterns = [


	path('admin/', admin.site.urls),
	
	re_path(r'^set_cookie/(\w+)/(\w+)/$', views.set_cookie),
	re_path(r'^set_cookie2/(\w+)/(\w+)/$', views.set_cookie2),
	re_path(r'^get_cookie/(\w+)/$', views.get_cookie),
	path('get_allcookies/', views.get_allcookies),
	re_path(r'^delete_cookie/(\w+)/$', views.delete_cookie),
	
	path('', views.index),
	path('index/', views.index),
	
	# 可以直接在index執行 
	# no template html required
	re_path(r'^set_session/(\w+)/(\w+)/$', views.set_session),
	re_path(r'^get_session/(\w+)/$', views.get_session),
	path('get_allsessions/', views.get_allsessions),
	
	path('vote/', views.vote),	
	re_path(r'^set_session2/(\w+)/(\w+)/$', views.set_session2),
	re_path(r'^delete_session/(\w+)/$', views.delete_session),

	path('login/', views.login),	
	path('logout/', views.logout),	
]