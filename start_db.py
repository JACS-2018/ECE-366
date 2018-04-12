def launchdb():
	db = MySQLdb.connect("localhost", "root", "password", "playgroundapr8")
	return db

def launchcursor(db):
	cursor = db.cursor()
	return cursor

def commitclose(db, cursor):
	db.commit()
	cursor.close()
	db.close()
