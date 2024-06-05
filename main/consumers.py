from channels.consumer import AsyncConsumer,SyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
from asyncio import sleep
from asgiref.sync import async_to_sync
from .models import Group_chat,Chat

class MySync(SyncConsumer):
    def websocket_connect(self,event):
        print("hello_connected",event)
        print("channel_layer",self.channel_layer)
        async_to_sync(self.channel_layer.group_add)('prox',self.channel_name)
        self.send({
            'type':'websocket.accept'
        })  
        
        
    def websocket_receive(self,event):
        print("received",event)
        for i in range(50):
            self.send({
                'type':'websocket.send',
                'text':str(i)
            })
            sleep(10) 
        
        
        
    def websocket_disconnect(self,event):
        print('WebSoket_disconnect',event)
        raise StopConsumer
        
        
from channels.generic.websocket import AsyncConsumer
import json

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Group_chat, Chat

class MyAsync(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        print("connected_channel_layer", self.channel_layer)
        print("connected_channel_name", self.channel_name)

        self.grp_name = self.scope['url_route']['kwargs']['grp_name']
        await self.channel_layer.group_add(
            self.grp_name,
            self.channel_name
        )
        await self.accept()
        
    async def websocket_receive(self, event):
        print("received", event)
        message = json.loads(event['text'])
        
        group, created = Group_chat.objects.get_or_create(name=self.grp_name)
        
        chat = Chat.objects.create(
            message=message['message'],
            group=group
        )
        
        await self.channel_layer.group_send(
            self.grp_name, {
                'type': 'chat.message',
                'text': message['message']
            }
        )
        
    async def chat_message(self, event):
        print("Hello")
        print("message", event)
        await self.send({
            'type': 'websocket.send',
            'text': json.dumps({
                'message': event['text']
            })
        })
        
    async def websocket_disconnect(self, event):
        print('WebSocket_disconnect')
        print("disconnected_channel_layer", self.channel_layer)
        print("disconnected_channel_name", self.channel_name)
        
        await self.channel_layer.group_discard(
            self.grp_name,
            self.channel_name
        )
