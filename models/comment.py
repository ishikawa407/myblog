from models import Model


class Comment(Model):
    def __init__(self, form):
        self.id = None
        self.content = form.get('content', '')
        self.nickname = form.get('nickname', '')
        self.email = form.get('email', '')
        self.article_id = form.get('article_id', '')
