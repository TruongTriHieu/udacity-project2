#--------- Cài đặt Flask
SERVER_HOST = 'https://neighborly-e2avdrgaesdcamdx.southeastasia-01.azurewebsites.net/' 
SERVER_PORT = 5000 
FLASK_DEBUG = True 

SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'


# API_URL định dạng: "https://[FUNCTION_APP_NAME_GOES_HERE].azurewebsites.net/api"
# Cập nhật URL của Function App đã triển khai
API_URL = "https://myuniqueapp2024.azurewebsites.net/api"
# API_URL = "http://localhost:7071/api" # Bỏ comment dòng này để kiểm tra trên máy local
