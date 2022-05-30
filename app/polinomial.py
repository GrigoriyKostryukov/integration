import matplotlib.pyplot as plt
import numpy as np
import math

from app.graph_drawer import plot_graph


def create_table(f, n, h, start):
    table = []
    table.append([])
    for x in range(-(n // 2) + 1, n // 2 + 1):
        table[0].append(
            f(start + x * h)
        )
    for column in range(1, n):
        table.append([])
        for i in range(
            len(table[column - 1]) - 1
        ):
            table[column].append(
                table[column - 1][i + 1] - table[column - 1][i]
            )
    return table


def create_polynomial(f, n, start, end):
    h = (end - start) / (n-1)
    x0 =  h*(n//2 - 1)
    table = create_table(f, n, h, x0)
    coefs = [column[(len(column) + 1) // 2 - 1] for column in table]

    def polynomial(x):
        t = (x - x0) / h
        result = coefs[0]
        coef = 1
        for i in range(1, len(coefs)):
            coef *= (t + (i // 2 * ((-1) ** (i + 1))))/i
            result = result + (coefs[i] * coef)
        return result
    return polynomial


def diff(f):
    def inner(x):
        h = 1e-10
        return (f(x+h)-f(x))/h
    return inner


def create_r(f, g):
    def inner(x):
        return f(x)-g(x)
    return inner


def create_interpolated_function(alpha, beta, gamma):
    def f(x):
        return alpha * np.sin(np.tan(beta*x))*np.sin(gamma*x)
    return f


def create_functions(form):
    alpha, beta, gamma = form.alpha.data, form.beta.data, form.gamma.data
    minX, maxX, minY, maxY = form.A.data, form.B.data, form.C.data, form.D.data
    segments_nimber = form.nodes_number.data * 2 + 2

    function = create_interpolated_function(alpha, beta, gamma)
    pol = create_polynomial(function, segments_nimber, minX, maxX)
    r = create_r(function, pol)
    df = diff(function)
    dp = diff(pol)
    functions_to_plot = {}
    if form.f.data:
        functions_to_plot['f(x)'] = function
    if form.Pn.data:
        functions_to_plot['Pn(x)'] = pol
    if form.df.data:
        functions_to_plot['df(x)'] = df
    if form.dPn.data:
        functions_to_plot['dPn(x)'] = dp
    if form.rn.data:
        functions_to_plot['rn(x)'] = r
    graph = plot_graph(minX, maxX, minY, maxY, functions_to_plot)
    return graph
