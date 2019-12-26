import sqlite3

from flask_restful import Resource, reqparse

class User:
    def __init__(self, _id, username, password):
        self.username = username
        self.id = _id
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = connection.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])

        else:
            user = None
        connection.close()
        return user
    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = connection.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(row[0], row[1], row[2])
        else:
            user = None
        connection.close()
        return user

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="this field cannot be blank")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="this field cannot be blank")

    def post(self):
        data = UserRegister.parser.parse_args()
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        if User.find_by_username(data['username']):
            return "message : user already exists, try other username", 400
        else:
            insert = "INSERT INTO users VALUES (NULL, ?, ?)"
            value = (data['username'], data['password'])
            cursor.execute(insert, value)
            connection.commit()
            connection.close()
            return "Message: user created successfully ", 201







