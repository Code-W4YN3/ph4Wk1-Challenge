#!/usr/bin/env python3

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    address = db.Column(db.String)

    pizzas = db.relationship('Pizza', secondary='restaurant_pizzas')

    @validates('name')
    def validates_name(self, key, name):
        if(len(name) >= 50):
            raise ValueError("Restaurant name cannot exceed 50 characters")
        return name
    
    def __repr__(self):
        return f'<Restaurant {self.name} | Address: {self.address}>'
    

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurants= db.relationship('Restaurant', secondary='restaurant_pizzas')

    def __repr__(self):
        return f'<Pizza {self.name} | Ingredients: {self.ingredients}>'
    

class Restaurant_pizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    pizza_id =  db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id =  db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    pizza = db.relationship(Pizza, backref=db.backref("restaurant_pizzas", cascade="all, delete-orphan"))
    restaurant = db.relationship(Restaurant, backref=db.backref("restaurant_pizzas", cascade="all, delete-orphan"))

    @validates('price')
    def validates_price(self, key, price):
        if(price not in range(1,31)):
            raise ValueError("Price can only range from 1 to 30")
        return price

    def __repr__(self):
        return f'<Pizza {self.name} | Ingredients: {self.ingredients}>'