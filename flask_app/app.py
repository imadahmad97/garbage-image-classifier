from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import pickle

label_mapping = {
    0: 'compostable',
    1: 'recyclable',
    2: 'trash'
}

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
    img = Image.open(file)
    img_resized = img.resize((15, 15))
    img_array = np.array(img_resized)
    img_array_flattened = img_array.flatten()
    prediction = model.predict([img_array_flattened])
    category = label_mapping[prediction[0]]
    return category

if __name__ == '__main__':
    app.run(port=5003)