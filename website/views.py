from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home_page_view(request):
	return render(request, 'website/home.html')

def index_page_view(request):
	return render(request, 'website/index.html')

def about_page_view(request):
	return render(request, 'website/about.html')
