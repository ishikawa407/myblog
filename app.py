from flask import Flask
import config

app = Flask(__name__)
app.secret_key = config.secret_key

from routes.index import main as index_routes
from routes.admin import main as admin_routes
from routes.article import main as article_routes
from routes.categorie import main as categorie_routes


app.register_blueprint(index_routes)
app.register_blueprint(admin_routes, url_prefix='/admin')
app.register_blueprint(article_routes, url_prefix='/article')
app.register_blueprint(categorie_routes, url_prefix='/categorie')
#haha
if __name__ == '__main__':

    app.run(debug=True)
