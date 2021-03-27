from flask import Flask, jsonify, make_response, request, render_template, redirect
import cv2
import easyocr
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

s = 'without regret'
matched_word = ''
detect_txt = ''


def is_match(text):
    for i in s.split():
        if i == text:
            global matched_word
            matched_word = matched_word + ' ' + text
            return True
    return False


def detect_text(image):
    total_detect_word = ''
    total_detect_matched_word = ''
    st = ''
    reader = easyocr.Reader(['ja', 'en'], gpu=False)
    result = reader.readtext(image)
    for (b, t, p) in result:
        st = t.split()
        for tx in st:
            total_detect_word = total_detect_word + tx + ' '
            print(tx)
            if is_match(tx):
                total_detect_matched_word = total_detect_matched_word + tx + ' '

    #
    # print('image result:', es)
    return total_detect_matched_word
    # return total_detect_word


# print(detect_text(cv2.imread('images/japanese3.png')))


@app.route('/')
def index():
    return 'Welcome to the course api'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': error}), 404)


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(ROOT_DIR + '\\files'):
    os.makedirs('files')

app.config['IMAGE_UPLOADS'] = ROOT_DIR + '\\files'
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ['PNG', 'JPG', 'JPEG', 'GIF']
app.config['MAX_IMAGE_FILESIZE'] = 0.5 * 1024 * 1024


def get_size(filename):
    fs = os.stat(filename)
    return fs.st_size


def allowed_image(filename):
    if not '.' in filename:
        return False
    ext = filename.rsplit('.', 1)[1]
    if ext.upper() in app.config['ALLOWED_IMAGE_EXTENSIONS']:
        return True
    else:
        return False


def allowed_image_file_size(file_size):
    if int(file_size) <= app.config['MAX_IMAGE_FILESIZE']:
        return True
    else:
        return False


@app.route('/api/detect-text', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if request.files:
            image = request.files['image']
            if image.filename == '':
                print('File note selected')
                # return redirect(request.url)
                return jsonify({'message': 'File note selected'})
            if not allowed_image(image.filename):
                print('That image extension is not allowed')
                # return redirect(request.url)
                return jsonify({'message': 'That image extension is not allowed'})
            else:
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config['IMAGE_UPLOADS'], filename))
                global detect_txt
                detect_txt = detect_text(cv2.imread('files/' + filename))
                print('file size: ', get_size('files/' + filename))
                if detect_txt == '':
                    return jsonify({'message': 'No data found'})

        return jsonify({'message': detect_txt})
        # return redirect(request.url)
    return render_template('upload_image.html')


if __name__ == '__main__':
    app.run(debug=True)
