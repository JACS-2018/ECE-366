#!/usr/bin/python
from flask import jsonify
import os
from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort
from flask_api import FlaskAPI
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/api/users', methods=['POST'])
def get_tasks():
    content = request.json
    return jsonify({'firstName':content['firstName'],'lastName':content['lastName'],'username':content['username'],'password':content['password'], 'success':'true'})

@app.route('/api/users', methods=['GET'])
def get_tasks2():
    content = request.json
    return jsonify({'users.username':"{Bob}"})

@app.route('/api/users', methods=['DELETE'])
def get_tasks3():
    content = request.json
    return jsonify({'success':'true'})


@app.route('/api/authenticate',methods=['POST'])
def Authenticate():
    content = request.json
    res =  jsonify({'username':content['username'],'password':content['password'], 'success':'true'})
    return res

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000,debug=True)
