from django.contrib import admin
from .models import Chat,Group_chat
# Register your models here.

@admin.register(Chat)
class chatAdmin(admin.ModelAdmin):
    list_display = ['message','date','group']
    
    
@admin.register(Group_chat)
class groupAdmin(admin.ModelAdmin):
    list_display = ['name']
