from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/ninja/add')
def add_ninja():
    dojos = Dojo.get_all()
    for i in dojos:
        print(i.name)
    return render_template("add_ninja.html", dojos = dojos)

@app.route('/ninja/create', methods=["POST"])
def create_ninja():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    # We pass the data dictionary into the save method from the user class.
    Ninja.create_ninja(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dojos')

@app.route('/ninja/edit/<int:id>')
def edit_ninja(id):
    data = {
        "id": id
    }
    return render_template("edit_ninja.html", ninja=Ninja.get_one(data))


@app.route('/ninja/update', methods=['POST'])
def update_ninja():
    print("A")
    print(request.form)
    print("B")
    print(Ninja)
    dojo_id = request.form["dojo_id"]
    Ninja.update(request.form)
    return redirect(f"/dojo/{dojo_id}")


@app.route('/ninja/delete/<int:id>')
def delete_ninja(id):
    data = {
        "id": id
    }
    Ninja.delete(data)
    return redirect('/dojos')