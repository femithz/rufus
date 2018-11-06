from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
 
from .models import Job
from .models import Front










def home(request):
	front = Front.objects.all() 	
	return render(request, 'jobs/home.html', {'jobs':front})





def portfolio(request):
	job = Job.objects.all() 	
	return render(request, 'jobs/portfolio.html', {'jobs':job})




def signup (request):
	if request.method =='POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username']), 
				return render(request, 'jobs/signup.html', {'error':'Username has already been taken!'})
			except User.DoesNotExist:         
		 		user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
		 		
		 		user.backend = 'django.contrib.auth.backends.ModelBackend'

		 		auth.login(request,user)
			return redirect('home')
		else: 
					return render(request, 'jobs/signup.html', {'error':'Passwords must match!'})
	else:
		return render (request, 'jobs/signup.html',)

def login (request):
	if request.method == 'POST':
			user = auth.authenticate(username=request.POST['username'],password=request.POST['password']) 
			if user is not None:
				auth.login(request,user)
				return redirect('home')
			else:
				return render(request, 'jobs/login.html', {'error':'username or password is incorrect!'})

	else:
		return render (request, 'jobs/login.html')

def logout (request):
	if request.method == 'POST':
		auth.logout(request)
		return redirect('home')

	