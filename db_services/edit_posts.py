#!/usr/bin/python

import MySQLdb
import datetime
from copy import deepcopy

#import start_db

############################### User Class Declarations ###############################

class post:
	def __init__(self, post_id, user_a, user_b, timestamp, content):
		self.post_id = post_id
		self.user_a = user_a #user a is the one posting, user b is the one whose profile user_a is posting on 
		self.user_b = user_b
		self.timestamp = timestamp
		self.content = content #content can be words or it can also be a relative path to media content 


############################### Start Function Declarations ###############################

## Creating a Post from A to B's Profile ##
def create_p(cursor, post):

	find = ("SELECT * FROM Friendships WHERE (user_id_a = %s AND user_id_b = %s) OR (user_id_a = %s AND user_id_b = %s) AND status = 1")
	value = (post.user_a, post.user_b, post.user_b, post.user_a)
	cursor.execute(find, value)
	friends = cursor.fetchone()
	
	if friends or post.user_a == post.user_b: 
		create = ("INSERT INTO Posts"
				"(post_id, user_a, user_b, timestamp, content)"
				"VALUES (%s, %s, %s, %s, %s)")
		value = (post.post_id, post.user_a, post.user_b, post.timestamp, post.content)
		cursor.execute(create, value)
		return 1
	else:
		return 0 	


## Shows Posts on User b's Profile ## (TODO!! if original poster isnt there anymore, show null)
def show_p(cursor, user_a, user_b):
	find = ("SELECT * FROM Friendships WHERE (user_id_a = %s AND user_id_b = %s) OR (user_id_a = %s AND user_id_b = %s) AND status = 1")
	value = (user_a, user_b, user_b, user_a)
	cursor.execute(find, value)
	friends = cursor.fetchone()
	
	name = ("SELECT * FROM User WHERE user_id = %(user_id)s")
	value = {'user_id' : user_b}
	cursor.execute(name, value)
	p_profile = cursor.fetchone()

	if friends or user_a == user_b:
		show = ("SELECT * FROM Posts WHERE user_b = %(user_b)s")
		value = {'user_b' : user_b}
		cursor.execute(show, value)
		all_p = cursor.fetchall()

		post_dict = []
		for ind_p in all_p: 
			find_u = ("SELECT * FROM User WHERE user_id = %(user_id)s")
			value = {'user_id': ind_p[1]}
			cursor.execute(find_u, value)
			friend = cursor.fetchone()
			i_dict = post(ind_p[0], ind_p[1], ind_p[2], ind_p[3], ind_p[4])
			resp = {'post_id':ind_p[0], 'user_a':ind_p[1], 'user_b':ind_p[2], 'timestamp':ind_p[3], 'content':ind_p[4]}
			post_dict.append(resp)
		return post_dict
	else:
		return 0


## Delete post based on post_id ##
def delete_p(cursor, post_id):
	delete = ("DELETE FROM Posts WHERE post_id = %(post_id)s")
	value = {'post_id' : post_id}
	cursor.execute(delete, value)


## Can User Edit Post? ##	
def can_edit_p(cursor, user_a, post_id):
	find_w = ("SELECT * FROM Posts WHERE post_id = %(post_id)s")
	value = {'post_id': post_id}
	cursor.execute(find_w, value)
	post = cursor.fetchone()
	if post[1] == user_a:
		return 1
	else: 
		return 0


## Edit post made by user ##
# Has to go through "can_edit_p" before edit_p
def edit_p(cursor, post_id, new_p): 
	edit = ("SELECT * FROM Posts WHERE post_id = %(post_id)s")
	value = {'post_id': post_id}
	cursor.execute(edit, value)
	old_p = cursor.fetchone()
	if new_p != old_p[4]:
		update = ("UPDATE Posts SET content = %s WHERE post_id = %s")
		value = (new_p, post_id)
		cursor.execute(update, value)



## TODO! 
## Show Feed Post ##
# def show_p(cursor, user_id):
# 	show = ("SELECT * FROM Posts")
# 	cursor.execute(show)
# 	all_p = cursor.fetchall()
# 	for ind_p in all_p:
# 		friends = ("SELECT * FROM Friendships WHERE (user_id_a = %s AND user_id_b = %s) OR (user_id_a = %s AND user_id_b = %s) AND status = 1")
# 		value = (ind_p[1], ind_p[2], ind_p[2], ind_p[1])
# 		cursor.execute()
# 		if friends: 
			

############################### Finished Function Declarations ###############################


'''
db = start_db.launchdb()
cursor = start_db.launchcursor(db)   

post_time = datetime.datetime.now()
post_id = cursor.lastrowid
post1 = post(post_id, 18, 12, post_time, 'hehe')
post_time = datetime.datetime.now()
post_id = cursor.lastrowid
post2 = post(post_id, 14, 13, post_time, 'hi bff')
post_time = datetime.datetime.now()
post_id = cursor.lastrowid
post3 = post(post_id, 13, 14, post_time, 'hello to you too bff')
post_time = datetime.datetime.now()
post_id = cursor.lastrowid
post4 = post(post_id, 14, 16, post_time, 'i can make my own post!!!')
post_id = cursor.lastrowid
post5 = post(post_id, 14, 14, post_time, 'i can make my own post!!!')
#create_p(cursor, post5)

# create_p(cursor, post1)
# create_p(cursor, post2)
# create_p(cursor, post3)
# create_p(cursor, post4)

edit_p(cursor, 4, 'HIIII WAZZUP')
#delete_p(cursor, 7)



start_db.commitclose(cursor, db)
'''