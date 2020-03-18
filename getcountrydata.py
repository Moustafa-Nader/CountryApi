import requests

def getdata(country):
	url = "https://restcountries.eu/rest/v2/name/" + country
	request = requests.get(url)
	jsonObj = requests.jsonObj
	return jsonObj