from .db import db
from datetime import datetime
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Document):
    name = db.StringField(max_length=50, required=True)
    username= db.StringField(min_length=2, max_length=50, required=True, unique=True)
    email = db.StringField(max_length=50, required=True, unique=True)
    image =db.ImageField(required=False)
    porject = db.StringField(max_length=50, required=True)
    password = db.StringField(min_length=8 ,max_length=100 ,required=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)



class Comment(db.EmbeddedDocument):
    content = db.StringField(required=True, unique=False)
    comment_posted = db.DateTimeField(default=datetime.utcnow)
    added_by = db.ReferenceField('User')



class Vote(db.EmbeddedDocument):
    user_id = db.IntField(nullable=True)
    post_id = db.IntField( nullable=True)


class Post(db.Document):
    title = db.StringField(max_length=120, required=True, unique=False)
    content = db.StringField(required=True, unique=False)
    portfolio = db.StringField(max_length=50, required=True, unique=False)
    post_posted = db.DateTimeField(default=datetime.now, required=True)
    like = db.IntField( nullable=True,default=0)
    author = db.ReferenceField('User')
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))
    vote = db.ListField(db.EmbeddedDocumentField('Vote'))


User.register_delete_rule(Post, 'author', db.CASCADE)