import requests

def getdata(country):
	url = "https://restcountries.eu/rest/v2/name/" + country
	request = requests.get(url)
	jsonObj = request.json()
	return jsonObj[0]

def setstring():
	return "aa"