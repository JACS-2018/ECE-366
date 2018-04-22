#!/usr/bin/python
from flask import jsonify
import os
from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort
from flask_api import FlaskAPI, status
from flask_cors import CORS
import datetime
import MySQLdb

import sys
sys.path.append('db_services')
import start_db
import edit_user
import edit_friendships
import edit_posts

app_user = Flask(__name__)
CORS(app_user)


#Register Function
@app_user.route('/api/users', methods=['POST'])
def register_user():
    content = request.json

    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)

    firstname = content['firstName']
    lastname = content['lastName']
    username = content['username']
    password = content['password']
    
    user_id = cursor.lastrowid
    start_time = datetime.datetime.now()
    test = edit_user.user(user_id, firstname, lastname, username, password,'','','', start_time, 1)
    check = edit_user.insert_u(cursor, test)
    
    start_db.commitclose(cursor, db)

    if check == 1:
        return jsonify({'firstName':content['firstName'],'lastName':content['lastName'],'username':content['username'],'password':content['password'], 'success':'true'})
    else:
        return '',status.HTTP_404_NOT_FOUND
        

#Read all users function
@app_user.route('/api/users', methods=['GET'])
def see_users():
    content = request.json

    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)    

    dict_user = edit_user.read_u(cursor, 0,0,0)
    array_user = []
    
    for userid, user in dict_user.items():
        username = user.u_name
        firstName = user.f_name
        lastName = user.l_name
        myid = user.user_id

        ind_user = {'username':username,'firstName':firstName,'lastName':lastName,'id':myid}

        array_user.app_userend(ind_user)
    
    start_db.commitclose(cursor,db)
    
    return jsonify({'person':array_user})


#Delete User Function
@app_user.route('/api/users/<identity>', methods=['DELETE'])
def delete_user(identity):
    content = request.json

    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)    

    edit_user.delete_u(cursor, identity)

    start_db.commitclose(cursor, db)
    
    return jsonify({'id':identity, 'success':'true'})


@app_user.route('/api/users/<user>', methods=['GET'])
def get_tasks4(user):
    content = request.json
    return jsonify({'user':user, 'success':'true'})


# Authenticates people
@app_user.route('/api/authenticate',methods=['POST'])
def Authenticate():
    
    content = request.json
    
    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)    
    
    username = content['username']
    password = content['password']

    check = edit_user.confirm_u(cursor, username, password)

    start_db.commitclose(cursor, db)

    if check == 1:
        return jsonify({'username':content['username'],'password':content['password'], 'success':'true'})
    else:
        return '',status.HTTP_404_NOT_FOUND


if __name__ == '__main__':
    app_user.run(host='0.0.0.0', port=5000,debug=True)