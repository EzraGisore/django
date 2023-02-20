from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def services(request):
    return render(request,'services.html')
def contactcopy(request):
    return render(request,'contact (copy).html')
def about(request):
    return render(request, 'about (copy).html')
def rhino_index(request):
    return render(request, 'rhino_index.html')