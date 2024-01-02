from django.contrib import admin
from django.urls import path
from . import views


urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('header/',views.header,name='header'),
    path('aboutus2/', views.aboutus2, name='aboutus2'),
    path('integrated/',views.integrated, name='integrated'),
    path('srevice/', views.service,name='service'),
    path('statics/',views.statics ,name='statics'),
    path('salient/', views.salient ,name='salient'),
    path('tenant/',views.tenant, name='tenant'),
    path('target/', views.target,name='target'),
    path('jalgaon/', views.jalgaon,name='jalgaon'),
    path('population/' ,views.population, name='population'),
    path('demografic/',views.demografic,name='demografic'),
    path('education/',views.education, name='education'),
    path('industry/',views.industry,name='industry'),
    path('scenario/', views.scenario,name='scenario'),
    path('vision/', views.vision, name='vision'),
    path('tourism/', views.tourism,name='tourism'), 
    path('gallery/',views.gallery,name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('quote/',views.quote,name='quote'),
    path('privacy/',views.privacy,name='privacy'),
    path('disclaimer/',views.disclaimer,name='disclaimer'),
    path('gallery/',views.gallery,name='gallery'),
    path('contact1/', views.contact1, name='contact1'),
    path('home/', views.home, name='home'),
    path('mumbai/', views.mumbai, name='mumbai'),
    
    path('footer/',views.footer,name='footer'),
    
]