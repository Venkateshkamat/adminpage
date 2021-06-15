import student
from django.shortcuts import render

from .models import studenttable
# Create your views here.

def studentdata(request):

    stud = studenttable.objects.all()

    return render(request,'studentinfo.html',{'stud':stud})
