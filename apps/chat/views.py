from io import StringIO

import matplotlib.pyplot as plt
import numpy as np
from django.shortcuts import render


def index(request):
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')

    x = np.arange(0,np.pi*3,.1)
    y = np.sin(x)

    fig = plt.figure()
    plt.plot(x,y)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    return render(request, "chat/index.html", {"room_name": "chat", "plt": imgdata.getvalue() })
