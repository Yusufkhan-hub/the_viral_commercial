from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request,'index.html')
    
def aboutus(request):
    return render(request,'about.html')
    
def contact(request):
    return render(request,'contact.html')
        
def services(request):
    return render(request,'services.html')
    
def portofolio(request):
    return render(request,'portfolio.html')