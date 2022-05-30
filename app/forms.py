from email.policy import default
from flask_wtf import FlaskForm
from wtforms import FloatField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class ParamsForm(FlaskForm):
    alpha = FloatField('a', default=1,  validators=[DataRequired()])
    beta = FloatField('b', default=1, validators=[DataRequired()])
    gamma = FloatField('y', default=1, validators=[DataRequired()])

    A=FloatField('y', default=-1, validators=[DataRequired()])
    B=FloatField('y', default=1, validators=[DataRequired()])
    C=FloatField('y', default=-1, validators=[DataRequired()])
    D=FloatField('y', default=1, validators=[DataRequired()])

    nodes_number=IntegerField(default=1,validators=[DataRequired()])

    f=BooleanField('y', validators=[DataRequired()])
    Pn=BooleanField('y', validators=[DataRequired()])
    df=BooleanField('y', validators=[DataRequired()])
    dPn=BooleanField('y', validators=[DataRequired()])
    rn=BooleanField('y', validators=[DataRequired()])
    submit = SubmitField('Построить график')


