from flask import Flask, render_template, jsonify, request, json

# webapp
from src.cloud_image_loader import CloudImageLoader

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/add_supervisioned_data')
def add_supervisioned_data():
    return render_template('load_image.html')


@app.route('/show_dataset')
def show_dataset():
    posts = CloudImageLoader().get_dataset_list
    return render_template('show_dataset.html', posts=posts)


@app.route('/fish_ai')
def use_fish_ai():
    return render_template('fish_ai.html')


@app.route('/api/load_image_to_cloud', methods=['POST'])
def load_image_to_cloud():
    json_content = str(request.get_json())
    return jsonify(CloudImageLoader().add_file(json_content))


@app.route('/api/load_data_from_cloud', methods=['POST'])
def load_data_from_cloud():
    json_request = request.get_json()
    name = json_request['name']
    size = json_request['size']
    return jsonify(CloudImageLoader().get_data_file(name, size))


if __name__ == '__main__':
    app.run()
