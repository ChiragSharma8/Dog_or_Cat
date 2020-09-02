import os
from flask import Flask, render_template, request, send_from_directory
from keras_preprocessing import image
from keras.models import load_model
import numpy as np
import tensorflow

app = Flask(__name__)


# path to the folder images will be stored
UPLOAD_FOLDER = 'uploads'

MODEL_FOLDER = 'models'

def predict(fullpath):
    classifier = load_model('./models/model.h5')
    test_image = image.load_img(fullpath, target_size=(256,256,3))
    test_image = image.img_to_array(test_image)
    test_image= np.expand_dims(test_image, axis = 0)
    predicitions = classifier.predict(test_image).flatten()

    return predicitions

#Home Page
@app.route('/')
def index():
    return render_template('index.html')

# process file and predict its label
@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        file = request.files['image']
        fullname = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(fullname)

        result = predict(fullname)

        pred_prob = result.item()

        if pred_prob > .5:
            label = 'DOG'
            accuracy = round(pred_prob * 100, 2)
        else:
            label = 'CAT'
            accuracy = round((1-pred_prob) * 100, 2)

        return render_template('predict.html', image_file_name = file.filename, label = label, accuracy = accuracy)

@app.route('/upload/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug =True)

