import logging
import azure.functions as func
import pymongo
from bson.json_util import dumps
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        # Lấy chuỗi kết nối từ biến môi trường
        connection_string = os.getenv("CosmosDBConnectionString")
        client = pymongo.MongoClient(connection_string)
        database = client['test']  # Tên cơ sở dữ liệu của bạn
        collection = database['advertisements']

        # Truy vấn tất cả các tài liệu trong collection "posts"
        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)

    except Exception as e:
        logging.error(f"Error connecting to the database: {str(e)}")
        return func.HttpResponse("Bad request. Unable to connect to the database.", status_code=500)
