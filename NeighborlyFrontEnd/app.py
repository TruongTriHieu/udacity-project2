import logging.config
import os
from flask import Flask, Blueprint, request, jsonify, render_template, redirect, url_for, make_response, send_from_directory
from flask_bootstrap import Bootstrap
import settings
import requests
import json
from feedgen.feed import FeedGenerator
from urllib.parse import urljoin

app = Flask(__name__)
Bootstrap(app)

def get_abs_url(url):
    """ Returns absolute url by joining post url with base url """
    return urljoin(request.url_root, url)

@app.route('/')
def home():
    response = requests.get(settings.API_URL + '/getAdvertisements')
    if response.status_code == 200:
        ads = response.json()
    else:
        ads = []

    response_posts = requests.get(settings.API_URL + '/getPosts')
    if response_posts.status_code == 200:
        posts = response_posts.json()
    else:
        posts = []

    return render_template('index.html', ads=ads, posts=posts)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/ad/add', methods=['GET'])
def add_ad_form():
    # Hiển thị form để thêm quảng cáo mới, sử dụng template `new_ad.html`
    return render_template('new_ad.html')

@app.route('/ad/<id>', methods=['GET'])
def view_ad(id):
    # Lấy thông tin quảng cáo từ API và hiển thị
    response = requests.get(settings.API_URL + f'/getAdvertisement?id={id}')
    if response.status_code == 200:
        ad = response.json()
        return render_template('view_ad.html', ad=ad)
    else:
        return jsonify({"error": "Advertisement not found"}), 404

@app.route('/ad/edit/<id>', methods=['GET', 'POST'])
def edit_ad(id):
    # Lấy thông tin quảng cáo và hiển thị form chỉnh sửa
    # Xử lý POST request để cập nhật quảng cáo
    if request.method == 'POST':
        # Code để cập nhật quảng cáo
        pass
    response = requests.get(settings.API_URL + f'/getAdvertisement?id={id}')
    if response.status_code == 200:
        ad = response.json()
        return render_template('edit_ad.html', ad=ad)
    else:
        return jsonify({"error": "Advertisement not found"}), 404

@app.route('/ad/new', methods=['GET', 'POST'])
def add_ad_request():
    if request.method == 'POST':
        req_data = {
            'title': request.form['title'],
            'city': request.form['city'],
            'description': request.form['description'],
            'email': request.form['email'],
            'imgUrl': request.form['imgUrl'],
            'price': request.form['price']
        }
        response = requests.post(settings.API_URL + '/createAdvertisement', json=req_data)
        return redirect(url_for('home'))
    else:
        # Nếu là GET request, render trang new_ad.html
        return render_template('new_ad.html')

@app.route('/feeds/')
def feeds():
    fg = FeedGenerator()
    fg.title('All Advertisements feed')
    fg.link(href=request.url_root)
    
    response = requests.get(settings.API_URL + '/getAdvertisements')
    if response.status_code == 200:
        posts = response.json()
        # Thêm các post vào feed
        for post in posts:
            fe = fg.add_entry()
            fe.title(post.get('title', 'No title'))
            fe.author(name=post.get('author_name', 'Anonymous'))
            fe.link(href=get_abs_url(post.get('url', '')))
            fe.updated(post.get('mod_date'))
            fe.published(post.get('created_date'))
        return make_response(fg.atom_str(pretty=True), 200, {'Content-Type': 'application/atom+xml'})
    else:
        return jsonify({"error": "Unable to fetch advertisements"}), 500

@app.route('/rss')
def rss():
    fg = FeedGenerator()
    fg.title('Feed title')
    fg.description('Feed Description')
    fg.link(href='https://neighborly-client-v1.azurewebsites.net/')
    
    response = requests.get(settings.API_URL + '/getAdvertisements')
    if response.status_code == 200:
        ads = response.json()
        for a in ads: 
            fe = fg.add_entry()
            fe.title(a.get('title', 'No title'))
            fe.description(a.get('description', 'No description'))
        
        response = make_response(fg.rss_str(pretty=True))
        response.headers.set('Content-Type', 'application/rss+xml')
        return response
    else:
        return jsonify({"error": "Unable to fetch advertisements"}), 500

# Chạy ứng dụng
def main():
    print(' ----->>>> Flask Python Application running in development server')
    app.run(host=settings.SERVER_HOST, port=settings.SERVER_PORT, debug=settings.FLASK_DEBUG)

if __name__ == '__main__':
    main()
