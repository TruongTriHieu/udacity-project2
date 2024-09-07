#--------- Cài đặt Flask
SERVER_HOST = '0.0.0.0' 
SERVER_PORT = 8080 
FLASK_DEBUG = False 

# Cài đặt Flask-Restplus
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'

#-------- Các hằng số của Azure

# API_URL định dạng: "https://[FUNCTION_APP_NAME_GOES_HERE].azurewebsites.net/api"
# Cập nhật URL của Function App đã triển khai
API_URL = "https://myuniqueapp2024.azurewebsites.net/api"
# API_URL = "http://localhost:7071/api" # Bỏ comment dòng này để kiểm tra trên máy local
