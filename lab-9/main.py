#!../venv/bin/python3.7
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://18.224.251.216:27017,3.15.170.128:27017,18.188.77.96:27017/?replicaSet=rs0')  # host uri

print(client)
db = client['chat']  # Select the database
collection = db['messages']

def get_data():
    data = collection.find({}, {'_id': 0})
    return data

@app.route('/')
def session():
    return render_template('session.html', data=get_data())

@app.route('/', methods=['POST'])
def add_message():
    collection.insert_one({"author": request.form['username'], "message": request.form['message']})
    return render_template('session.html', data=get_data())

if __name__ == '__main__':
    app.run(debug=True)