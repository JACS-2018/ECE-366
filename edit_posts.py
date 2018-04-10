#!/usr/bin/python

import MySQLdb
import datetime
from copy import deepcopy

#current db on VM: playgroundapr8v2; on jas' computer: playgroundapr8

#opening db connection: 
db = MySQLdb.connect("localhost", "root", "password", "playgroundapr8")

#preparing cursor option using cursor() method
cursor = db.cursor()



db.commit()
cursor.close()
db.close()
