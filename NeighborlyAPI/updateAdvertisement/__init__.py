import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import os
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:

    # Lấy 'id' từ query parameters
    id = req.params.get('id')
    try:
        request = req.get_json()
    except ValueError:
        return func.HttpResponse('Invalid JSON input.', status_code=400)

    if id and request:
        try:
            # Lấy chuỗi kết nối từ biến môi trường
            connection_string = os.getenv("CosmosDBConnectionString")
            client = pymongo.MongoClient(connection_string)
            database = client['test']  # Đặt tên cơ sở dữ liệu của bạn
            collection = database['advertisements']
            
            # Tạo bộ lọc và câu truy vấn cập nhật
            filter_query = {'_id': ObjectId(id)}
            update_query = {"$set": request}

            # Thực hiện cập nhật
            result = collection.update_one(filter_query, update_query)

            if result.matched_count == 1:
                return func.HttpResponse(f"Advertisement with id {id} updated successfully.", status_code=200)
            else:
                return func.HttpResponse(f"No advertisement found with id {id}.", status_code=404)

        except Exception as e:
            logging.error(f"Could not connect to MongoDB: {str(e)}")
            return func.HttpResponse('Could not connect to MongoDB.', status_code=500)
    else:
        return func.HttpResponse('Please provide both an id in the query string and valid JSON body.', status_code=400)
