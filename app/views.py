from django.http import request
from django.shortcuts import render

# Create your views here.
def BRadmin_index(request):
    return render(request,'BRadmin_index.html')

def BRadmin_profiledash(request):
    return render(request,'BRadmin_profiledash.html')

def BRadmin_Training(request):
    return render(request,'BRadmin_Training.html')

def BRadmin_trainingteam1(request):
    return render(request,'BRadmin_trainingteam1.html')
def BRadmin_trainerstable(request):
    return render(request,'BRadmin_trainerstable.html')
def BRadmin_topictable(request):
    return render(request,'BRadmin_topictable.html')
def BRadmin_completedtasktable(request):
    return render(request,'BRadmin_completedtasktable.html')
def BRadmin_trainingprofile(request):
    return render(request,'BRadmin_trainingprofile.html')
def BRadmin_traineestable(request):
    return render(request,'BRadmin_traineestable.html')     
                   

