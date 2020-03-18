import unittest
import requests
import sys
sys.path.append("..")
import getcountrydata
import requesthandler


class getcountrydatapyTest(unittest.TestCase):
	def test_getcountrydata(self):
		url = "https://restcountries.eu/rest/v2/name/egypt"
		request = requests.get(url)
		jsonObj = request.json()
		self.assertEqual(getcountrydata.getdata("egypt"),jsonObj[0])

	def test_getfakecountrydata(self):
		self.assertEqual(getcountrydata.getdata("dsaefaeaeda"),None)

	def test_CheckNullObjtrue(self):
		self.assertEqual(requesthandler.CheckNullObj(None),True)

	def test_CheckNullObjfalse(self):
		self.assertEqual(requesthandler.CheckNullObj("None"),False)

	def test_CheckNullQuerytrue(self):
		self.assertEqual(requesthandler.CheckNullQuery(None),True)

	def test_CheckNullQueryfalse(self):
		self.assertEqual(requesthandler.CheckNullQuery("None"),False)

	#def test_ParseQuery(self):


											
#class requesthandlerTest(unittest.TestCase):
	#def test_parseQuery(self):
unittest.main()