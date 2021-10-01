from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Ian Jones'},
    {'id': 2, 'name': 'Zach Jones'},
    {'id': 3, 'name': 'Micah Jones'},

]


def home(request):
    return render(request, 'home.html', {'rooms': rooms})


def room(request):
    return render(request, 'room.html')
