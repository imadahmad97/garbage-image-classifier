from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import pickle

app = Flask(__name__)

with open('flask_app/test_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/how-it-works')
def how_it_works():
    return render_template('how_it_works.html')

@app.route('/about-us')
def about_us():
    return render_template('about_us.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    how_it_works()

if __name__ == '__main__':
    app.run(port=5003)