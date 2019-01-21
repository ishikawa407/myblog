from flask import Blueprint, render_template, url_for, request, redirect
from models.categorie import Categorie
from models.article import Article
main = Blueprint('categorie', __name__)


@main.route('/tech')
def tech():
    arts = Article.find_all(categorie='技术')
    ys = Article.years_mouths_dates(arts)[0]
    return render_template('archives.html', articles=arts, ys=ys)


@main.route('/lang')
def lang():
    arts = Article.find_all(categorie='语学')
    ys = Article.years_mouths_dates(arts)[0]
    return render_template('archives.html', articles=arts, ys=ys)


@main.route('/leisure')
def leisure():
    arts = Article.find_all(categorie='闲聊')
    ys = Article.years_mouths_dates(arts)[0]
    return render_template('archives.html', articles=arts, ys=ys)