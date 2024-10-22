import os
import cv2
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)


@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
    image_file = request.files['file']
    height = int(request.form['height'])
    width = int(request.form['width'])

    filename = secure_filename(image_file.filename)
    image_path = os.path.join('static/', filename)
    image_file.save(image_path)
    
    image = Image.open(image_path)
    image.thumbnail((width, height))  # Resizes in place
    resized_image_path = os.path.join('static/', 'resized_' + filename)
    image.save(resized_image_path)  # Save the resized image

    return render_template('upload.html', filename='resized_' + filename)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename=filename))


if __name__ == "__main__":
    app.run()
