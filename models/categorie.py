from models import Model


class Categorie(Model):
    def __init__(self, form):
        self.id = form.get('id', None)
        self.name = form.get('name', '')
        self.nums = form.get('nums', 0)

    def get_nums(self):
        pass