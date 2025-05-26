# sandbox.py
from lib.models.articles import Article
from lib.models.author import Author
from lib.models.magazine import Magazine

articles = Article.find_by_author_id(1)
new_magazine = Magazine.create("Car and Tell", "Technology")

print(new_magazine)
