from controllers.museums_controller import new_museum
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.museum import Museum
from models.work import Work
import repositories.museum_repository as museum_repository
import repositories.work_repository as work_repository

works_blueprint = Blueprint("works", __name__)

# INDEX
# GET '/works
@works_blueprint.route('/works')
def get_works():
    works = work_repository.select_all()
    return render_template("works/index.html", works=works)

# NEW
# GET '/works/new'
@works_blueprint.route('/works/new')
def new_work():
    museums = museum_repository.select_all()
    work = Work("","","",None)
    return render_template('works/new.html', museums=museums, work=work, post_to="/works")

# CREATE
# POST '/works'
@works_blueprint.route('/works', methods=["POST"])
def post_work():
    form = request.form
    museum_id = int(form['museum_id'])
    museum = museum_repository.select(museum_id)
    title = form['title']
    artist = form['artist']
    year = int(form['year'])
    new_work = Work(title, artist, year, museum)
    work_repository.save(new_work)
    return redirect("/works")


# SHOW
# GET '/works/<id>'
@works_blueprint.route("/works/<id>")
def show_work(id):
    work = work_repository.select(id)
    return render_template("works/show.html", work=work)

# EDIT
# GET '/works/<id>/edit'
@works_blueprint.route("/works/<id>/edit")
def edit_work(id):
    work = work_repository.select(id)
    museums = museum_repository.select_all()
    print(vars(work))
    return render_template("works/new.html", work=work, museums=museums, post_to=f"/works/{work.id}")


# UPDATE
# PUT '/works/<id>'
@works_blueprint.route("/works/<id>", methods=["POST"])
def update_work(id):
    museum = museum_repository.select(request.form["museum_id"])
    work = Work(request.form['title'], request.form['artist'], request.form['year'], museum, id)
    work_repository.update(work)
    return redirect("/works")

# DELETE
# DELETE '/works/<id>'
@works_blueprint.route("/works/<id>/delete", methods=["POST"])
def delete_work(id):
    work_repository.delete(id)
    return redirect("/works")
