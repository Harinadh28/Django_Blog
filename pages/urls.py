from django.contrib import admin
from django.urls import path
from .views import home,contact,about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    

]