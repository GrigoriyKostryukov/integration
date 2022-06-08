import matplotlib.pyplot as plt
import numpy as np
import math

from app.graph_drawer import plot_graph


def create_function(alpha, beta, gamma):
    def f(x):
        return alpha * np.sin(np.tan(beta*x))*np.sin(gamma*x)
    return f


def In(f, n, lower, upper):
    """Приближёное вычисление интеграла с разбиением на n отрезков"""
    
    step = (upper - lower)/n
    integral_value = 0
    for i in range(1, n+1):
        integral_value += f((lower + i*step) - (step/2))*step
    return integral_value


def integral(f, lower, upper, n, precision):
    """Приближёное вычисление интеграла с указанной точностью"""
    # Приближённое значение интеграла для разбиения на n отрезков
    current_partition = In(f, n, lower, upper)
    # Приближённое значение интеграла для разбиения на 2n отрезков
    double_partition = In(f, 2*n, lower, upper)
    while (1/3)*abs(current_partition - double_partition) > precision:
        n*=2
        current_partition = double_partition
        double_partition = In(f, 2*n, lower, upper)
    return (double_partition, 2*n)



def integrate(form):
    GRAPH_POINTS_NUMBER = 300  # Количество узлов для построения графика

    alpha, beta, gamma = form.alpha.data, form.beta.data, form.gamma.data
    lower_limit, upper_limit = form.lower_limit.data, form.upper_limit.data
    minX, maxX, minY, maxY = form.A.data, form.B.data, form.C.data, form.D.data
    selected_parameter = form.selected_parameter.data
    precision = float(form.precision.data)
    n = form.n.data

    step = (maxX - minX)/(GRAPH_POINTS_NUMBER - 1)
    points = [(minX + i*step) for i in range(GRAPH_POINTS_NUMBER)]
    values = []

    if selected_parameter == 'alpha':

        for point in points:
            f = create_function(point, beta, gamma)
            values.append(integral(f, lower_limit, upper_limit, n, precision))
    elif selected_parameter == 'beta':
        for point in points:
            f = create_function(alpha, point, gamma)
            values.append(integral(f, lower_limit, upper_limit, n, precision))
    else:
        for point in points:
            f = create_function(alpha, beta, point)
            values.append(integral(f, lower_limit, upper_limit, n, precision))

    integral_values = [value[0] for value in values]
    n_max = max([value[1] for value in values])
    graph = plot_graph(minX, maxX, minY, maxY, points, integral_values)

    return graph, n_max
