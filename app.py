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
import json
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
    test = edit_user.user(user_id, firstname, lastname, username, password,'','','','','', start_time, 1)
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
        bday = user.bday
        occupation = user.occupation
        about = user.about
        email = user.email

        ind_user = {'username':username, 'firstName':firstName, 'lastName':lastName, 'id':myid, 'bday':bday, 'occupation':occupation, 'about':about, 'email':email}

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
        bday = user.bday
        occupation = user.occupation
        about = user.about
        email = user.email

        ind_user = {'username':username, 'firstName':firstName, 'lastName':lastName, 'id':myid, 'bday':bday, 'occupation':occupation, 'about':about, 'email':email}

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
    
    for friend in f_dict:
        username = friend.u_name
        firstName = friend.f_name
        lastName = friend.l_name
        myid = friend.user_id
        bday = friend.bday
        occupation = friend.occupation
        about = friend.about
        email = friend.email

        ind_f = {'username':username, 'firstName':firstName, 'lastName':lastName, 'id':myid, 'bday':bday, 'occupation':occupation, 'about':about, 'email':email}

        array_f.append(ind_f)
    
    start_db.commitclose(cursor, db)
    
    return jsonify({'person':array_f})


# #Sees Potential Friends
@app.route('/api/friendships/confirm/<username>',methods=['GET'])
def see_pot_friends(username):
    content = request.json

    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)
    
    f_dict = edit_friendships.allpotential_f(cursor, username, 1)
    array_f = []

    for friend in f_dict:
        username = friend.u_name
        firstName = friend.f_name
        lastName = friend.l_name
        myid = friend.user_id
        bday = friend.bday
        occupation = friend.occupation
        about = friend.about
        email = friend.email

        ind_f = {'username':username, 'firstName':firstName, 'lastName':lastName, 'id':myid, 'bday':bday, 'occupation':occupation, 'about':about, 'email':email}

        array_f.append(ind_f)
    
    start_db.commitclose(cursor, db)
    print array_f
    return jsonify({'person':array_f})

@app.route('/api/friendships/exists/<requestexists>',methods=['GET'])
def check_requests(requestexists):
    json_acceptable_string = requestexists.replace("'", "\"")
    requestexists = json.loads(json_acceptable_string)

    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)

    f_dict = edit_friendships.request_exists_f(cursor, requestexists['user_id_a'],requestexists['user_id_b'])
    print f_dict
    start_db.commitclose(cursor, db)

    if f_dict == 1:
        return jsonify({'exists':'requestgood'})
    else:
        return jsonify({'exists':'requestbad'})

# #Friends you're awaiting confirmation from
@app.route('/api/friendships/awaiting/<username>',methods=['GET'])
def wait_confirm(username):

    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)

    f_dict = edit_friendships.allpotential_f(cursor, username, 2)
    array_f = []

    for friend in f_dict:
        username = friend.u_name
        firstName = friend.f_name
        lastName = friend.l_name
        myid = friend.user_id
        bday = friend.bday
        occupation = friend.occupation
        about = friend.about
        email = friend.email

        ind_f = {'username':username, 'firstName':firstName, 'lastName':lastName, 'id':myid, 'bday':bday, 'occupation':occupation, 'about':about, 'email':email}

        array_f.append(ind_f)
    print array_f
    start_db.commitclose(cursor, db)

    return jsonify({'person':array_f})

# # Add a Friend
@app.route('/api/friendships/add',methods=['POST'])
def add_friend():
    content = request.json
    print "content" 
    print content
    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)

    checkbit = edit_friendships.add_f(cursor,content['user_id_a'], content['user_id_b']) #just in case, "supposed" to be user_id
    
    start_db.commitclose(cursor, db)

    #need to pull relevant info out of content, if necessary

    if checkbit == 0:
        return jsonify({'user_a':content['user_id_a'], 'user_b':content['user_id_b'], 'success':'false'})
    else:
        return jsonify({'user_a':content['user_id_a'], 'user_b':content['user_id_b'], 'success':'true'}) 

# # Confirm Friend
@app.route('/api/friendships/confirming',methods=['POST'])
def confirm_friend():
    content = request.json

    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)

    #may need to change status from string to int
    checkbit = edit_friendships.confirm_f(cursor,content['user_id_a'], content['user_id_b'],content['status'])

    start_db.commitclose(cursor, db)
    print "checkbit"
    print checkbit
    #Again, need to pull out all relevant info from content
 
    if checkbit > 0:
        if checkbit == 2:
            return jsonify({'user_a':content['user_id_a'], 'user_b':content['user_id_b'], 'result':'denied'}) #return for deny, success
        else:
            return jsonify({'user_a':content['user_id_a'], 'user_b':content['user_id_b'], 'result':'accepted'}) #return for accept, success
    else:
        if checkbit == -2:
            return '',status.HTTP_404_NOT_FOUND
        else:
            return '',status.HTTP_404_NOT_FOUND


# # Delete Friend
@app.route('/api/friendships/<username_a>/<username_b>',methods=['DELETE'])
def delete_friend():
    content = request.json

    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)

    edit_friendships.delete_f(cursor,username_a,username_b) #if either this or confirm friend breaks, check if delete_f in edit_friendships has been switched to usernames
    
    start_db.commitclose(cursor, db)

    return jsonify({'username_a':username_a,'username_b':username_b,'success':'true'})

######################################################## Posts ########################################################

#requires fill in based on front end
@app.route('/api/posts',methods=['POST'])
def makepost():
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
    user_id_a = content['user_id_a']
    user_id_b = content['user_id_b']
    writeup = content['content']
    newpost = edit_posts.post(post_id, user_id_a, user_id_b, timestamp, writeup)
    check = edit_posts.create_p(cursor, newpost)
    start_db.commitclose(cursor, db)

    if check == 1:
        return jsonify({'stuff':content})
        #return correct jsonify
    else:
        return '',status.HTTP_404_NOT_FOUND
        #return error jsonify?

@app.route('/api/posts/<useridb>',methods=['GET'])
def getpost(useridb):
    json_acceptable_string = useridb.replace("'", "\"")
    useridb = json.loads(json_acceptable_string)
    db = start_db.launchdb()
    cursor = start_db.launchcursor(db)

    post_dict = edit_posts.show_p(cursor,useridb['user_id_a'],useridb['user_id_b'])
    #Need to decide what to do with post_dict after grabbing it
    friendzone = edit_friendships.is_f(cursor,useridb['user_id_a'],useridb['user_id_b'])
    start_db.commitclose(cursor, db)
    if (post_dict != 0):
        if(len(post_dict) != 0):
            return jsonify({'posts':post_dict})
        else:
            return jsonify({'posts': 1})
    elif (friendzone == 1):
        return jsonify({'posts': 1})
    else:
        return jsonify({'posts': 0})

#Need to be able to grab all posts for display
#Delete Posts (bugtesting)


#Optional?
#Comments on Posts
#Editing Posts
#Editing Comments

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
