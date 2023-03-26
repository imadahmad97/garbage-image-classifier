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
    img_resized = file.resize((15, 15)) # resize image
    img_array = np.array(img_resized) # convert image to numpy array
    img_array_flattened = img_array.flatten() # flatten numpy array
    prediction = model.predict([img_array_flattened]) # pass flattened array to model's predict method
    return str(prediction[0]) # return predicted result to user as string

if __name__ == '__main__':
    app.run(port=5003)