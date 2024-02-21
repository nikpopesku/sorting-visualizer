from io import StringIO

import matplotlib.pyplot as plt
from django.shortcuts import render


def index(request):
    x = [1, 2, 3, 4]
    y = [3, 4, 10, 5]

    fig = plt.figure()
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    return render(request, "chat/index.html", {"room_name": "chat", "plt": imgdata.getvalue() })
