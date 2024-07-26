from datetime import datetime
from modules.common.db import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    making_time = db.Column(db.String(100), nullable=False)
    serves = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(300), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)
    deleted = db.Column(db.Boolean, default=False)
    deleted_at = db.Column(db.DateTime)

    def to_dict(self, include_timestamps=False):
        data = {
            'id': self.id,
            'title': self.title,
            'making_time': self.making_time,
            'serves': self.serves,
            'ingredients': self.ingredients,
            'cost': self.cost
        }
        
        if include_timestamps:
            data['created_at'] = self.created_at
            data['updated_at'] = self.updated_at
        return data
    
    def validate(self):
        errors = {}

        if self.title is None or not isinstance(self.title, str):
            errors['title'] = 'Title must be a string.'
        
        if self.making_time is None or not isinstance(self.making_time, str):
            errors['making_time'] = 'Making time must be a string.'
        
        if self.serves is None or not isinstance(self.serves, str):
            errors['serves'] = 'Serves must be a string.'
        
        if self.ingredients is None or not isinstance(self.ingredients, str):
            errors['ingredients'] = 'Ingredients must be a string.'
        
        if self.cost is None or not isinstance(self.cost, int):
            errors['cost'] = 'Cost must be an integer.'
        
        if errors:
            raise ValueError(errors)

    def save(self):
        self.validate()
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        updateable_fields = ["title", "making_time", "serves", "ingredients", "cost"]
        for field in updateable_fields:
            if field in data:
                setattr(self, field, data[field])
        self.validate()
        db.session.commit()

    def delete(self):
        setattr(self, "deleted", True)
        setattr(self, "deleted_at", datetime.now)
        # db.session.delete(self)
        db.session.commit()

