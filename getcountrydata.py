import requests

def getdata(country):
	url = "https://restcountries.eu/rest/v2/name/" + country
	request = requests.get(url)
	if request.status_code == 404:
		return None
	jsonObj = request.json()
	return jsonObj[0]