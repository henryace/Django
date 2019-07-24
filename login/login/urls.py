from django.urls import path
from django.contrib import admin
from loginapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index),
    path('index/', views.index),

    path('login/', views.login),
    path('logout/', views.logout),	
	
	path('adduser/', views.adduser),	
]