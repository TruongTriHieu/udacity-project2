import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Lấy chuỗi kết nối từ biến môi trường
        connection_string = os.getenv("CosmosDBConnectionString")
        client = pymongo.MongoClient(connection_string)
        database = client['NeighborlyDB']  # Thay đổi tên cơ sở dữ liệu nếu cần
        collection = database['advertisements']

        # Truy vấn tất cả tài liệu trong collection
        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except Exception as e:
        # Ghi lỗi để dễ dàng chẩn đoán vấn đề
        return func.HttpResponse(f"Could not connect to MongoDB: {str(e)}", status_code=500)
