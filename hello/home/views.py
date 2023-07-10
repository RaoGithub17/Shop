from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    context = {
        "variable1":"new is good",
        "variable2":"old is gold"
    }
    return render(request,'index.html', context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("this is about page")

def services(request):
    return render(request,'services.html')
    #return HttpResponse("this is services age")

def contact(request):
    return render(request,'contact.html')
    #return HttpResponse("this is contact page")
