from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request):
    my_context = {
        'title': 'clarusway',
        'dict_1': {'djang': 'best framework'},
        'my_list': [2, 3, 4, 5]
    }
    return render(request, "fscohort/home.html", my_context)


def about(request):
    return HttpResponse("Merhaba About.")
