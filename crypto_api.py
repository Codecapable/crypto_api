from flask import Flask, jsonify, request
import requests
from flask_restful import Resource, Api



app = Flask(__name__)
app.secret_key = 'mustapha'
api = Api(app)

class Crypto(Resource):

    def get(self):
        url = 'https://min-api.cryptocompare.com/data/top/totalvolfull?limit=10&tsym=USD'
        page = requests.get(url)
        list = page.json()['Data']
        data = [coin["CoinInfo"]['Name'] for coin in list],[coin["RAW"]['USD']['TOTALVOLUME24HTO'] for coin in list]
        
        return jsonify(data)
    
        

api.add_resource(Crypto,'/top_10_coins')


app.run(port=5000,debug=True)