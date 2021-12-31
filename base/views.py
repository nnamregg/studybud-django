from django.shortcuts import render
from .models import Room

# rooms = [
#     {'id': 1, 'name': 'Lets do it!'},
#     {'id': 2, 'name': 'hahahahah!'},
#     {'id': 3, 'name': 'what im i gonna do with a soul anyway?'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}    
    return render(request, 'base/room.html', context)
