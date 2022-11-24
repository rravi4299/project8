from django.shortcuts import render

# Create your views here.
def ravi(request):
    d={'a':20,'b':10}
    return render(request,'ravi.html',d)
    