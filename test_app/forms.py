from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,SubmitField
from wtforms.validators import DataRequired,Length
from . import models

class IngresarForm(FlaskForm):
    nombre = StringField('Nombre : ',validators=(DataRequired(),Length(max=255)))
    apellido = StringField('Apellido : ',validators=(DataRequired(),Length(max=255)))
    biografia = StringField('Biografia : ',validators=(Length(max=255),))
    submit = SubmitField('Aceptar')
    
    
class SeleccionarPersonaForm(FlaskForm):
    lista = SelectField('Selecciona una persona: ',
    validators=(DataRequired(),),
    choices= [ ] )
    submit = SubmitField('Confirmar')

