from flask import Flask
import instance.database as DBT

app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = DBT.db_name
