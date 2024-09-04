import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        connection_string = os.getenv("CosmosDBConnectionString")  
        client = pymongo.MongoClient(connection_string)
        database = client['NeighborlyDB']  
        collection = database['advertisements']

        request = req.get_json()

        if request:
            collection.insert_one(request)

            return func.HttpResponse(json.dumps(request), mimetype="application/json", charset='utf-8')

        else:
            return func.HttpResponse(
                "Please pass valid data in the body",
                status_code=400
            )

    except Exception as e:
        return func.HttpResponse(f"Could not connect to MongoDB: {str(e)}", status_code=500)