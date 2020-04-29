from flask_restful import Resource 
import flask_restful.reqparse as parserrequest
import getcountrydata
import json
import os
cachedData = {}

class requesthandler(Resource):
    def get(self,country):
        parsedQuery = ParseQuery()
        if CheckNullQuery(parsedQuery) == False :
            dat = country + "," + parsedQuery
            if dat in cachedData:
                return cachedData[dat]

        obj = getcountrydata.getdata(country)
        if CheckNullQuery(obj):
            return "404 Country Not found"
        
        if CheckNullQuery(parsedQuery) or parsedQuery == "" :
            cachedData[dat] = obj
            return obj

        splitted = parsedQuery.split(",")
        result = {}
        for info in splitted:
            if info in obj : 
                result[info] = obj[info]
            else :
                result[info] = "invalid"
        cachedData[dat] = result
        return result

def CheckNullObj(object):
    if object == None:
        return True
    return False

def CheckNullQuery(query):
    if query == None:
        return True
    return False


def ParseQuery():        
    parser = parserrequest.RequestParser()
    parser.add_argument("info")  
    args = 	parser.parse_args()
    return args["info"]

