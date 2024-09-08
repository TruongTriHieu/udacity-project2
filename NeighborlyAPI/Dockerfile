# Sử dụng Python 3.8 làm base image
FROM python:3.8-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép các file requirements vào thư mục làm việc và cài đặt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn ứng dụng vào thư mục làm việc
COPY . /app

# Expose cổng mà ứng dụng Flask sẽ chạy (đã thay đổi thành 5000)
EXPOSE 5000

# Thiết lập biến môi trường Flask (nếu cần)
ENV FLASK_APP=app.py

# Chạy ứng dụng Flask (thay đổi phương thức chạy)
CMD ["python", "app.py"]
