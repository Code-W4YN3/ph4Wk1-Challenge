#!/usr/bin/env python3

from app import app
from models import db, Restaurant, Pizza, Restaurant_pizza
import random

with app.app_context():

    Restaurant.query.delete()
    Pizza.query.delete()
    Restaurant_pizza.query.delete()

    debonairs = Restaurant(
        id=1,
        name="Debonairs",
        address="Kilimani",
    )

    pizza_inn = Restaurant(
        id=2,
        name="Pizza Inn",
        address="Lavington",
    )

    dominos = Restaurant(
        id=3,
        name="Dominos",
        address="Karen",
    )

    db.session.add_all([debonairs, pizza_inn, dominos])

    hawaiian = Pizza(
        id=1,
        name="Hawaiian",
        ingredients="Pineapple, Ham, Onions, Cheese",
    )

    bbq_chicken = Pizza(
        id=2,
        name="BBQ Chicken",
        ingredients = "BBQ sauce, Chicken, Cheese, Onions",
    )

    meat_lovers = Pizza(
        id=3,
        name="Meat Lovers",
        ingredients="Hot Sauce, Ham, Bacon, Sausage, Cheese", 
    )

    cheese_steak = Pizza(
        id=4,
        name="Cheese Steak",
        ingredients="Roast beef, Mushrooms, Green bell pepper, Cheese"
    )

    veggie = Pizza(
        id=5,
        name="Veggie Pizza",
        ingredients="Zucchini, Bell peppers, Tomatoes, Cheese",
    )

    db.session.add_all([hawaiian, bbq_chicken, meat_lovers, cheese_steak, veggie])
    
    one = Restaurant_pizza(
        id=1,
        pizza_id=1,
        restaurant_id=1,
        price=random.randint(1,30),
    )

    two = Restaurant_pizza(
        id=2,
        pizza_id=3,
        restaurant_id=1,
        price=random.randint(1,30),
    )

    three = Restaurant_pizza(
        id=3,
        pizza_id=5,
        restaurant_id=1,
        price=random.randint(1,30),
    )

    four = Restaurant_pizza(
        id=4,
        pizza_id=2,
        restaurant_id=2,
        price=random.randint(1,30),
    )

    five = Restaurant_pizza(
        id=5,
        pizza_id=3,
        restaurant_id=2,
        price=random.randint(1,30),
    )

    six = Restaurant_pizza(
        id=6,
        pizza_id=4,
        restaurant_id=2,
        price=random.randint(1,30),
    )

    seven = Restaurant_pizza(
        id=7,
        pizza_id=2,
        restaurant_id=3,
        price=random.randint(1,30),
    )

    eight = Restaurant_pizza(
        id=8,
        pizza_id=4,
        restaurant_id=3,
        price=random.randint(1,30),
    )

    nine = Restaurant_pizza(
        id=9,
        pizza_id=5,
        restaurant_id=3,
        price=random.randint(1,30),
    )

    ten = Restaurant_pizza(
        id=10,
        pizza_id=2,
        restaurant_id=1,
        price=random.randint(1,30),
    )

    db.session.add_all([one, two, three, four, five, six, seven, eight, nine, ten])

    db.session.commit()