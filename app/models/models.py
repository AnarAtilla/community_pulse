from app import db
from sqlalchemy import func

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('questions', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'category_id': self.category_id,
            'category_name': self.category.name if self.category else None
        }

    def update(self, data):
        for key, value in data.items():
            if key == 'category_name':
                category = Category.query.filter_by(name=value).first()
                if not category:
                    category = Category(name=value)
                    db.session.add(category)
                    db.session.commit()
                self.category_id = category.id
            else:
                setattr(self, key, value)

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    user_id = db.Column(db.Integer, default=lambda: int(func.random() * 1000000), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    question = db.relationship('Question', backref=db.backref('responses', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'question_id': self.question_id,
            'user_id': self.user_id,
            'user_name': self.user_name,
            'text': self.text
        }