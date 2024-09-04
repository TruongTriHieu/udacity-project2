import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    # Lấy 'id' từ query parameters
    id = req.params.get('id')

    if id:
        try:
            # Lấy chuỗi kết nối từ biến môi trường
            connection_string = os.getenv("CosmosDBConnectionString")
            client = pymongo.MongoClient(connection_string)
            database = client['test']  # Thay đổi tên cơ sở dữ liệu nếu cần
            collection = database['advertisements']

            # Tạo truy vấn để xóa document với _id được cung cấp
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)

            if result.deleted_count == 1:
                return func.HttpResponse(f"Advertisement with id {id} deleted successfully.", status_code=200)
            else:
                return func.HttpResponse(f"No advertisement found with id {id}.", status_code
