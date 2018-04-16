#!/usr/bin/python
from flask import jsonify
import os
from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort
from flask_api import FlaskAPI
from flask_cors import CORS
import edit_user
import datetime
import MySQLdb
app = Flask(__name__)
CORS(app)

#Register Function
@app.route('/api/users', methods=['POST'])
def get_tasks():
    content = request.json

    db = edit_user.launchdb()
    cursor = edit_user.launchcursor(db)

    firstname = content['firstName']
    lastname = content['lastName']
    username = content['username']
    password = content['password']
    
    user_id = cursor.lastrowid
    start_time = datetime.datetime.now()
    test = edit_user.user(user_id, firstname, lastname, username, password,'','','', start_time, 1)
    check = edit_user.insert_u(test,cursor)
    
    edit_user.commitclose(db,cursor)

    if check == 1:
        return jsonify({'firstName':content['firstName'],'lastName':content['lastName'],'username':content['username'],'password':content['password'], 'success':'true'})
    else:
        return '',status.HTTP_404_NOT_FOUND
        
#Read all users function
@app.route('/api/users', methods=['GET'])
def get_tasks2():
    content = request.json

    db = edit_user.launchdb()
    cursor = edit_user.launchcursor(db)    

    testdict = edit_user.read_u(0,0,0,cursor)
    bobarray = []
    
    for userid, user in testdict.items():
        username = user.u_name
        firstName = user.f_name
        lastName = user.l_name
        myid = user.user_id

        johndoe = {'username':username,'firstName':firstName,'lastName':lastName,'id':myid}

        bobarray.append(johndoe)
    
    edit_user.commitclose(db,cursor)
    
    #bob = {'username':'bobby','firstName':'bobbert','lastName':'lee','id':'bobbity'}

    '''

    user_id = cursor.lastrowid
    start_time = datetime.datetime.now()
    test = edit_user.user(user_id, 'Blah','Lmao','test1','haHAAAA','','','enigmamemory@gmail.com', start_time, 1)
    edit_user.insert_u(test,cursor)
    

    '''
    return jsonify({'person':bobarray})
    #return jsonify({'person':[bob]})


#Delete User Function
@app.route('/api/users/<identity>', methods=['DELETE'])
def get_tasks3(identity):
    content = request.json

    db = edit_user.launchdb()
    cursor = edit_user.launchcursor(db)    

    edit_user.delete_u(identity, cursor)

    edit_user.commitclose(db,cursor)
    
    return jsonify({'id':identity, 'success':'true'})

@app.route('/api/users/<user>', methods=['GET'])
def get_tasks4(user):
    content = request.json
    return jsonify({'user':user, 'success':'true'})


@app.route('/api/authenticate',methods=['POST'])
def Authenticate():
    
    content = request.json
    
    db = edit_user.launchdb()
    cursor = edit_user.launchcursor(db)    
    
    username = content['username']
    password = content['password']

    check = edit_user.confirm_u(username,password,cursor)
    #insert some function to check username and password here

    if check == 1:
        res =  jsonify({'username':content['username'],'password':content['password'], 'success':'true'})
    else:
        return '',status.HTTP_404_NOT_FOUND
    #if match:
    #res includes success:true

    #else:
    #res only has regular stuff

    edit_user.commitclose(db,cursor)
    
    #res =  jsonify({'username':content['username'],'password':content['password'], 'success':'true'})
    #do not add success true is false
    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
