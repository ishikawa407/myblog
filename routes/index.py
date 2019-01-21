from flask import (Blueprint,
                   redirect,
                   render_template
                   )
from models.article import Article
main = Blueprint('index', __name__)


@main.route('/')
def index():
    articles = Article.all()
    return render_template('index.html', articles=articles)


@main.route('/archives')
def articles_list():
    articles = Article.all()
    ys = Article.years_mouths_dates_all()[0]

    return render_template('archives.html', articles=articles, ys=ys)


@main.route('/about')
def about():
    return render_template('about.html')
