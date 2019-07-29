from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User

# 使用 objects.all()方法讀取 User 資料表所有資料

def index(request):
	# 用 request.user.is_authenticated 檢查使用者是否認證過
	if request.user.is_authenticated:
	   name=request.user.username
	return render(request, "index.html", locals())

def login(request):
	if request.method == 'POST':
		name = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=name, password=password)
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return redirect('/index/')
				message = '登入成功！'
			else:
				message = '帳號尚未啟用！'
		else:
			message = '登入失敗！'
	return render(request, "login.html", locals())
	
def logout(request):
	auth.logout(request)
	return redirect('/index/')	

def adduser(request):	
	try:
		user=User.objects.get(username="test")
	except:
		user=None
		message = "沒有 test 帳號!"

	if user!=None:
		message = user.username + " 帳號已建立!"
		return HttpResponse(message)
	else:	# 建立 test 帳號
		# 建立帳號後，輸入郵件帳號、密碼			
		user=User.objects.create_user("test","test@test.com.tw","aa123456")
		user.first_name="wen" # 姓名
		user.last_name="lin"  # 姓氏
		user.is_staff=True	# 工作人員狀態
		user.save()
		return redirect('/admin/')