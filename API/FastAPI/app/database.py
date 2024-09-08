from dotenv import load_dotenv
from peewee import *

import os

load_dotenv()

database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    passwd=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")), 
)

class UserModel(Model):
    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=50)
    password = CharField(max_length=50) 

    class Meta:
        database = database
        table_name = "users"

class OrderModel(Model):
    id = AutoField(primary_key=True)
    customer_name = CharField(max_length=100)
    product_id = IntegerField()  
    quantity = IntegerField()
    order_date = DateTimeField()

    class Meta:
        database = database
        table_name = "orders"

class PetModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    species = CharField(max_length=50)
    age = IntegerField()
    owner_name = CharField(max_length=100)

    class Meta:
        database = database
        table_name = "pets"

class ProductModel(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=100)
    description = TextField()
    price = FloatField()
    stock = IntegerField()

    class Meta:
        database = database
        table_name = "products"

class VehicleModel(Model):
    id = AutoField(primary_key=True)
    make = CharField(max_length=50)
    model = CharField(max_length=50)
    year = IntegerField()
    color = CharField(max_length=50)

    class Meta:
        database = database
        table_name = "vehicles"
