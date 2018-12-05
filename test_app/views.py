from . import app
from flask import request,flash,redirect,url_for,render_template
from .forms import IngresarForm,SeleccionarPersonaForm
from . import models


@app.route('/',methods=['POST','GET'])
@app.route('/ingresar',methods=['POST','GET'])
def ingresar():
    title = 'Ingresar Persona'
    form = IngresarForm(request.form)
    
    if request.method == 'POST' and form.validate_on_submit():
        nombre = form.nombre.data
        apellido = form.apellido.data
        biografia = form.biografia.data
        models.insert_persona(nombre,apellido,biografia)
        flash(f'La persona {nombre} {apellido} ha sido registrada')
        return redirect(url_for('ingresar'))
    else:
        return render_template('ingresar.html',title=title,form=form)
    


@app.route('/editar',methods=['POST','GET'])
@app.route('/editar/<pk>',methods=['POST','GET'])
@app.route('/editar/<pk>/<confirm>',methods=['POST','GET'])
def editar(pk=None,confirm=None):
    title = 'Ingresar Persona'
    if pk:
        form = IngresarForm(request.form)
        if request.method == 'GET' and not confirm:
            data = models.get_persona_data(id_persona=int(pk))
            form.nombre.data = data[0][0]
            form.apellido.data = data[0][1]
            form.biografia.data = data[0][2]
            return render_template('editar.html',title=title,form=form,id_editar=pk)
        elif request.method == 'POST' and form.validate_on_submit():
            nombre = form.nombre.data
            apellido = form.apellido.data
            biografia = form.biografia.data
            models.edit_persona(int(pk),nombre,apellido,biografia)
            flash(f'La persona {nombre} {apellido} ha sido editada')
            return redirect(url_for('editar'))
    else:

        form = SeleccionarPersonaForm(request.form)
        form.lista.choices = [(str(id),str(full_name)) for id,full_name in models.get_persona_data()]
        if request.method == 'POST' and form.lista.data:
            id_persona = form.lista.data
            return redirect(url_for('editar',pk=id_persona))
        else:
            return render_template('editar.html',title=title,form=form)
    

                

@app.route('/eliminar',methods=['POST','GET'])
def eliminar():
    title = 'Eliminar Persona'
    form = SeleccionarPersonaForm(request.form)
    form.lista.choices = [(str(id),str(full_name)) for id,full_name in models.get_persona_data()]
    if request.method == 'POST' and form.lista.data:
        id_persona = form.lista.data
        persona_info = dict(form.lista.choices).get(form.lista.data)
        models.delete_persona(int(id_persona))
        flash(f'La persona {persona_info} ha sido eliminada')
        return redirect(url_for('eliminar'))
    else:
        return render_template('eliminar.html',title=title,form=form)
