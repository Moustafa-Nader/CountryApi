import unittest
import requests
import sys
sys.path.append("..")
import getcountrydata


class getcountrydatapyTest(unittest.TestCase):
	def test_getcountrydata(self):
		url = "https://restcountries.eu/rest/v2/name/egypt"
		request = requests.get(url)
		jsonObj = request.json()
		self.assertEqual(getcountrydata.getdata("egypt"),jsonObj[0])

	def test_getfakecountrydata(self):
		self.assertEqual(getcountrydata.getdata("dsaefaeaeda"),None)

											
#class requesthandlerTest(unittest.TestCase):
	#def test_parseQuery(self):
unittest.main()