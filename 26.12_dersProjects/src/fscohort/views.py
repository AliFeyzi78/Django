from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm


# Create your views here.
def home_view(request):
    form = StudentForm()
    my_context = {
        'title': 'clarusway',
        'dict_1': {'djang': 'best framework'},
        'my_list': [2, 3, 4, 5],
        'form': form
    }
    return render(request, "fscohort/home.html", my_context)


def about(request):
    return HttpResponse("Merhaba About.")
