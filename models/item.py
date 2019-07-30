from db import db

class ItemModel(db.Model):
    ___tablename__ = 'items'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision = 2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        #
        # check_table = "SELECT * FROM items WHERE name = ?"
        #
        # result = cursor.execute(check_table, (name,))
        #
        # row = result.fetchone()
        # connection.close()
        #
        # if row:
        #     return cls(row[0],row[1]) # *row can also be used
        # return None
    def save_to_db(self): # db.session.add can do both insert and update
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):  # db.session.add can do both insert and update, so here it is being used for delete
        db.session.delete(self)
        db.session.commit()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor
        #
        # query = "UPDATE items SET price = ? WHERE name = ?"
        # cursor.execute(query, (self.price, self.name))
        #
        # connection.commit()
        # connection.close()
