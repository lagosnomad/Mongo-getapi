from flask import Flask
from pymongo import MongoClient
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
conn = MongoClient('mongodb://localhost:27017/')
db = conn.runapi

class departments(Resource):
	def get(self):
		return {'departments': [i for i in db.info.distinct("Department")]}

class departmentalDetails(Resource):
    def get(self, department_name):
    	return {'data': [i for i in db.info.find({"Department":department_name.upper()}, {"_id":0})]}

api.add_resource(departmentalDetails_lecturers, "/department/<string:department_name>")
api.add_resource(departments, "/departments")

if __name__ == "__main__":
    app.run(debug=True)
