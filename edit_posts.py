#!/usr/bin/python

import MySQLdb
import datetime
from copy import deepcopy

#current db on VM: playgroundapr8v2; on jas' computer: playgroundapr8

#opening db connection: 
db = MySQLdb.connect("localhost", "root", "password", "playgroundapr8")

#preparing cursor option using cursor() method
cursor = db.cursor()

############################### User Class Declarations ###############################

class post:
	def __init__(self, post_id, user_a, user_b, timestamp, content):
		self.post_id = post_id
		self.user_a = user_a
		self.user_b = user_b
		self.timestamp = timestamp
		self.content = content #content can be words or it can also be a relative path to media content 


############################### Start Function Declarations ###############################

#user a is the one posting, user b is the one whose profile user_a is posting on 
#user b is the profile you're looking at
def create_p(post):
	find = ("SELECT * FROM Friendships WHERE (user_id_a = %s AND user_id_b = %s) OR (user_id_a = %s AND user_id_b = %s) AND status = 1")
	value = (post.user_a, post.user_b, post.user_b, post.user_a)
	cursor.execute(find, value)
	friends = cursor.fetchone()
	
	if friends: 
		create = ("INSERT INTO Posts"
				"(post_id, user_a, user_b, timestamp, content)"
				"VALUES (%s, %s, %s, %s, %s)")
		value = (post.post_id, post.user_a, post.user_b, post.timestamp, post.content)
		cursor.execute(create, value)
	else:
		print("You are not allowed to post on this person's profile")	


def show_p(user_a, user_b):
	find = ("SELECT * FROM Friendships WHERE (user_id_a = %s AND user_id_b = %s) OR (user_id_a = %s AND user_id_b = %s) AND status = 1")
	value = (user_a, user_b, user_b, user_a)
	cursor.execute(find, value)
	friends = cursor.fetchone()
	
	name = ("SELECT * FROM User WHERE user_id = %(user_id)s")
	value = {'user_id' : user_b}
	cursor.execute(name, value)
	p_profile = cursor.fetchone()
	
	print("You are viewing %s %s's Profile" %(p_profile[1], p_profile[2]))

	if friends or user_a == user_b:
		show = ("SELECT * FROM Posts WHERE user_b = %(user_b)s")
		value = {'user_b' : user_b}
		cursor.execute(show, value)
		all_p = cursor.fetchall()

		for ind_p in all_p: 
			#TODO: make a linked list of posts (or something)
			find_u = ("SELECT * FROM User WHERE user_id = %(user_id)s")
			value = {'user_id': ind_p[1]}
			cursor.execute(find_u, value)
			friend = cursor.fetchone()
			print("%s %s says: %s\nTime: %s" %(friend[1], friend[2], ind_p[4], ind_p[3]))
	else:
		print("You aren't friends with this person, so you cannot see their profile")
			

def edit_p(): 
	print("hello")
	

############################### Finished Function Declarations ###############################

# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post1 = post(post_id, '1', '2', post_time, 'hehe')
# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post2 = post(post_id, '2', '3', post_time, 'hi bff')
# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post3 = post(post_id, '3', '2', post_time, 'hello to you too bff')
# post_time = datetime.datetime.now()
# post_id = cursor.lastrowid
# post4 = post(post_id, '4', '4', post_time, 'i can make my own post!!!')

# create_p(post1)
# create_p(post2)
# create_p(post3)
# create_p(post4)
show_p(2, 2)

db.commit()
cursor.close()
db.close()