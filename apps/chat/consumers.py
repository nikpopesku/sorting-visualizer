import json
from asyncio import ensure_future
from typing import Optional

from channels.generic.websocket import AsyncWebsocketConsumer

from apps.chat.generator import generate_array
from apps.chat.image import get_image_data
from apps.sort.method.bubble import (bubble_sort, bubble_sort_average,
                                     bubble_sort_best, bubble_sort_worst,
                                     bubble_space_complexity)
from apps.sort.method.counting import (counting_iterative_average,
                                       counting_iterative_best,
                                       counting_iterative_worst, counting_sort,
                                       counting_space_complexity)
from apps.sort.method.heapsort import (heap_sort, heapsort_iterative_average,
                                       heapsort_iterative_best,
                                       heapsort_iterative_worst,
                                       heapsort_space_complexity)
from apps.sort.method.insertion import (insertion_average, insertion_best,
                                        insertion_sort,
                                        insertion_space_complexity,
                                        insertion_worst)
from apps.sort.method.quicksort import (quicksort_iterative,
                                        quicksort_iterative_average,
                                        quicksort_iterative_best,
                                        quicksort_iterative_worst,
                                        quicksort_space_complexity)


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
        keys, array = generate_array(20)
        if sort_type == "":
            array = array.tolist()
            await self.sendit(sort_type, array, keys, None, None, None, None, None)
        elif sort_type == "bubble":
            ensure_future(self.looper(
                text_data_json,
                sort_type,
                keys,
                bubble_sort,
                bubble_sort_best,
                bubble_sort_worst,
                bubble_sort_average,
                bubble_space_complexity
            ))
        elif sort_type == "quicksort":
            ensure_future(self.looper(
                text_data_json,
                sort_type,
                keys,
                quicksort_iterative,
                quicksort_iterative_best,
                quicksort_iterative_worst,
                quicksort_iterative_average,
                quicksort_space_complexity
            ))
        elif sort_type == "counting":
            ensure_future(self.looper(
                text_data_json,
                sort_type,
                keys,
                counting_sort,
                counting_iterative_best,
                counting_iterative_worst,
                counting_iterative_average,
                counting_space_complexity
            ))
        elif sort_type == "insertion":
            ensure_future(self.looper(
                text_data_json,
                sort_type,
                keys,
                insertion_sort,
                insertion_best,
                insertion_worst,
                insertion_average,
                insertion_space_complexity
            ))
        elif sort_type == "heapsort":
            ensure_future(self.looper(
                text_data_json,
                sort_type,
                keys,
                heap_sort,
                heapsort_iterative_best,
                heapsort_iterative_worst,
                heapsort_iterative_average,
                heapsort_space_complexity
            ))
        else:
            array = text_data_json["array"]
            await self.sendit(sort_type, array, keys, None, None, None, None, None)


    async def looper(
            self,
            text_data_json,
            sort_type,
            keys: list,
            sort_function,
            best,
            worst,
            average,
            space
    ):
        array, old_array = text_data_json["array"], []

        while array != old_array:
            array, old_array = sort_function(array[:]), array
            await self.sendit(
                sort_type,
                array,
                keys,
                best(),
                worst(),
                average(),
                space(),
                array == old_array
            )


    async def sendit(
            self,
            sort_type: str,
            array: list,
            keys: list,
            best: Optional[str],
            worst: Optional[str],
            average: Optional[str],
            space: Optional[str],
            final_step: Optional[bool]
    ):
        await self.channel_layer.group_send(
            self.room_group_name, {
                "type": "chat.message",
                "message": {
                    "sort_type": sort_type,
                    "array": array,
                    "best": best,
                    "worst": worst,
                    "average": average,
                    "space": space,
                    "final_step": final_step,
                    "pic": get_image_data(keys, array),
                }
            }
        )


    # Receive message from room group
    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(
            text_data=json.dumps({
                "sort_type": event["message"]["sort_type"],
                "best": event["message"]['best'],
                "worst": event["message"]['worst'],
                "average": event["message"]['average'],
                "space": event["message"]['space'],
                "final_step": event["message"]['final_step'],
                "array": event["message"]["array"],
                "pic": event["message"]['pic'],
            })
        )
