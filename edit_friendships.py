#!/usr/bin/python

import MySQLdb
import datetime
from copy import deepcopy

#current db on VM: playgroundapr8v2; on jas' computer: playgroundapr8

#opening db connection: 
db = MySQLdb.connect("localhost", "root", "password", "playgroundapr8")

#preparing cursor option using cursor() method
cursor = db.cursor()

## Add Friends ##
# Creates new table entry for friendship
def add_f(user_id_a, user_id_b):
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

	print("add friend end")


## Confirm Friends ##
# Confirm friends makes bit = 1, if not confirmed, then deletes table entry
def confirm_f(user_id_a, user_id_b, status):
	if status:
		confirm = ("UPDATE Friendships SET status = 1 WHERE user_id_a = %s AND user_id_b = %s")
		value = (user_id_a, user_id_b)
		cursor.execute(confirm, value)
	else:
		delete_f(user_id_a, user_id_b)

	print("DONE CONFIRMING")

## Delete Friends ## 
# deletes table entry of friends
def delete_f(user_id_a, user_id_b):
	f_delete = ("DELETE FROM Friendships WHERE (user_id_a = %s AND user_id_b = %s) OR (user_id_a = %s AND user_id_b = %s)")
	value = (user_id_a, user_id_b, user_id_b, user_id_a)
	cursor.execute(f_delete, value)
	print("DONE DELETING")

## See Friendships ##
def see_f(user_id):
	print("hi")
	see = ("SELECT * FROM Friendships WHERE (user_id_a = %s OR user_id_b = %s) AND status = 1")
	value = (user_id, user_id)
	cursor.execute(see, value)
	s_friends = cursor.fetchall()
	print("2")
	for all_f in s_friends:
		print("3")
		if all_f[0] == user_id:
			user_id2 = all_f[1]
		else: 
			user_id2 == all_f[0]
		print("hehe")
		find_u = ("SELECT * FROM User WHERE user_id = %(user_id)s")
		value = {'user_id': user_id2}
		cursor.execute(find_u, value)
		f_name = cursor.fetchone()
		print("You are friends with %s %s" %(f_name[1], f_name[2]))

## See Potential Friendships ##
def allpotential_f():

	print("hello")

add_f(1,2)
confirm_f(1,2, 1)
see_f(1)
delete_f(1, 2)


db.commit()
cursor.close()
db.close()
