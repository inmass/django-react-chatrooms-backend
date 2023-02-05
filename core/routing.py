# chat/routing.py
from django.urls import re_path

from user import consumers

websocket_urlpatterns = [
    re_path(r"room/(?P<room_name>[\w-]+)/$", consumers.ChatConsumer.as_asgi()),
]