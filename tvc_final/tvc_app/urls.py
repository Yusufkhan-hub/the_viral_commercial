from django.urls import path
from .views import home,aboutus,contact,portofolio,services
urlpatterns = [
    path('',home,name="home"),
    path('aboutus',aboutus,name="aboutus"),
    path('contact',contact,name="contact"),
    path('services',services,name="services"),
    path('portofolio',portofolio,name="portofolio"),
    
]