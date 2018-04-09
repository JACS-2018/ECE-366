#!/usr/bin/python

import MySQLdb
import datetime

#opening db connection
db = MySQLdb.connect("localhost", "root", "password", "playgroundapr8v2")

#preparing cursor option using cursor() method
cursor = db.cursor()

class user:
	def __init__(self, user_id, f_name, l_name, u_name, pwrd, email, time):
		self.user_id = user_id
		self.f_name = f_name
		self.l_name = l_name
		self.u_name = u_name
		self.pwrd = pwrd
		self.email = email
		self.time = time


#insert new user
def insert_u(user):
	ins = ("INSERT INTO User" 
			"(user_id, first_name, last_name, username, password, email, signup_date)"
			"VALUES (%s, %s, %s, %s, %s, %s, %s)")
			
	data_user = (user.user_id, user.f_name, user.l_name, user.u_name, user.pwrd, user.email, user.time)

	cursor.execute(ins, data_user)
	


#read user info
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
	 	print("%s %s's password is %s" %(user[1], user[2], user[4]))
	 	## TODO!! put it into the user class format 

#update user
def update_u():
	print("hello")

#delete user
def delete_u():
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