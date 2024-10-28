from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = {}  # Словник для зберігання елементів

class Item(Resource):
    def get(self, name):
        item = items.get(name)
        if item:
            return item, 200
        return {"message": "Item not found"}, 404

    def post(self, name):
        data = request.get_json()
        item = {"name": name, "price": data["price"]}
        items[name] = item
        return item, 201

# Додаємо ресурс до API
api.add_resource(Item, '/item/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)
