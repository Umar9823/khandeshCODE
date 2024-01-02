from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail




def index(request):
    return render(request,'index.html')
def aboutus2(request):
    return render(request, 'aboutus2.html')
def integrated(request):
    return render(request,'integrated.html')
def service(request):
    return render(request,'service.html' )
def statics(request):
    return render(request, 'statics.html')
def salient( request):
    return render (request, 'salient.html')
def tenant(request):
    return render(request,'tenant.html')
def target(request):
    return render (request,'target.html')
def jalgaon(request):
    return render(request, 'jalgaon.html')
def population(request):
    return render(request,'population.html')
def demografic(request):
    return render(request, 'demografic.html')
def education(request):
    return render(request,'education.html')
def industry(request):
    return render(request, 'industry.html')
def scenario(request):
    return render(request,'scenario.html')
def vision(request):
    return render(request,'vision.html')
def tourism(request):
    return render(request,'tourism.html')
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    if request.method =='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject') 
        message=request.POST.get('message') 
        print(name,email,subject,message) 
        obj=contact(name=name,email=email,subject=subject,message=message)
        obj.save()
    return render (request,'contact.html')
    
    
def quote(request):
    return render(request,'quote.html')
def privacy(request):
    return render(request,'privacy.html')
def disclaimer(request):
    return render(request,'disclaimer.html')
def gallery(request):
    return render(request,'gallery.html')


def contact1 (request):
    if request.method=='POST':
        name=request.POST.get('fname')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        
        data={
            'name':name,
            'email':email,
            'subject':subject,
            'message':message
        }
        message= '''
        New message:{}
        
        
        From:{}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message,'',['umar.shaikh.iqra@gmail.com'])
    return render(request,'contact1.html',{})  

def home(request):
    return render(request,'home.html') 

def mumbai(request):
    return render(request,'mumbai.html')  

def header(request):
    return render(request,'header.html')  

def footer(request):
    return render(request,'footer.html')    
        
           
        

    