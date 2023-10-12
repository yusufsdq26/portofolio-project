from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/contact", methods=["POST"])
def contact_post():
    email_receive = request.form["email_give"]
    contact_receive = request.form["contact_give"]
    count = db.portofolio.count_documents({})
    num = count + 1
    doc = {
        'num':num,
        'email': email_receive,
        'contact': contact_receive,
        'done': 0
    }
    db.portofolio.insert_one(doc)
    return jsonify({'msg':'data saved!'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)