import cv2
import numpy as np
import glob

original = cv2.imread('images/nayan3.jpg')
# second_image = cv2.imread('images/nayan2.jpg')

rsz = (1200, 800)
resized_img = cv2.resize(original, rsz, interpolation=cv2.INTER_AREA)

sift = cv2.SIFT_create()
kp_1, desc_1 = sift.detectAndCompute(resized_img, None)

index_param = dict(algorithm=0, trees=5)
search_param = dict()
flann = cv2.FlannBasedMatcher(index_param, search_param)

# Load all the image
all_image_to_compare = []
titles = []
all_image = glob.iglob('images/*')

for f in all_image:
    image = cv2.imread(f)
    all_image_to_compare.append(image)
    titles.append(f)

for image_to_compare, title in zip(all_image_to_compare, titles):

    resized_img2 = cv2.resize(image_to_compare, rsz, interpolation=cv2.INTER_AREA)
    # 1) check if 2 images are equal
    if resized_img.shape == resized_img2.shape:
        # print('The image have same size and channel')
        difference = cv2.subtract(resized_img, resized_img2)
        b, g, r = cv2.split(difference)
        # cv2.imshow('difference', difference)
        # print(cv2.countNonZero(b))
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print('The images are completely equal')

    # 2) check for similarities between 2 images

    kp_2, desc_2 = sift.detectAndCompute(resized_img2, None)

    # print('ke point 1st image:', len(kp_1))
    # print('ke point 2nd image:', str(len(kp_2)))

    matches = flann.knnMatch(desc_1, desc_2, k=2)
    # print(len(matches))

    good_points = []
    for m, n in matches:
        if m.distance < 0.6 * n.distance:
            good_points.append(m)

    number_keypoints = 0
    if len(kp_1) <= len(kp_2):
        number_keypoints = len(kp_1)
    else:
        number_keypoints = len(kp_2)

    # print('good', len(good_points))
    print('Title', title)
    pecentages = len(good_points) / number_keypoints * 100
    print("how good it's the match " + str(int(pecentages)) + '%\n')
#     result = cv2.drawMatches(resized_img, kp_1, resized_img2, kp_2, good_points, None)
#
#     cv2.imshow('result', cv2.resize(result, None, fx=0.4, fy=0.4))
#     cv2.imshow('original', cv2.resize(resized_img, None, fx=0.4, fy=0.4))
#     cv2.imshow('others', cv2.resize(resized_img2, None, fx=0.4, fy=0.4))
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()
