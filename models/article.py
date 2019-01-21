from . import Model
import time
from utils import local_time


class Article(Model):
    def __init__(self, form):
        self.id = None
        self.content = form.get('content', '')
        self.title = form.get('title', '')
        self.creat_time = int(time.time())
        self.upgrade_time = self.creat_time
        self.categorie = form.get('categorie', '')
        self.tags = form.get('tags', '').split(' ')

    def local_time(self):
        format = '%Y-%m-%d'
        value = time.localtime(self.upgrade_time)
        dt = time.strftime(format, value)
        return dt

    def time_y_m_d(self):
        return self.local_time().split('-')

    @classmethod
    def years_mouths_dates_find_all(cls, **kwargs):
        arts = cls.find_all(**kwargs)
        ys = set()
        ms = set()
        ds = set()
        for art in arts:
            y_m_d = art.time_y_m_d()
            ys.add(y_m_d[0])
            ms.add(y_m_d[1])
            ds.add(y_m_d[2])
        return ys, ms, ds

    @classmethod
    def years_mouths_dates(cls, arts):
        ys = set()
        ms = set()
        ds = set()
        for art in arts:
            y_m_d = art.time_y_m_d()
            ys.add(y_m_d[0])
            ms.add(y_m_d[1])
            ds.add(y_m_d[2])
        return ys, ms, ds

    @classmethod
    def years_mouths_dates_all(cls):
        arts = cls.all()
        ys = set()
        ms = set()
        ds = set()
        for art in arts:
            y_m_d = art.time_y_m_d()
            ys.add(y_m_d[0])
            ms.add(y_m_d[1])
            ds.add(y_m_d[2])
        return ys, ms, ds

    def get_comments(self):
        from .comment import Comment
        comments = Comment.find_all(article_id=self.id)
        return comments

