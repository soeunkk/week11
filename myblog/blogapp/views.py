from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blogapp/home.html')

def community(request):
    return render(request, 'blogapp/community.html')
