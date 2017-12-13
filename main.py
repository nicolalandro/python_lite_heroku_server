from flask import Flask, render_template

# webapp
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/add_supervisioned_data')
def add_supervisioned_data():
    return render_template('load_image.html')


if __name__ == '__main__':
    app.run()
