from django.shortcuts import render

from apps.chat.generator import generate_array
from apps.chat.image import get_image_data


def index(request):
    message = ""
    keys, values = generate_array(50, message)

    return render(request, "chat/index.html", {"room_name": "chat", "pyplot": get_image_data(keys, values) })
