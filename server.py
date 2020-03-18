from flask import Flask
from flask_restful import Resource , Api
from requesthandler import requesthandler

app = Flask(__name__)
api = Api(app)

api.add_resource(requesthandler , "/country/guide/<string:country>")

if __name__ == "__main__":
    app.run(debug=True)
#@app.route("/")
#def home():
#    return "Hello, World!"

#@app.route("/country/guide/<string:country>")
#def countryroute(country):
#	obj = getcountrydata.getdata(country)
#	return obj[0]

#@app.route("/parser/")
#def parsertest():
#	parser = rp.RequestParser()
#	parser.add_argument("info")
#	args = 	parser.parse_args()
#	return args["info"]
