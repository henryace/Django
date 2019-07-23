from django.contrib import admin
from studentsapp import views
from django.urls import path, re_path 

"""
update to 2.2.3 2019/7/22
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 
# admin.site.urls
# administrator login in module

urlpatterns = [
    path('admin/', admin.site.urls),
	path('listone/', views.listone),
	path('listall/', views.listall),
    path('', views.index),
    path('index/', views.index),

	path('post/', views.post), # POST 傳送表單
	path('post1/', views.post1), #資料新增，資料不驗證
	path('post2/', views.post2), #資料新增，資料作驗證

	re_path(r'^delete/(\d+)/', views.delete),
	
	re_path(r'^edit/(\d+)/$', views.edit), # 由 瀏覽器 開啟
	re_path(r'^edit/(\d+)/(\w+)$', views.edit), # 由 edit.html 按 送出 鈕

	re_path(r'^edit2/(\d+)/(\w+)$', views.edit2),
	re_path(r'^postform/$', views.postform), # 表單驗證
]