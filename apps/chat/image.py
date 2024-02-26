from io import StringIO

import matplotlib.pyplot as plt


def get_image_data(keys, values):
    fig = plt.figure()
    plt.stem(keys, values)

    imgdata = StringIO()
    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    return imgdata.getvalue()
