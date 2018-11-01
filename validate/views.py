from django.http import HttpResponse
from django.shortcuts import render
import operator


def portfolio(request):
	return render(request, 'jobs/portfolio.html')
	

