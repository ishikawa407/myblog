from flask import Blueprint, request, render_template, url_for, redirect, abort

from models.article import Article
from models.comment import Comment
main = Blueprint('article', __name__)


@main.route('/<int:id>')
def article_detail(id):
    a = Article.find(id)
    if a is None:
        abort(404)
    return render_template('article.html', article=a)


@main.route('/add-comment', methods=['POST'])
def add_comment():
    form = request.form
    c = Comment(form)
    article_id = request.args.get('id')
    c.article_id = int(article_id)
    c.save()
    return redirect(url_for('article.article_detail', id=article_id))
