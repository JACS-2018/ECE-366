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

app = Flask(__name__)
CORS(app)


######################################################## User ######################################################### 


#Register Function
@app.route('/api/users', methods=['POST'])
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
        

## TODO: READ all user except themselves and their friends (suggested friends)
#Read all users function
@app.route('/api/users', methods=['GET'])
def see_users():
    content = request.json

    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)    

    dict_user = edit_user.read_u(cursor, 0,0,0)
    array_user = []
    
    for user in dict_user.items():
        username = user.u_name
        firstName = user.f_name
        lastName = user.l_name
        myid = user.user_id

        ind_user = {'username':username,'firstName':firstName,'lastName':lastName,'id':myid}

        array_user.append(ind_user)
    
    start_db.commitclose(cursor,db)
    
    return jsonify({'person':array_user})


#Delete User Function
@app.route('/api/users/<identity>', methods=['DELETE'])
def delete_user(identity):
    content = request.json

    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)    

    edit_user.delete_u(cursor, identity)

    start_db.commitclose(cursor, db)
    
    return jsonify({'id':identity, 'success':'true'})


@app.route('/api/users/<user>', methods=['GET'])
def get_tasks4(user):
    content = request.json
    return jsonify({'user':user, 'success':'true'})


# Authenticates people
@app.route('/api/authenticate',methods=['POST'])
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



##################################################### Friendships ##################################################### 

Sees all Friends
@app.route('/api/friendships/<username>',methods=['GET'])
    content = request.json

    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)    

    f_dict = edit_friendships.see_f(cursor, username)
    array_f = []
    
    for friend in f_dict.items():
        username = friend.u_name
        firstName = friend.f_name
        lastName = friend.l_name
        myid = friend.user_id

        ind_f = {'username':username,'firstName':firstName,'lastName':lastName,'id':myid}

        array_f.append(ind_f)
    
    start_db.commitclose(cursor, db)
    
    return jsonify({'person':array_f})



# Add a Friend



# Confirm/Delete Friend




######################################################## Posts ########################################################



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)