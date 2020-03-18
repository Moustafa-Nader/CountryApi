import requests

def getdata(country):
	url = "https://restcountries.eu/rest/v2/name/" + country
	request = requests.get(url)
	jsonObj = request.json()
	return jsonObj

def setstring():
	return "aa"