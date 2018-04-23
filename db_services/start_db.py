import MySQLdb
import datetime
from copy import deepcopy

#current db on VM: playgroundapr8; on jas' computer: playgroundapr8; on github: playgroundapr11

def launchdb():
	db = MySQLdb.connect(host="localhost", user="root", passwd="", db="playgroundapr8")
	return db

def launchcursor(db):
	cursor = db.cursor()
	return cursor

def commitclose(cursor, db):
	db.commit()
	cursor.close()
	db.close()
