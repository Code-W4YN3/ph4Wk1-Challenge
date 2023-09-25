#!/usr/bin/env python3

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'

    serialize_rules = ('-pizzas.restaurants',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    address = db.Column(db.String)

    pizzas = db.relationship(
        "Pizza", secondary = "restaurant_pizzas" , back_populates = "restaurants"    
    )

    @validates('name')
    def validates_name(self, key, name):
        if(len(name) >= 50):
            raise ValueError("Restaurant name cannot exceed 50 characters")
        else:
            return name
    
    def __repr__(self):
        return f'<Restaurant {self.name}>'
    

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    restaurants = db.relationship(
        "Restaurant", secondary = "restaurant_pizzas" , back_populates="pizzas"
    ) 

    def __repr__(self):
        return f'<Pizza {self.name}>'
    

class Restaurant_pizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    pizza_id =  db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant_id =  db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('price')
    def validates_price(self, key, price):
        if not(price >= 1 and price <=30):
            raise ValueError("Price can only range from 1 to 30")
        return price