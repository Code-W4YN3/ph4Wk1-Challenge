#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Restaurant, Pizza, Restaurant_pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

@app.route('/')
def index():
    return '<h1>Restaurants API</h1> \n \n <h2>Endpoints: </h2> \n <p>All restaurants: /restaurants</p> \n <p>Restaurant by ID: /restaurants/[id]</p> \n <p>All pizzas: /pizzas</p> \n <p>Restaurant-pizzas: /restaurant_pizzas</p>'

class Restaurants(Resource):

    def get(self):
        restaurants = [rest.to_dict() for rest in Restaurant.query.all()]
        return make_response(jsonify(restaurants), 200)

api.add_resource(Restaurants, '/restaurants')

class RestaurantsID(Resource):

    def get(self, id):
        restaurantsID = [Restaurant.query.filter_by(id = id).first().to_dict()]
        return make_response(jsonify(restaurantsID), 200)
    
    def delete(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        restaurant_pizzas = Restaurant_pizza.query.filter_by(restaurant_id = id).all()

        db.session.delete(restaurant_pizzas)
        db.session.delete(restaurant)
        db.session.commit()

        response = make_response(
            " ",
            200
        )

        return response

api.add_resource(RestaurantsID, '/restaurants/<int:id>')

class Pizzas(Resource):

    def get(self):
        pizzas = [pizza.to_dict() for pizza in Pizza.query.all()]
        return make_response(jsonify(pizzas), 200)
    
api.add_resource(Pizzas, '/pizzas')

class Restaurant_pizzas(Resource):

    def get(self):
        rest_pizzas = [rest_pizza.to_dict() for rest_pizza in Restaurant_pizza.query.all()]
        return make_response(jsonify(rest_pizzas), 200)
    
    def post(self):
        
        new_rest_pizza = Restaurant_pizza(
            price = request.form['name'],
            pizza_id = request.form['pizza_id'],
            restaurant_id = request.form['restaurant_id'],
        )

        db.session.add(new_rest_pizza)
        db.session.commit()

        return make_response(new_rest_pizza.to_dict(), 201)

api.add_resource(Restaurant_pizzas, '/restaurant_pizzas')


if __name__ == '__main__':
    app.run(port=5555, debug=True)