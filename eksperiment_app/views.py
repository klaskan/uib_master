from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Eksperiment
from .forms import EksperimentForm

#Mitt bruk
import random
import time
# Create your views here.

#Seksjon 1
rand_penger = Eksperiment.utbetalt
sansynlighet1 = 0
all_penger = Eksperiment.objects.all()
utbetaling = Eksperiment.utbetalt
utbetaling_etter_skatt = Eksperiment.faktisk_utbetaling

def index(request):
    return render(request,'index.html',{})

def about(request):
    return render(request, 'about.html',{})

def waiting(request):
    return render(request, 'waiting.html', {})

def revidert(request):
    return render(request, 'revidert.html',{}) 

def eksperiment(request):
   

    form = EksperimentForm(request.POST or None)
    if form.is_valid():
        form.save() 
        form = EksperimentForm(request.POST or None)

        return redirect('waiting')
    
    return render(request, 'eksperiment.html', {'utbetaling' : utbetaling, 
                                                'sansynlighet1' : sansynlighet1,
                                                'form': form, 
                                                'all_penger': all_penger,
                                                'count': count(),
                                                'utbetaling_etter_skatt' : utbetaling_etter_skatt,
                                                })




#Utregninger og andre ting.

def wait():
    time.sleep(5)
    return redirect('eksperiment')


def count():
    sum_all = 0
    for i in Eksperiment.objects.all():
        sum_all = sum_all + i.deklarert_inntekt
    return float(sum_all)