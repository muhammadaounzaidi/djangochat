from django.shortcuts import render
from .models import ChatRoom
# Create your views here.
def index(request):
    chatrrooms = ChatRoom.objects.all()
    return render(request,'chatapp/index.html', context={"chatrooms":chatrrooms})     

def chatroom(request,slug):
    chatroom=ChatRoom.objects.get(slug=slug)
    return render(request,'chatapp/chatroom.html', context={"chatroom":chatroom})