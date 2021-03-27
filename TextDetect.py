import cv2
import easyocr
import os
from flask import Flask, jsonify

original = cv2.imread('images/japanese3.png')

reader = easyocr.Reader(['ja', 'en'], gpu=False)
result = reader.readtext(original)
s = 'without regret'
matched_word = []
total_detect = ''


def get_size(filename):
    fs = os.stat(filename)
    return fs.st_size


print('size:', get_size('images/japanese3.png'))


def is_match(text):
    for i in s.split():
        if i == text:
            matched_word.append(text)
            return True
    return False


# print(result[1][0])
for (b, t, p) in result:
    st = t.split()

    for tx in st:
        total_detect = total_detect + ' ' + tx
        print(tx)
        print(is_match(tx))
    # print(is_match(t))
    # unpack the bounding box
    (tl, tr, br, bl) = b
    tl = (int(tl[0]), int(tl[1]))
    tr = (int(tr[0]), int(tr[1]))
    br = (int(br[0]), int(br[1]))
    bl = (int(bl[0]), int(bl[1]))

    # cv2.rectangle(original, tl, br, (0, 255, 0), 2)
    # cv2.putText(original, t, (tl[0], tl[1] - 10),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    print('detect: ', total_detect)
    print(matched_word)
# cv2.imshow('result', original)
cv2.waitKey(0)

# app = Flask(__name__)
#
# course = {'results': es,
#           'id': "1"}
#
#
# @app.route('/texts', methods=['GET'])
# def get_data():
#     return jsonify({'res': course})
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
