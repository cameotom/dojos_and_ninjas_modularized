from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo


@app.route('/dojos')
def dojos():
    # call the get all classmethod to get all users
    dojos = Dojo.get_all()
    for i in dojos:
        print(i.name)
    return render_template("dojos.html", dojos=dojos)

@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojo/create', methods=["POST"])
def create_dojo():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name": request.form["name"]
    }
    # We pass the data dictionary into the save method from the user class.
    Dojo.create_dojo(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo_ninjas(id):
    data = {
        "id": id
    }
    dojo_ninjas = Dojo.get_dojo_with_ninjas(data)
    return render_template("single_dojo_ninjas.html", dojo = dojo_ninjas)


@app.route('/dojo/edit/<int:id>')
def dojo_edit(id):
    data = {
        "id": id
    }
    return render_template("edit_dojo.html", dojo=Dojo.get_one(data))


@app.route('/dojo/update', methods=['POST'])
def update():
    Dojo.update(request.form)
    return redirect('/dojos')


@app.route('/dojo/delete/<int:id>')
def delete_dojo(id):
    print("am i working")
    data = {
        "id": id
    }
    Dojo.delete(data)
    return redirect('/dojos')


