#!/usr/bin/python

import MySQLdb
import datetime
from copy import deepcopy
import edit_user
import start_db
	



############################### Start Function Declarations ###############################

## Add Friends ##
# Creates new table entry for friendship
def add_f(cursor, username_a, username_b):
	if username_a == username_b:
		return 0
	user_id_a = edit_user.find_u(cursor, username_a)
	user_id_b = edit_user.find_u(cursor, username_b)
	pot = ("SELECT * FROM Friendships WHERE (user_id_a = %s AND user_id_b = %s) OR (user_id_a = %s AND user_id_b = %s)")
	value = (user_id_a, user_id_b, user_id_b, user_id_a)
	cursor.execute(pot, value)
	found = cursor.fetchall()

	if found: 
		return 0
	else:
		add = ("INSERT INTO Friendships"
		"(user_id_a, user_id_b, status)"
		"VALUES (%s, %s, 0)")

		value = (user_id_a, user_id_b)
		cursor.execute(add, value)
		return 1


## Confirm Friends ##
# Confirm friends makes bit = 1, if not confirmed, then deletes table entry
# 1 in status makes friends and 0 in status deletes table entry
def confirm_f(cursor, username_a, username_b, status):
	user_id_a = edit_user.find_u(cursor, username_a)
	user_id_b = edit_user.find_u(cursor, username_b)

	if status:
		confirm = ("UPDATE Friendships SET status = 1 WHERE user_id_a = %s AND user_id_b = %s")
		value = (user_id_a, user_id_b)
		cursor.execute(confirm, value)
		test = ("SELECT * FROM Friendships WHERE user_id_a = %s AND user_id_b = %s AND status = 1")
		value = (user_id_a, user_id_b)
		cursor.execute(test, value)
		found = cursor.fetchall()
		if found:
			return 1
		else:
			return -1
	else:
		delete_f(cursor, user_id_a, user_id_b)
		test = ("SELECT * FROM Friendships WHERE user_id_a = %s AND user_id_b = %s")
		value = (user_id_a, user_id_b)
		cursor.execute(test, value)
		found = cursor.fetchall()
		if found:
			return -2
		else:
			return 2

## See All Friendships & Potential Friendships (0- where you guys are friends, 1 - where you have to accept, 2 - where you are awaiting their acceptance) ##
def allpotential_f(cursor, username, val):
	## you have to accept
	individual = ("SELECT * FROM User WHERE username = %(username)s")
	value = {'username': username}
	cursor.execute(individual, value) 
	i_name = cursor.fetchone()
	user_id = i_name[0]

	if val == 0: 
		find_p_f = ("SELECT * FROM Friendships WHERE (user_id_a = %s OR user_id_b = %s) AND status = 1")
		value = (user_id, user_id)
	elif val == 1: 
		find_p_f = ("SELECT * FROM Friendships WHERE user_id_b = %(user_id_b)s AND status = 0")
		value = {'user_id_b': user_id}
	else: 
		find_p_f = ("SELECT * FROM Friendships WHERE user_id_a = %(user_id_a)s AND status = 0")
		value = {"user_id_a": user_id}

	cursor.execute(find_p_f, value)
	u_friends = cursor.fetchall()

	ap_dict = []	
	for all_u_f in u_friends:
		if all_u_f[0] == user_id:
			user_id2 = all_u_f[1]
		else: 
			user_id2 = all_u_f[0]

		find_f = ("SELECT * FROM User WHERE user_id = %(user_id)s")
		value = {'user_id': user_id2}
		cursor.execute(find_f, value)
		u_f_name = cursor.fetchone()
		i_conf = edit_user.user(u_f_name[0], u_f_name[1], u_f_name[2], u_f_name[3], u_f_name[4], u_f_name[5], u_f_name[6], u_f_name[7], u_f_name[8], u_f_name[9], u_f_name[10], u_f_name[11])
		ap_dict.append(i_conf)

	return ap_dict


## Delete Friends ## 
# deletes table entry of friends
def delete_f(cursor, user_id_a, user_id_b):
	f_delete = ("DELETE FROM Friendships WHERE (user_id_a = %s AND user_id_b = %s) OR (user_id_a = %s AND user_id_b = %s)")
	value = (user_id_a, user_id_b, user_id_b, user_id_a)
	cursor.execute(f_delete, value)


def is_f(cursor, username_a, username_b):
	user_a = edit_user.find_u(cursor, username_a)
	user_b = edit_user.find_u(cursor, username_b)
	find = ("SELECT * FROM Friendships WHERE ((user_id_a = %s AND user_id_b = %s) OR (user_id_a = %s AND user_id_b = %s)) AND status = 1")
	value = (user_a, user_b, user_b, user_a)
	cursor.execute(find, value)
	friends = cursor.fetchone()
	if friends:
		return 1
	else:
		return 0

def request_exists_f(cursor, username_a, username_b):
	user_a = edit_user.find_u(cursor, username_a)
	user_b = edit_user.find_u(cursor, username_b)
	find = ("SELECT * FROM Friendships WHERE user_id_a = %s AND user_id_b = %s AND status = 0")
	value = (user_a, user_b)

	cursor.execute(find, value)
	exists = cursor.fetchone()

	if exists:
		return 1
	else:
		return 0

############################### Finished Function Declarations ###############################

