import psycopg2
from app import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    last_modified_date = db.Column(db.DateTime, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text(), nullable=False)

    # 
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_modified_date': self.last_modified_date,
            'created_date': self.created_date,
            'text': self.text
        }

    def __init__(self, name, last_modified_date, created_date, text):
        self.name = name
        self.last_modified_date = last_modified_date
        self.created_date = created_date
        self.text = text



db.create_all()