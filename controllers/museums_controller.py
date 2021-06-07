from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.museum import Museum
import repositories.museum_repository as museum_repository

museums_blueprint = Blueprint("museums", __name__)

# INDEX
# GET '/museums
@museums_blueprint.route("/museums")
def get_museums():
    museums = museum_repository.select_all()
    return render_template("museums/index.html", museums=museums)


# NEW
# GET '/museums/new'
@museums_blueprint.route("/museums/new")
def new_museum():
    return render_template("museums/new.html", museum=Museum("",""), post_to="/museums")


# CREATE
# POST '/museums'
@museums_blueprint.route("/museums", methods=["POST"])
def post_new_museum():
    new_museum = Museum(request.form['name'], request.form['address'])
    museum_repository.save(new_museum)
    return redirect("/museums")

# SHOW
# GET '/museums/<id>'
@museums_blueprint.route("/museums/<id>")
def show_museum(id):
    museum = museum_repository.select(id)
    return render_template("museums/show.html", museum=museum)

# EDIT
# GET '/museums/<id>/edit'
@museums_blueprint.route("/museums/<id>/edit")
def edit_museum(id):
    museum = museum_repository.select(id)
    return render_template("museums/new.html", museum=museum, post_to=f"/museums/{museum.id}")

# UPDATE
# PUT '/museums/<id>'
@museums_blueprint.route("/museums/<id>", methods=["POST"])
def update_museum(id):
    museum = Museum(request.form['name'], request.form['address'], id)
    museum_repository.update(museum)
    return redirect("/museums")


# DELETE
# DELETE '/museums/<id>'
@museums_blueprint.route("/museums/<id>/delete", methods=["POST"])
def delete_museum(id):
    museum_repository.delete(id)
    return redirect("/museums")
