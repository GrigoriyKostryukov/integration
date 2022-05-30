from app import app
from app.forms import ParamsForm

from flask import redirect, render_template, url_for, request

from app.polinomial import create_functions

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = ParamsForm()
    graph = None
    if request.method == "POST":
        graph = create_functions(form)
    return render_template('index.html', title='Interpolation', form=form, graph=graph)
