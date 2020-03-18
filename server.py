from flask import Flask
import getcountrydata
import flask_restful.reqparse as parserrequest
import flask_restful


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/country/guide/<string:country>")
def countryroute(country):
	obj = getcountrydata.getdata(country)
	return obj[0]

@app.route("/parser/")
def parsertest():
	parser = rp.RequestParser()
	parser.add_argument("info")
	args = 	parser.parse_args()
	return args["info"]
    
if __name__ == "__main__":
    app.run(debug=True)