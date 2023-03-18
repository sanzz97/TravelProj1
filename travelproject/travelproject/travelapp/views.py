from django.shortcuts import render #to display html files in templates folder
from django.http import HttpResponse
from . models import Place,Team #to render the contents in our 'place;' table in our webpage

# Create your views here.
# here we need to add all functionalities to render our page
# def demo(request): #we need to add request parameter
#     return HttpResponse('hello world') #it will be rendered on the page by httpresponse

#in case if u want to render/display a full html file
# def demo(request):
#     return render(request,'index1.html')

# def addition(request):
#     x= int(request.GET['number1'])
#     y= int(request.GET['number2'])
#     res = x+y
#     return render(request,'result.html',{'result':res})
# def operations(request):
#     x = int(request.GET['number1'])
#     y = int(request.GET['number2'])
#     add = x+y
#     sub = x-y
#     mul = x*y
#     div = x/y
#     mod = x%y
#     exp = x**y
#     floor = x//y
#     return render(request,'result.html',{'a':add,'s':sub,'m':mul,'d':div,'m1':mod,'e':exp,'f':floor})


# to fetch all objects from 'place' table
def demo (request):
    obj = Place.objects.all()
    obj1 = Team.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1}) #pass the values of obj using dict

