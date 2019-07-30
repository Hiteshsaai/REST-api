from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store  = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'The given store name does not exist'}


    def post(self,name):
        if StoreModel.find_by_name(name):
            return{'message':'The given store name already exist'}

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {'message':'An error occured when adding the store name'}, 500

        return store.json(), 201

    def delete(self,name):
        store = StoreModel.find_by_name(name)

        if store:
            try:
                store.delete_from_db()
            except:
                return {'message':'An error occured while deleting the store name'}, 500

        return {'message':'Given store name deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()] }
