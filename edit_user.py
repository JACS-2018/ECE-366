#!/usr/bin/python

import MySQLdb
import datetime
from copy import deepcopy

#current db on VM: playgroundapr8v2; on jas' computer: playgroundapr8; on github: playgroundapr9v2

#opening db connection: 
db = MySQLdb.connect("localhost", "root", "password", "playgroundapr8")

#preparing cursor option using cursor() method
cursor = db.cursor()


############################### User Class Declarations ###############################

class user:
	def __init__(self, user_id, f_name, l_name, u_name, pwrd, pro_pic, about, email, time, active):
		self.user_id = user_id
		self.f_name = f_name
		self.l_name = l_name
		self.u_name = u_name
		self.pwrd = pwrd
		self.pro_pic = pro_pic
		self.about = about
		self.email = email
		self.time = time
		self.active = active


############################### Start Function Declarations ###############################

## Insert New User ##
#insert new user takes in a class called User (as defined above and puts it into the database)
def insert_u(user):
	if confirm_u(user.email): 
		print("email is the same")
		return 0	
	elif confirm_u(user.u_name):
		print("username is the same ")
		return 0
	else: 
		ins = ("INSERT INTO User" 
				"(user_id, first_name, last_name, username, password, pro_pic, about, email, signup_date, active)"
				"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
				
		data_user = (user.user_id, user.f_name, user.l_name, user.u_name, user.pwrd, user.pro_pic, user.about, user.email, user.time, user.active)

		cursor.execute(ins, data_user)
		return 1

	
## Read User Info ##
#read user info (mostly used for searching for friends or going to specific people's profiles -> username ?)
# TODO: different values of f_name & l_name 
def read_u(f_name, l_name, u_name): 
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
	 	user_dict[r_user[0]] = user(r_user[0], r_user[1], r_user[2], r_user[3], r_user[4], r_user[5], r_user[6], r_user[7], r_user[8], r_user[9])
	
	# for u_id in user_dict:
		# 	print("%s" %(user_dict[u_id].f_name))

	return user_dict


## Update User ##
#update user (takes information from their OWN profile- first, last, username)
def update_u(u_name, new_u):
	
	read = ("SELECT * FROM User WHERE username = %(username)s")
	value = {'username': u_name}
	cursor.execute(read, value) 
	
	u_user = cursor.fetchone()
	old_u = user(u_user[0], u_user[1], u_user[2], u_user[3], u_user[4], u_user[5], u_user[6], u_user[7], u_user[8], u_user[9])


	if old_u.u_name != new_u.u_name:
		update = ("UPDATE User SET username = %s WHERE user_id = %s")
		value = (new_u.u_name, old_u.user_id)
		cursor.execute(update, value)
	if old_u.f_name != new_u.f_name:
		update = ("UPDATE User SET first_name = %s WHERE user_id = %s")
		value = (new_u.f_name, old_u.user_id)
		cursor.execute(update, value)
	if old_u.l_name != new_u.l_name:
		update = ("UPDATE User SET last_name = %s WHERE user_id = %s")
		value = (new_u.l_name, old_u.user_id)
		cursor.execute(update, value)
	if old_u.pwrd != new_u.pwrd:
		update = ("UPDATE User SET password = %s WHERE user_id = %s")
		value = (new_u.pwrd, old_u.user_id)
		cursor.execute(update, value)
	if old_u.email != new_u.email:
		update = ("UPDATE User SET email = %s WHERE user_id = %s")
		value = (new_u.email, old_u.user_id)
		cursor.execute(update, value)

	print("Done Updating!")

## Deactivate User ##
def deactivate_u(u_name):
	deactivate = ("SELECT * FROM User WHERE username = %(username)s")
	value = {'username': u_name}
	cursor.execute(deactivate, value)
	d_user = cursor.fetchone()
	
	update = ("UPDATE User SET active = 0 WHERE user_id = %(user_id)s")
	value = {'user_id': d_user[0]}
	cursor.execute(update, value)

## Reactivate User ##
def reactivate_u(u_name): 
	reactivate = ("SELECT * FROM User WHERE username = %(username)s")
	value = {'username': u_name}
	cursor.execute(reactivate, value)
	d_user = cursor.fetchone()
	
	update = ("UPDATE User SET active = 1 WHERE user_id = %(user_id)s")
	value = {'user_id': d_user[0]}
	cursor.execute(update, value)


## Confirm user exists ##
def confirm_u(sign_in, pwrd):
	find_u = ("SELECT * FROM User WHERE (username = %s OR email = %s) AND password = %s")
	value = (sign_in, sign_in, pwrd)
	cursor.execute(find_u, value)
	found = cursor.fetchall()

	if found: 
		return 1
	else: 
		return 0

## Delete User (for debugging purposes) ##
def delete_u(user_id):
	del_u = ("DELETE FROM User WHERE user_id = %(u_id)s")
	value = {'u_id' : user_id}
	cursor.execute(del_u, value)


############################### Finished Function Declarations ###############################


user_id = cursor.lastrowid
start_time = datetime.datetime.now()
car = user(user_id, 'Cardy', 'Wei', 'cwei', 'hehexd', '', '', 'wei1@cooper.edu', start_time, 1)

user_id = cursor.lastrowid
start_time = datetime.datetime.now()
jas = user(user_id, 'Jas', 'Tea', 'jtangbb', 'heh', '', '', 'tang@cooper.edu', start_time, 1)

user_id = cursor.lastrowid
start_time = datetime.datetime.now()
sam = user(user_id, 'sam', 'cheng', 'scheng829', 'wow', '', '', 'scheng839@gmail.com', start_time, 1)

user_id = cursor.lastrowid
start_time = datetime.datetime.now()
alex = user(user_id, 'alex', 'hu', 'enigmamemoryg', 'cupnoodles', '', '', 'hu5@cooper.edu', start_time, 1)

user_id = cursor.lastrowid
start_time = datetime.datetime.now()
eric = user(user_id, 'eric', 'n', 'eric.ng.5013', 'hehe', '', '', '501@col.edu', start_time, 1)


#new_me = deepcopy(me)
#new_me.email = "hehe@gmail.com"


insert_u(car)
insert_u(jas)
insert_u(sam)
insert_u(alex)
insert_u(eric)
read_u(0, 0, 0)


# cursor.execute(ins, data_user)
db.commit()
cursor.close()
db.close()