from email.policy import default
from flask_wtf import FlaskForm
from wtforms import FloatField, RadioField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class ParamsForm(FlaskForm):
    alpha = FloatField('alpha', default=1,  validators=[DataRequired()])
    beta = FloatField('beta', default=1, validators=[DataRequired()])
    gamma = FloatField('gamma', default=1, validators=[DataRequired()])
    lower_limit = FloatField('lower', default=-1, validators=[DataRequired()])
    upper_limit = FloatField('upper', default=1, validators=[DataRequired()])

    A = FloatField('A', default=-1, validators=[DataRequired()])
    B = FloatField('B', default=1, validators=[DataRequired()])
    C = FloatField('C', default=-1, validators=[DataRequired()])
    D = FloatField('D', default=1, validators=[DataRequired()])

    n = IntegerField(default=10, validators=[DataRequired()])
    selected_parameter = RadioField(
        label='Выделенный параметр',
        choices=[('alpha', 'α'), ('beta', 'β'), ('gamma', 'γ')],
        default='alpha',
        validators=[
            DataRequired()
        ])
    precision = RadioField(
        label='Точность',
        choices=[1.0, 0.1, 0.01, 0.001, 0.0001],
        default=0.1,
        validators=[
            DataRequired()
        ])

    submit = SubmitField('Построить график')
