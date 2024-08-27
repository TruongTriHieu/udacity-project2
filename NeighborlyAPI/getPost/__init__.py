import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Lấy ID từ tham số truy vấn
    id = req.params.get('id')

    if id:
        try:
            # Lấy chuỗi kết nối từ biến môi trường
            connection_string = os.getenv("CosmosDBConnectionString")
            client = pymongo.MongoClient(connection_string)
            database = client['NeighborlyDB']  # Thay đổi tên cơ sở dữ liệu nếu cần
            collection = database['posts']

            query = {'_id': ObjectId(id)}
            result = collection.find_one(query)
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except Exception as e:
            # Ghi lỗi để dễ dàng chẩn đoán vấn đề
            return func.HttpResponse(f"Database connection error: {str(e)}", status_code=500)

    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)
