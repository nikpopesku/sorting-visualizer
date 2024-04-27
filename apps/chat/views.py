import time

import environ
from django.shortcuts import render

from apps.chat.generator import generate_array
from apps.chat.image import get_image_data


def index(request):
    keys, values = generate_array(20, "")
    env = environ.Env()
    environ.Env.read_env()

    return render(request, "chat/index.html", {
        "room_name": str(time.time()).replace('.', ''),
        "array": values.tolist(),
        "pyplot": get_image_data(keys, values),
        "homelink": env('URL')
    })
