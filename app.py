from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact-us')
def contact_us():
    return render_template('contact_us.html')

app.run()