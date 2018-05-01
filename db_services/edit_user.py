#!/usr/bin/python

import MySQLdb
import datetime
from copy import deepcopy


############################### User Class Declarations ###############################

class user:
	def __init__(self, user_id, f_name, l_name, u_name, pwrd, pro_pic, about, occupation, bday, email, time, active):
		self.user_id = user_id
		self.f_name = f_name
		self.l_name = l_name
		self.u_name = u_name
		self.pwrd = pwrd
		self.pro_pic = pro_pic
		self.about = about
		self.occupation = occupation
		self.bday = bday
		self.email = email
		self.time = time
		self.active = active

############################### Start Function Declarations ###############################


## Insert New User ##
#insert new user takes in a class called User (as defined above and puts it into the database)
def insert_u(cursor, user):
	# if confirm_u(cursor, user.email, 0): 
	# 	print("email is the same")
	# 	return 0	
	# elif
	if confirm_u(cursor, user.u_name, 0):
		return 0
	else: 
		ins = ("INSERT INTO User" 
				"(user_id, first_name, last_name, username, password, pro_pic, about, occupation, bday, email, signup_date, active)"
				"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
		data_user = (user.user_id, user.f_name, user.l_name, user.u_name, user.pwrd, user.pro_pic, user.about, user.occupation, user.bday, user.email, user.time, user.active)

		cursor.execute(ins, data_user)
		return 1

	
## Read User Info ##
#read user info (mostly used for searching for friends or going to specific people's profiles -> username ?)
# TODO: different values of f_name & l_name 
def read_u(cursor, f_name, l_name, u_name): 
	if f_name == 0 and l_name == 0 and u_name == 0:
		read = ("SELECT * FROM User")
		value = {}
	elif u_name:
		read = ("SELECT * FROM User WHERE username = %(username)s AND active = 1")
		value = {'username': u_name}
	else:
		read = ("SELECT * FROM User WHERE first_name = %s AND last_name = %s AND active = 1")	
		value = (f_name, l_name)


	cursor.execute(read, value)
	data = cursor.fetchall()
	user_dict = {}
	
	for r_user in data:
	 	user_dict[r_user[0]] = user(r_user[0], r_user[1], r_user[2], r_user[3], r_user[4], r_user[5], r_user[6], r_user[7], r_user[8], r_user[9], r_user[10], r_user[11])
	
	# for u_id in user_dict:
		# 	print("%s" %(user_dict[u_id].f_name))

	return user_dict


## Update User ##
#update user (takes information from their OWN profile- first, last, username)
def update_u(cursor, u_name, new_u):
	
	read = ("SELECT * FROM User WHERE username = %(username)s")
	value = {'username': u_name}
	cursor.execute(read, value) 
	
	u_user = cursor.fetchone()
	print u_user
	print new_u.bday
	print new_u.about
	print new_u.email
	print new_u.u_name
	old_u = user(u_user[0], u_user[1], u_user[2], u_user[3], u_user[4], u_user[5], u_user[6], u_user[7], u_user[8], u_user[9], u_user[10], u_user[11])

	if old_u.pro_pic != new_u.pro_pic:
		update = ("UPDATE User SET pro_pic = %s WHERE user_id = %s")
		value = (new_u.pro_pic, old_u.user_id)
		cursor.execute(update, value)
	if old_u.about != new_u.about:
		update = ("UPDATE User SET about = %s WHERE user_id = %s")
		value = (new_u.about, old_u.user_id)
		cursor.execute(update, value)
	if old_u.occupation != new_u.occupation:
		update = ("UPDATE User SET occupation = %s WHERE user_id = %s")
		value = (new_u.occupation, old_u.user_id)
		cursor.execute(update, value)
	if old_u.email != new_u.email:
		update = ("UPDATE User SET email = %s WHERE user_id = %s")
		value = (new_u.email, old_u.user_id)
		cursor.execute(update, value)
	if old_u.bday != new_u.bday:
		update = ("UPDATE User SET bday = %s WHERE user_id = %s")
		value = (new_u.bday, old_u.user_id)
		cursor.execute(update, value)
	return 1

## Confirm user exists ##
def confirm_u(cursor, sign_in, pwrd):
	if pwrd: 
		find_u = ("SELECT * FROM User WHERE (username = %s OR email = %s) AND password = %s")
		value = (sign_in, sign_in, pwrd)
	else: 
		find_u = ("SELECT * FROM User WHERE username = %s OR email = %s")
		value = (sign_in, sign_in)
	cursor.execute(find_u, value)
	found = cursor.fetchall()

	if found: 
		return 1
	else: 
		return 0


## Delete User (for debugging purposes) ## (TODO!! also delete all frienships)
def delete_u(cursor, user_id):
	del_u = ("DELETE FROM User WHERE user_id = %(u_id)s")
	value = {'u_id' : user_id}
	cursor.execute(del_u, value)


## Deactivate User ##
def deactivate_u(cursor, u_name):
	deactivate = ("SELECT * FROM User WHERE username = %(username)s")
	value = {'username': u_name}
	cursor.execute(deactivate, value)
	d_user = cursor.fetchone()
	
	update = ("UPDATE User SET active = 0 WHERE user_id = %(user_id)s")
	value = {'user_id': d_user[0]}
	cursor.execute(update, value)


## Reactivate User ##
def reactivate_u(cursor, u_name): 
	reactivate = ("SELECT * FROM User WHERE username = %(username)s")
	value = {'username': u_name}
	cursor.execute(reactivate, value)
	d_user = cursor.fetchone()
	
	update = ("UPDATE User SET active = 1 WHERE user_id = %(user_id)s")
	value = {'user_id': d_user[0]}
	cursor.execute(update, value)

## Given Username, find User ID ##
def find_u(cursor, username):
	query = ("SELECT * FROM User WHERE username = %(username)s")
	value = {'username': username}
	cursor.execute(query, value)
	person = cursor.fetchone()
	return person[0]


############################### Finished Function Declarations ###############################
