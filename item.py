import sqlite3
from flask_restful import Resource, reqparse
from flask import request
from flask_jwt import jwt_required


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="this field cannot be blank")

    @jwt_required()
    def get(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        get_item = "SELECT * FROM items WHERE name = ?"
        rows = cursor.execute(get_item, (name,))
        row = rows.fetchone()
        connection.close()
        if row:
            return {"item": {"name": row[0], "price": row[1]}}
        return {"message": "item not found"}, 404

    def post(self, name):

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        insert_query = "INSERT INTO items VALUES(?, ?)"
        data = Item.parser.parse_args()
        cursor.execute(insert_query, (name, data['price']))
        connection.commit()
        connection.close()
        return {'item': {'name': name, 'price': data['price']}}, 201

    def delete(self, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        deleteitem = "DELETE FROM items WHERE name=?"
        cursor.execute(deleteitem, (name,))
        connection.commit()
        connection.close()
        return {"message": "item deleted successfully"}


    @classmethod
    def getbyitem(cls, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        getitem = "SELECT * FROM items WHERE name=?"
        row = cursor.execute(getitem, (name,))
        connection.commit()
        connection.close()
        return row

    def put(self, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        item = Item.getbyitem(name)
        data = Item.parser.parse_args()
        if item:

            query = "UPDATE items SET price=? WHERE name=? "
            values = (data['price'], name)

        else:

            query = "INSERT INTO items VALUES(?, ?) "
            values = (name, data['price'])
            print("fresh value")

        cursor.execute(query, values)
        connection.commit()
        connection.close()
        return {"item": name, "price": data['price']}


class Items(Resource):
    def get(self):
        items = []
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        itemlist = "SELECT * FROM items"
        rows = cursor.execute(itemlist)
        for row in rows:
            items.append({"name": row[0], "price": row[1]})
        return {"items": items}
    