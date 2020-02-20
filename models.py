from app import db
from datetime import datetime
from app import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    # image_file = db.Column(db.String(20),nullable =False, default='default.jpg')
    password = db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post',backref= 'author',lazy=True)
    comments = db.relationship('Comment', backref='author', lazy= True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(100),nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default= datetime.utcnow)
    summary = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # image_file = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'), nullable=False)
    upvote = db.Column(db.Integer, nullable=False, default = 0)
    downvote = db.Column(db.Integer, nullable=False, default = 0)
    comments = db.relationship('Comment', backref='post', lazy=True, cascade = "all, delete, delete-orphan")

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


class Comment(db.Model):
    __tablename__ ='comments'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.description}"