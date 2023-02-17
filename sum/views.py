from django.shortcuts import render

# Create your views here.
def index(request):
    x = request.GET.get('x',None)
    y = request.GET.get('y',None)
    if x and y:
        context = {'result':(int(x) + int(y)),
        'x':x,
        'y':y}
    else:
        context = {}
    return render(request,'sum/index.html',context)
