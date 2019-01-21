from flask import Blueprint, request, render_template, redirect, url_for
from models.article import Article
from models.categorie import Categorie
main = Blueprint('admin', __name__)


@main.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'GET':
        return render_template('admin/new.html')
    if request.method == 'POST':
        form = request.form
        a = Article(form)
        a.save()
        return redirect(url_for('index.index'))


@main.route('/add-categorie', methods=['GET', 'POST'])
def add_categorie():
    if request.method == 'POST':
        form = request.form
        name = form.get('name')
        if Categorie.find_by(name=name):
            return redirect(url_for('admin.add_categorie'))
        nc = Categorie(form)
        nc.save()
        return redirect(url_for('index.index'))
    return render_template('admin/new_categorie.html')