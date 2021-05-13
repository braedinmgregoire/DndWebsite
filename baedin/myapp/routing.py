from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/tavern/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]

"""channel_routing = [
    route('websocket.receive', 'tavern.consumers.ws_echo'),
    route('websocket.connect', 'tavern.consumers.ws_add',
        path=r'^/tavern/(?P<room>\w+)$'),
]"""
