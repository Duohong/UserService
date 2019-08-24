from pymongo import MongoClient

class Mongo:
    @staticmethod
    def save_new_user(message):
        client = MongoClient("localhost", 27017)
        print("Mongo:", message)


