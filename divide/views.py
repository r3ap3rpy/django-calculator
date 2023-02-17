from django.shortcuts import render

# Create your views here.
def index(request):
    x = request.GET.get('x',None)
    y = request.GET.get('y',None)
    if x and y:
        context = {'result':(round(int(x) / int(y),2)),
        'x':x,
        'y':y}
    else:
        context = {}
    return render(request,'divide/index.html',context)
