from django.shortcuts import get_object_or_404, render
from .models import Group_chat,Chat
# Create your views here.
def index(request,grp_name):
    # group, created = Group.objects.get_or_create(name=grp_name)
    # group = get_object_or_404(Group, name=grp_name)
    
    chats=[]
    
    group = Group_chat.objects.filter(name = grp_name).first()
    if group is None:
        group = Group_chat.objects.create(name = grp_name)
        
    else:
        chats = Chat.objects.filter(group=group)
        
    
    print("hi")
    return render(request, './index.html',{
        'grp_name':grp_name,
        'chats':chats
        })