import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        connection_string = os.getenv("CosmosDBConnectionString")
        client = pymongo.MongoClient(connection_string)
        database = client['test']  
        collection = database['advertisements']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except Exception as e:
        return func.HttpResponse(f"Could not connect to MongoDB: {str(e)}", status_code=500)
