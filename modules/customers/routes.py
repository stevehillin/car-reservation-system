import os
import json
from flask import request, jsonify
from modules.customers import bp
from extensions.DB import DB
from app import app

db = DB()

@bp.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    sql =   "INSERT INTO customers (first_name, last_name, address, " \
            "city, state, zip, phone, email) VALUES " \
            "(%s, %s, %s, %s, %s, %s, %s, %s)"
    info = (
            data['first_name'], data['last_name'], data['address'], data['city'],
            data['state'], data['zip'], data['phone'], data['email'])
    results = db.ExecUpdate(sql, info)
    return jsonify(results)

@bp.route('/', methods=['GET'])
@bp.route('/<id>', methods=['GET'])
def read(id = False):
    if id:
        sql = f"SELECT * FROM customers WHERE id = {id}"
    else:
        sql = "SELECT * FROM customers"
    results = db.ExecQuery(sql)
    return jsonify(results)

@bp.route('/<id>', methods=['POST','DELETE'])
def update_or_delete(id):
    if request.method == 'POST':
        # Update the data for this user
        data = request.get_json()
        sql =   "UPDATE customers SET first_name = %s, last_name = %s, address = %s, "\
                "city = %s, state = %s, zip = %s, phone = %s, email = %s WHERE "\
                "id = %s"
        info = (
            data['first_name'], data['last_name'], data['address'], data['city'],
            data['state'], data['zip'], data['phone'], data['email'], id) 
        results = db.ExecUpdate(sql, info)
    elif request.method == 'DELETE':
        # Delete the id of the customer
        sql = f"DELETE FROM customers WHERE id = {id} LIMIT 1"
        results = db.ExecUpdate(sql)
    return jsonify(results)


