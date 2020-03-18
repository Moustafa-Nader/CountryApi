from flask_restful import Resource 
import flask_restful.reqparse as parserrequest
import getcountrydata
class requesthandler(Resource):
    
    def get(self,country ):
        obj = getcountrydata.getdata(country)
        parsedQuery = ParseQuery()
        if parsedQuery == None :
            return obj
        splitted = parsedQuery.split(",")
        result = {}
        for info in splitted:
            if info in obj : 
                result[info] = obj[info]
            else :
                result[info] = "invalid"
        return result

def ParseQuery():        
        parser = parserrequest.RequestParser()
        parser.add_argument("info")  
        args = 	parser.parse_args()
        return args["info"]

        

