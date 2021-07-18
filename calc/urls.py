from django.urls import path
from calc import views
urlpatterns = [
      path('',views.index, name='index'),
      path('about/',views.about, name='about'),
      path('skill/',views.skill, name='skill'),
      path('contact/',views.contact, name='contact')
]
