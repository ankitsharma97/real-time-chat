from django.urls import path

from . import consumers

websocket_urlpatterns = [
    # path('ws/Async/', consumers.MyAsync.as_asgi()),
    path('ws/Async/<str:grp_name>/', consumers.MyAsync.as_asgi()),
    path('ws/Sync/', consumers.MySync.as_asgi()),
]