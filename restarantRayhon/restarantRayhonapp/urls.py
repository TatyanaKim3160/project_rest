from django.urls import path
from . import views  #подключаем представление

urlpatterns=[
    path('',views.main, name='home'),
    path('about/',views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('delivery/', views.delivery, name='delivery'),
    path('register/', views.register, name='register'),

]


