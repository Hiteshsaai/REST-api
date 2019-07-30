from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store_id."
                        )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404


    def post(self,name):

        if ItemModel.find_by_name(name):
            return {'message': 'The item already exist'}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, data['price'], data['store_id']) #using the ItemModel __init__ method

        try:
            item.save_to_db() # inserting using __init__ values (check for item in package models)
        except:
            return {'message':'An error occured while inserting the item'}, 500 #internal server error

        return item.json(), 201

    def delete(self,name):
        # global items

        item = ItemModel.find_by_name(name)

        if item:
            item.delete_from_db()
            return {'message': 'Item deleted.'}
        return {'message':'The item {} is not found'.format(name)}
        #     connection = sqlite3.connect("data.db")
        #     cursor = connection.cursor()
        #
        #     query = "DELETE FROM items WHERE name =?"
        #
        #     cursor.execute(query, (name,))
        #
        #     connection.commit()
        #     connection.close()
        #
        #     return {'message': 'The item {} has been successfully deleted'.format(name)}
        #
        # return {'message': 'Mentioned item does not exist in the database'}

        # items = list(filter(lambda x: x['name'] != name, items))
        # return {"message":"Item {} deleted".format(name)}

    def put(self, name):

        data = Item.parser.parse_args()
        item = Item.find_by_name(name) # to check for existing item
        # updated_item = ItemModel(name , data['price']) # to update with new item

        if item is None:
            item = ItemModel(name, data['price'], data['store_id'])
            # try:
            #     udpated_item.insert()
            # except:
            #     return {'message': "Error occured while inserting the row"}, 500
        else:
            item.price = data['price']
            # try:
            #     update_item.update()
            # except:
            #     return {'message':'Error occured while updating the row'}, 500
        item.save_to_db()

        return item.json()


class ItemList(Resource):
    # TABLE_NAME = "items"

    def get(self):
        return {'item':[ item.json() for item in ItemModel.query.all()]}

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items" #.format(table=self.TABLE_NAME)
        # result = cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'name': row[0], 'price': row[1]})
        # connection.close()
        #
        # return {'items': items}
