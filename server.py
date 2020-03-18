from flask import Flask
import getcountrydata
import flask_restful.reqparse as rp
import flask_restful as fr

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/country/guide/<string:country>")
def countryroute(country):
	obj = getcountrydata(country)
	return obj
	
    
if __name__ == "__main__":
    app.run(debug=True)