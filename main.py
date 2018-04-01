import os
from unittest.mock import MagicMock

from flask import Flask, render_template, jsonify, request

from src.cloud_image_loader import CloudImageLoader

# webapp
app = Flask(__name__)


def create_cloud_image_load():
    if "test" in os.environ:
        mock = MagicMock()
        mock.get_dataset_list = []
        mock.get_data_file = MagicMock(side_effect=(lambda x, y: "{'img':'data:image/png;base64','name':'0.json','specie':'test'}"))
        mock.add_file = MagicMock(side_effect=lambda x: [])
        return mock
    else:
        uname = os.environ['pcloud_uname']
        password = os.environ['pcloud_password']
        return CloudImageLoader(uname, password)


cloud_image_loader = create_cloud_image_load()


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/add_supervisioned_data')
def add_supervisioned_data():
    return render_template('load_image.html')


@app.route('/show_dataset')
def show_dataset():
    posts = cloud_image_loader.get_dataset_list
    return render_template('show_dataset.html', posts=posts)


@app.route('/fish_ai')
def use_fish_ai():
    return render_template('fish_ai.html')


@app.route('/api/load_image_to_cloud', methods=['POST'])
def load_image_to_cloud():
    json_content = str(request.get_json())
    return jsonify(cloud_image_loader.add_file(json_content))


@app.route('/api/load_data_from_cloud', methods=['POST'])
def load_data_from_cloud():
    json_request = request.get_json()
    name = json_request['name']
    size = json_request['size']
    return jsonify(cloud_image_loader.get_data_file(name, size))


if __name__ == '__main__':
    app.run()
