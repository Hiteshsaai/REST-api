from db import db

class UserModel(db.Model):
    ___tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password): # the id is not mentioned here as id is a primary key and it is auto generated
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()
        #
        # connection = sqlite3.connect('data.db')
        #
        # cursor = connection.cursor()
        #
        # select_table = "SELECT * FROM users WHERE username = ?"
        # result = cursor.execute(select_table, (username,))
        # row = result.fetchone()
        #
        # if row:
        #     user = cls(row[0], row[1], row[2]) # OR (*row) <-- this also works
        # else:
        #     user = None
        #
        # connection.close()
        # return user

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()
        # connection = sqlite3.connect('data.db')
        #
        # cursor = connection.cursor()
        #
        # select_table = "SELECT * FROM users WHERE id = ?"
        # result = cursor.execute(select_table, (_id,))
        # row = result.fetchone()
        #
        # if row:
        #     user = cls(row[0], row[1], row[2]) # OR (*row) <-- this also works
        # else:
        #     user = None
        #
        # connection.close()
        # return user
