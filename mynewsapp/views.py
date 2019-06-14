from django.shortcuts import render

# Create your views here.
import requests
import json

def home(request):
	url="https://newsapi.org/v2/top-headlines?country=in&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def world(request):
	url="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def sports(request):
	url="https://newsapi.org/v2/top-headlines?category=sports&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def entertainment(request):
	url="https://newsapi.org/v2/top-headlines?category=entertainment&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def business(request):
	url="https://newsapi.org/v2/top-headlines?category=business&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def science(request):
	url="https://newsapi.org/v2/top-headlines?category=science&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})

def tech(request):
	url="https://newsapi.org/v2/top-headlines?category=technology&apiKey=89aa79ae8ccb4fabbc83f1a572eaa445&country=in"
	api_request=requests.get(url)
	api=json.loads(api_request.content)
	if api["status"]=="error":
		return render(request,'error.html',{})
	return render(request,'home.html',{'api':api})
