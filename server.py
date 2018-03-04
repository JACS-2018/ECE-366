from flask import Flask
from flask import request
import _mysql as mysqldb
db = mysqldb.connect('localhost', 'mysql', 'password', 'jacs')
app = Flask(__name__)

@app.route("/")
def root(): 
	return "at root of base app"
 
@app.route("/idk/add")
def idk(): 
	name = request.args.get('name')
	age = request.args.get('age')


@app.route("/idk")
def idk(): 
	mysqldb.query("SELECT * FROM test:")
	result = mysqldb.store_result()
	result = result.fetch_row(maxrows = 0)
	
