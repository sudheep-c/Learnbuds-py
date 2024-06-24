from django.urls import path
from.import views

urlpatterns = [

    path('base/',views.base,name='base'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('jobs/',views.jobs,name='jobs'),
    path('posts/',views.posts,name='posts'),
    path('contacts/',views.contacts,name='contacts'),

    
]