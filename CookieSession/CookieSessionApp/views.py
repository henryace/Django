from django.shortcuts import render
from django.http import HttpResponse
import datetime

# cookie
# key為 session 的名稱, value為 session 的內容
def set_cookie(request,key=None,value=None):
	# 
	# 以 HttpResponse 建立 response 物件
	# 再以 response 物件 的 set_cookie
	# 方法儲存 Cookie
	#  
	# print out 'Cookie 儲存完畢!'
	#
	response = HttpResponse('Cookie 儲存完畢!')
	response.set_cookie(key,value)
	return response
	
def get_cookie(request,key=None):
	if key in request.COOKIES:
		return HttpResponse('%s : %s' %(key,request.COOKIES[key]))
	else:
		return HttpResponse('Cookie 不存在!')	

def set_cookie2(request,key=None,value=None):
	response = HttpResponse('Cookie 有效時間1小時!')
	response.set_cookie(key,value,max_age=3600)
	return response			
		
def delete_cookie(request,key=None):
	if key in request.COOKIES:
		response = HttpResponse('Delete Cookie: '+key)	
		response.delete_cookie(key)
		return response
	else:
		return HttpResponse('No cookies:' + key)		


# Note
# expires=date
# 指定Cookie的有效日期，當過了有效日期後，那個Cookie 就不會再儲存在瀏覽器；
# date是GMT格式的有效日期。 如果不指定這個參數，該Cookie的有效日期就是使用者 
# 退出瀏覽器時(End of Browser Session)。 
#
# strftime函數將日期換成指定的格式

def index(request):
	if "counter" in request.COOKIES:
		counter=int(request.COOKIES["counter"])
		counter+=1
	else:		
		counter=1
	response = HttpResponse('今日瀏覽次數：' + str(counter))		
	tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1)
	tomorrow = datetime.datetime.replace(tomorrow, hour=0, minute=0, second=0)
	expires = datetime.datetime.strftime(tomorrow, "%a, %d-%b-%Y %H:%M:%S GMT") 
	response.set_cookie("counter",counter,expires=expires)
	return response	

def get_allcookies(request):
	if request.COOKIES!=None:
		strcookies=""
		for key1,value1 in request.COOKIES.items():
			strcookies= strcookies + key1 + ":" + value1 + "<br>"
		return HttpResponse('%s' %(strcookies))
	else:
		return HttpResponse('Cookie 不存在!')	

def set_session(request,key=None,value=None):
	response = HttpResponse('Session 儲存完畢!')
	request.session[key]=value
	return response
	
def get_session(request,key=None):
	if key in request.session:
		return HttpResponse('%s : %s' %(key,request.session[key]))
	else:
		return HttpResponse('Session 不存在!')
		
def vote(request):
	if not "vote" in request.session:
		request.session["vote"]=True
		msg="您第一次投票!"		
	else:		
		msg="您已投過票!"			
	response = HttpResponse(msg)		
	return response					

def get_allsessions(request):
	if request.session!=None:
		strsessions=""
		for key1,value1 in request.session.items():
			strsessions= strsessions + key1 + ":" + str(value1) + "<br>"
		return HttpResponse(strsessions)
	else:
		return HttpResponse('Session 不存在!')	
		
def set_session2(request,key=None,value=None):
	response = HttpResponse('Session 儲存完畢!')
	request.session[key]=value
	request.session.set_expiry(30) # 設持續的時間為30秒
	return response

def delete_session(request,key=None):
	if key in request.session:
		response = HttpResponse('Delete Session: '+key)	
		del request.session[key]
		return response
	else:
		return HttpResponse('No Session:' + key)
	
def login(request):
	#預設帳號密碼
	username = "chiou"
	password = "1234"
	# http://127.0.0.1:8000/login/
	if request.method == 'POST':
		if not 'username' in request.session:
			if request.POST['username']==username and request.POST['password']==password:
				request.session['username']=username #儲存Session
				message=username + " 您好，登入成功！"
				status="login"
	# 再輸入一次 http://127.0.0.1:8000/login/
	else:
		if 'username' in request.session:
			if request.session['username']==username:
				message=request.session['username'] + " 您已登入過了！"
				status="login"				
	return render(request, 'login.html',locals())
	
def logout(request):
	if 'username' in request.session:
		message=request.session['username'] + ' 您已登出!'
		del request.session['username']	#刪除Session	
	return render(request, 'login.html',locals())