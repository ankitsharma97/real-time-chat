from django.db import models

# Create your models here.
class Chat(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
    group = models.ForeignKey('Group_chat' , on_delete=models.CASCADE)
    def __str__(self):
        return self.group
    
    
    
class Group_chat(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
