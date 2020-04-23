import unittest
import sys
sys.path.append("..")
import server
import getcountrydata
import requesthandler

class Test_requestHandler(unittest.TestCase):
	def test_getActualCountry(self):
		with server.app.test_client() as client:
			resp = client.get("/country/guide/egypt")
		args = teststring1
		self.assertEqual(resp.json,args)

	def test_getFakeCountry(self):
		with server.app.test_client() as client:
			resp = client.get("/country/guide/FakCountry")
		self.assertEqual(resp.json,"404 Country Not found")

	def test_getPopEgypt(self):
		with server.app.test_client() as client:
			resp = client.get("/country/guide/egypt?info=population")
		self.assertEqual(resp.json,{'population': 91290000})





teststring1 = {u'timezones': [u'UTC+02:00'], u'demonym': u'Egyptian', u'regionalBlocs': [{u'acronym': u'AU', u'otherNames': [u'\u0627\u0644\u0627\u062a\u062d\u0627\u062f \u0627\u0644\u0623\u0641\u0631\u064a\u0642\u064a', u'Union africaine', u'Uni\xe3o Africana', u'Uni\xf3n Africana', u'Umoja wa Afrika'], u'name': u'African Union', u'otherAcronyms': []}, {u'acronym': u'AL', u'otherNames': [u'\u062c\u0627\u0645\u0639\u0629 \u0627\u0644\u062f\u0648\u0644 \u0627\u0644\u0639\u0631\u0628\u064a\u0629', u'J\u0101mi\u02bbat ad-Duwal al-\u02bbArab\u012byah', u'League of Arab States'], u'name': u'Arab League', u'otherAcronyms': []}], u'currencies': [{u'symbol': u'\xa3', u'code': u'EGP', u'name': u'Egyptian pound'}], u'alpha2Code': u'EG', u'alpha3Code': u'EGY', u'area': 1002450.0, u'languages': [{u'nativeName': u'\u0627\u0644\u0639\u0631\u0628\u064a\u0629', u'iso639_2': u'ara', u'name': u'Arabic', u'iso639_1': u'ar'}], u'capital': u'Cairo', u'borders': [u'ISR', u'LBY', u'SDN'], u'altSpellings': [u'EG', u'Arab Republic of Egypt'], u'gini': 30.8, u'translations': {u'fr': u'\xc9gypte', u'nl': u'Egypte', u'pt': u'Egipto', u'hr': u'Egipat', u'de': u'\xc4gypten', u'it': u'Egitto', u'fa': u'\u0645\u0635\u0631', u'br': u'Egito', u'ja': u'\u30a8\u30b8\u30d7\u30c8', u'es': u'Egipto'}, u'flag': u'https://restcountries.eu/data/egy.svg', u'nativeName': u'\u0645\u0635\u0631\u200e', u'topLevelDomain': [u'.eg'], u'numericCode': u'818', u'population': 91290000, u'callingCodes': [u'20'], u'name': u'Egypt', u'region': u'Africa', u'subregion': u'Northern Africa', u'cioc': u'EGY', u'latlng': [27.0, 30.0]}

unittest.main()