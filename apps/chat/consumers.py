import json

from channels.generic.websocket import AsyncWebsocketConsumer

from apps.chat.generator import generate_array
from apps.chat.image import get_image_data


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        sort_type = text_data_json["sort_type"] if text_data_json["sort_type"] else ""
        keys, array = generate_array(50, sort_type)
        array = array.tolist() if sort_type == "" else text_data_json["array"]


        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat.message",
                "message": {
                    "pic": get_image_data(keys, array),
                    "sort_type": sort_type,
                    "array": array
                }
            }
        )

    # Receive message from room group
    async def chat_message(self, event):

        # Send message to WebSocket
        await self.send(
            text_data=json.dumps({
                "pic": event["message"]['pic'],
                "sort_type": event["message"]["sort_type"],
                "array": event["message"]["array"]
            })
        )
