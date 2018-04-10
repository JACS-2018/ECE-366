#!/usr/bin/python

import MySQLdb
import datetime

#opening db connection
db = MySQLdb.connect("localhost", "root", "password", "playgroundapr8v2	")

#preparing cursor option using cursor() method
cursor = db.cursor()


# TODO! add profile picture, description, birthday

############################### User Class Declarations ###############################

class user:
	def __init__(self, user_id, f_name, l_name, u_name, pwrd, email, time):
		self.user_id = user_id
		self.f_name = f_name
		self.l_name = l_name
		self.u_name = u_name
		self.pwrd = pwrd
		self.email = email
		self.time = time


############################### Start Function Declarations ###############################

## Insert New User ##
#insert new user takes in a class called User (as defined above and puts it into the database)
def insert_u(user):
	ins = ("INSERT INTO User" 
			"(user_id, first_name, last_name, username, password, email, signup_date)"
			"VALUES (%s, %s, %s, %s, %s, %s, %s)")
			
	data_user = (user.user_id, user.f_name, user.l_name, user.u_name, user.pwrd, user.email, user.time)

	cursor.execute(ins, data_user)

	# TODO! make sure no usernames are the same and no emails are the same
	
## Read User Info ##
#read user info (mostly used for searching for friends or going to specific people's profiles -> username ?)
def read_u(f_name, l_name, u_name): 
	if u_name:
		read = ("SELECT * FROM User WHERE username = %(username)s")
		value = {'username': u_name}
	else:
		read = ("SELECT * FROM User WHERE first_name = %s AND last_name = %s")	
		value = (f_name, l_name)

	cursor.execute(read, value)
	data = cursor.fetchall()
	for user in data:
	 	print("%s %s's signup date is %s" %(user[1], user[2], user[7]))
	 	## TODO!! put it into the user class format + return from the function
## maybe change this to get the user_id and pass the user_id into another function called "read" and have this one as "find"



## Update User ##
#update user (takes information from their OWN profile)
def update_u(f_name, l_name, u_name, new_u):
	print("hello")
	## TODO!! has to have first name, last name and username
	read = ("SELECT * FROM User WHERE username = %s AND first_name = %s AND last_name = %s")
	value = (u_name, f_name, l_name)
	cursor.execute(read, value) #TODO, gets user_id then alter
	user = cursor.fetchall()
	old_u = user(user[0], user[1], user[2], user[3], user[4], user[5], user[6])
	
	if old_u.u_name != new_u.u_name:
		print("hello")
	if old_u.f_name != new_u.f_name:
		print("hello")
	if old_u.l_name != new_u.l_name:
		print("hello")
	if old_u.pwrd != new_u.pwrd:
		print("hello")
	if old_u.email != new_u.email:
		print("hello")

#delete user
def delete_u():
	print("hello")

#used for sign in/updating information in user
def confirm_u(u_name, email, password):
	print("hello")

############################### Finished Function Declarations ###############################


user_id = cursor.lastrowid
start_time = datetime.datetime.now()
me = user(user_id, 'Jasmine', 'Tang', 'jtangqt', 'hehexd', 'tang@cooper.edu', start_time)
			
#insert_u(me)
read_u('Jasmine', 'Tang', "jtangqt")


# cursor.execute(ins, data_user)
db.commit()


cursor.close()
db.close()