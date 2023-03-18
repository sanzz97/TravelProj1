from . import views
from django.urls import path


urlpatterns = [
    path('',views.demo,name='demo'), #we need to add views here, urls will be connected to views where we define our fns
    # path('about/',views.about, name='about'), #another url - about page
    # path('contact/',views.contact,name='contact')
    # path('operations/',views.operations,name='operations')
]

