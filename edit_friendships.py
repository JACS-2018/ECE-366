#!/usr/bin/python

import MySQLdb
import datetime
from copy import deepcopy


############################### Start Function Declarations ###############################

## Add Friends ##
# Creates new table entry for friendship
def add_f(cursor, user_id_a, user_id_b):
	pot = ("SELECT * FROM Friendships WHERE (user_id_a = %s AND user_id_b = %s) OR (user_id_a = %s AND user_id_b = %s)")
	value = (user_id_a, user_id_b, user_id_b, user_id_a)
	cursor.execute(pot, value)
	found = cursor.fetchall()

	if found: 
		print("We have this value already")
	else:
		add = ("INSERT INTO Friendships"
		"(user_id_a, user_id_b, status)"
		"VALUES (%s, %s, 0)")

		value = (user_id_a, user_id_b)
		cursor.execute(add, value)


## Confirm Friends ##
# Confirm friends makes bit = 1, if not confirmed, then deletes table entry
def confirm_f(cursor, user_id_a, user_id_b, status):
	if status:
		confirm = ("UPDATE Friendships SET status = 1 WHERE user_id_a = %s AND user_id_b = %s")
		value = (user_id_a, user_id_b)
		cursor.execute(confirm, value)
	else:
		delete_f(cursor, user_id_a, user_id_b)


## See Friendships ##
def see_f(cursor, user_id):
	## for debugging purposes:
	individual = ("SELECT * FROM User WHERE user_id = %(user_id)s")
	value = {'user_id': user_id}
	cursor.execute(individual, value) 
	i_name = cursor.fetchone()
	print("Your name is: %s %s" %(i_name[1], i_name[2]))

	
	see = ("SELECT * FROM Friendships WHERE (user_id_a = %s OR user_id_b = %s) AND status = 1")
	value = (user_id, user_id)
	cursor.execute(see, value)
	s_friends = cursor.fetchall()
	
	for all_f in s_friends:
		if all_f[0] == user_id:
			user_id2 = all_f[1]
		else: 
			user_id2 = all_f[0]
		find_u = ("SELECT * FROM User WHERE user_id = %(user_id)s")
		value = {'user_id': user_id2}
		cursor.execute(find_u, value)
		f_name = cursor.fetchone()
		print("You are friends with %s %s" %(f_name[1], f_name[2]))


## See Potential Friendships ##
def allpotential_f(cursor, user_id):
	## you have to accept
	unaccepted = ("SELECT * FROM Friendships WHERE user_id_b = %(user_id_b)s AND status = 0")
	value = {'user_id_b': user_id}
	cursor.execute(unaccepted, value)
	u_friends = cursor.fetchall()

	for all_u_f in u_friends:
		find_u_f = ("SELECT * FROM User WHERE user_id = %(user_id)s")
		value = {'user_id': all_u_f[0]}
		cursor.execute(find_u_f, value)
		u_f_name = cursor.fetchone()
		print("You have an unconfirmed friendship with: %s %s" %(u_f_name[1], u_f_name[2]))
	

	## they have to accept
	waiting = ("SELECT * FROM Friendships WHERE user_id_a = %(user_id_a)s AND status = 0")
	value = {"user_id_a": user_id}
	cursor.execute(waiting, value)
	w_friends = cursor.fetchall()

	for all_w_f in w_friends:
		find_w_f = ("SELECT * FROM User WHERE user_id = %(user_id)s")
		value = {'user_id': all_w_f[1]}
		cursor.execute(find_w_f, value)
		w_f_name = cursor.fetchone()
		print("You are waiting for a friendship with: %s %s" %(w_f_name[1], w_f_name[2]))


## Delete Friends ## 
# deletes table entry of friends
def delete_f(cursor, user_id_a, user_id_b):
	f_delete = ("DELETE FROM Friendships WHERE (user_id_a = %s AND user_id_b = %s) OR (user_id_a = %s AND user_id_b = %s)")
	value = (user_id_a, user_id_b, user_id_b, user_id_a)
	cursor.execute(f_delete, value)


############################### Finished Function Declarations ###############################


'''
add_f(cursor, 1,2)
add_f(cursor, 1,4)
add_f(cursor, 1,3)
add_f(cursor, 2,3)
add_f(cursor, 2,5)
add_f(cursor, 3,5)
add_f(cursor, 5,1)
add_f(cursor, 4,3)
add_f(cursor, 4,2)
confirm_f(cursor, 2, 3,1)
confirm_f(cursor, 2, 5, 1)
confirm_f(cursor, 1, 4, 1)
confirm_f(cursor, 4,3,1)
allpotential_f(cursor, 1)
see_f(cursor, 1)
allpotential_f(cursor, 2)
see_f(cursor, 2)
allpotential_f(cursor, 3)
see_f(cursor, 3)
allpotential_f(cursor, 4)
see_f(cursor, 4)
allpotential_f(cursor, 5)
see_f(cursor, 5)