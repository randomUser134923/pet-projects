from django.shortcuts import render

from main.function.oil import local_xml

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def index(request):
    template_path = 'main/index.html'
    data = local_xml()
    return render(request,template_path,data)
    
def introductionview(request):
    return render(request,'main/introduction.html')
    
def faqview(request):
    return render(request,'main/faq.html')
    
def productview(request):
    return render(request,'main/product.html')