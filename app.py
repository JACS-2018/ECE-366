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
    
    for userid,user in dict_user.items():
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
    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)    

    dict_user = edit_user.read_u(cursor, 0,0,user)
    array_user = []
    
    for userid,user in dict_user.items():
        username = user.u_name
        firstName = user.f_name
        lastName = user.l_name
        myid = user.user_id

        ind_user = {'username':username,'firstName':firstName,'lastName':lastName,'id':myid}

        array_user.append(ind_user)
    
    start_db.commitclose(cursor,db)
    
    return jsonify({'person':array_user, 'success':'true'})


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

#Sees all Friends
@app.route('/api/friendships/<username>',methods=['GET'])
def read_friends(username):
    content = request.json

    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)    

    f_dict = edit_friendships.allpotential_f(cursor, username, 0)
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


# #Sees Potential Friends
# @app.route('/api/friendships/confirm/<username>',methods=['GET'])

# #Friends you're awaiting confirmation from
# @app.route('/api/friendships/awaiting/<username>',methods=['GET'])


# # Add a Friend
# @app.route('/api/friendships/',methods=['POST'])


# # Confirm/Delete Friend
# @app.route('/api/friendships/',methods=['PUT', 'DELETE'])
# def is_friend():
#     if request == 'PUT'



######################################################## Posts ########################################################

#requires fill in based on front end
@app.route('/api/posts/<user_id_a>/<user_id_b>',methods=['POST'])
def makepost(user_id_a,user_id_b):
    content = request.json

    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)

    '''
    #usera = edit_user.read_u(cursor, username_a) #might be (cursor, 0, 0, username_a)
    #userb = edit_user.read_u(cursor, username_b)
    '''
    #Supposedly want user_id, not user

    post_id = cursor.lastrowid
    timestamp = datetime.datetime.now()
    writeup = content['content']
    newpost = edit_posts.post(post_id, user_id_a, user_id_b, timestamp, writeup)
    check = create_p(cursor, post)
    
    start_db.commitclose(cursor, db)
    '''
    if check == 1:
        #return correct jsonify
    else:
        #return error jsonify?
    '''
    return 0

@app.route('/api/posts/<useridb>',methods=['GET'])
def getpost(useridb):
    content = request.json

    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)

    post_dict = edit_posts.show_p(cursor,useridb,useridb)

    #Need to decide what to do with post_dict after grabbing it

    start_db.commitclose(cursor, db)

    return jsonify({'posts':post_dict})

#Need to be able to grab all posts for display
#Delete Posts (bugtesting)


#Optional?
#Comments on Posts
#Editing Posts
#Editing Comments

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
