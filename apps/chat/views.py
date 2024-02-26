from io import StringIO

import matplotlib.pyplot as plt
from django.shortcuts import render

from apps.chat.generator import generate_array


def index(request):
    keys, values = generate_array(50)

    fig = plt.figure()
    plt.plot(keys,values)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    return render(request, "chat/index.html", {"room_name": "chat", "plt": imgdata.getvalue() })
