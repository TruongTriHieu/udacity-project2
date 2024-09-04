import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    # Ví dụ URL gọi: http://localhost:7071/api/getAdvertisement/?id=5eb6cb8884f10e06dc6a2084

    id = req.params.get('id')
    logging.info(f"Received request for advertisement with id: {id}")
    
    if id:
        try:
            # Lấy chuỗi kết nối từ biến môi trường
            connection_string = os.getenv("CosmosDBConnectionString")
            client = pymongo.MongoClient(connection_string)
            database = client['test']  # Đặt tên cơ sở dữ liệu của bạn
            collection = database['advertisements']
           
            # Tìm kiếm document với _id được cung cấp
            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)

            if result:
                logging.info("Advertisement found, returning result.")
                result = dumps(result)
                return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
            else:
                logging.warning(f"No advertisement found with id: {id}.")
                return func.HttpResponse(f"No advertisement found with id: {id}.", status_code=404)

        except Exception as e:
            logging.error(f"Database connection error: {str(e)}")
            return func.HttpResponse("Database connection error.", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)
