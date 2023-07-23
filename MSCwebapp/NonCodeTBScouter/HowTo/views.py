from django.shortcuts import render

# Create your views here.

def HowTo(request):
  return render(request, 'HowTo.html') 