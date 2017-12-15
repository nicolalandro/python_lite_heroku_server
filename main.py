from flask import Flask, render_template

# webapp
from src.cloud_image_loader import CloudImageLoader

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/add_supervisioned_data')
def add_supervisioned_data():
    return render_template('load_image.html')


@app.route('/fish_ai')
def use_fish_ai():
    return render_template('fish_ai.html')

@app.route('/api/load_image_to_cloud')
def load_image_to_cloud():
    return CloudImageLoader().load_image()


if __name__ == '__main__':
    app.run()
