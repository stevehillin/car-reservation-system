import os
import json
from flask import request, jsonify
from modules.bookings import bp
from extensions.DB import DB
from app import app

db = DB()

@bp.route('/create', methods=['POST'])
def create():
    data = request.get_json()

@bp.route('/', methods=['GET'])
def read():
    # return jsonify({'message': 'Query executed successfully'})
    results = db.ExecQuery("SELECT * FROM bookings ORDER BY id DESC")
    return jsonify(results)

@bp.route('/update/<id>', methods=['POST'])
def update(id):
    pass

@bp.route('/delete/<id>', methods=['POST'])
def delete(id):
    pass
