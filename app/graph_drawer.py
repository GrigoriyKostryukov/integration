import base64
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np


def plot_graph(start, end, bottom, top, points, integral_values):

    x = np.linspace(start - 0.1, end + 0.1, 5000)

    fig, ax = plt.subplots()
    ax = plt.gca()
    ax.set_ylim([bottom, top])
    plt.plot(points, integral_values, 'r')

    plt.rcParams['figure.figsize'] = [15, 8]
    image = create_image()
    return image


def create_image():
    '''Converts plotted figure into a png image'''
    image = BytesIO()
    plt.savefig(image, format='png')
    plt.close()
    image.seek(0)
    plot = base64.b64encode(image.getvalue()).decode('utf8')
    return plot
