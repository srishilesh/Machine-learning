import NLP_Astro
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class sumNumbers(Resource):
    def get(self, first):
        #message_text=input("Enter a string")
        return {'data': NLP_Astro.NLP(first)}

api.add_resource(sumNumbers, '/NLP/<first>')

if __name__ == '__main__':
     app.run()
     