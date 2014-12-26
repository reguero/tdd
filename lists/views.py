from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
  response = render(request, 'home.html')
  #print(repr(response.content))
  return response

