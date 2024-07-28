from app import db
from sqlalchemy import func

class Response(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, default=lambda: int(func.random() * 1000000), nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'question_id': self.question_id,
            'user_id': self.user_id,
            'user_name': self.user_name,
            'text': self.text
        }