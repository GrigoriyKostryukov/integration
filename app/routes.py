from app import app
from app.forms import ParamsForm

from flask import redirect, render_template, url_for, request

from app.integration import integrate

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ParamsForm()
    graph = None
    n_max = None
    if request.method == "POST":
        graph, n_max = integrate(form)
    return render_template('index.html', title='Interpolation', form=form, graph=graph, n_max = n_max)
