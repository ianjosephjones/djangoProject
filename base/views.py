from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Ian Jones'},
    {'id': 2, 'name': 'Zach Jones'},
    {'id': 3, 'name': 'Micah Jones'},

]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request):
    return render(request, 'base/room.html')
