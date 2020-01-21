from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from webscraper import get_cnn, get_fox, get_NYT, get_huff, get_nbc
from flask_cors import CORS

import time
import os

# Init App

app = Flask(__name__)

CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)


@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Hello World'})


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(100))
    title = db.Column(db.String(500))
    url = db.Column(db.String(500))
    number = db.Column(db.Integer)

    def __init__(self, site, title, url, number):
        self.site = site
        self.title = title
        self.url = url
        self.number = number

# Article Schema


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'site', 'title', 'url', 'number')


# Init Schema
article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

# Create an Article


def add_article(obj, organization):
    for article in obj:
        site = article['site']
        title = article['title']
        url = article['url']
        number = article['number']

        current = Article.query.filter(
            Article.number == number, Article.site == organization).first()

        if current:
            current.site = site
            current.title = title
            current.url = url
            current.number = number
            db.session.commit()
        else:
            new_article = Article(site, title, url, number)
            db.session.add(new_article)
            db.session.commit()


@app.route('/article/', methods=['GET'])
def get_articles():
    all_articles = Article.query.all()
    result = articles_schema.dump(all_articles)
    return jsonify(result)


@app.route('/article/<id>', methods=['GET'])
def get_article(id):
    article = Article.query.get(id)
    result = article_schema.dump(article)
    return jsonify(result)


while True:
    cnn_results = get_cnn()
    fox_results = get_fox()
    fox_results = get_NYT()
    huff_results = get_huff()
    nbc_results = get_nbc()

    add_article(cnn_results, 'CNN')
    add_article(fox_results, 'FOX')
    add_article(fox_results, 'NYTimes')
    add_article(huff_results, 'Huffington Post')
    add_article(nbc_results, 'NBC News')

    time.sleep(10800)


# Run Server
if __name__ == '__main__':
    # port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=port)
    app.run(debug=True);

