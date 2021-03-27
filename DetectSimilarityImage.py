from skimage.metrics import structural_similarity
import cv2

original = cv2.imread('images/nayan.jpg')
second_image = cv2.imread('images/laptop.jpg')


def orb_sim(img1, img2):
    orb = cv2.ORB_create()
    kp_1, desc_1 = orb.detectAndCompute(img1, None)
    kp_2, desc_2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = bf.match(desc_1, desc_2)

    similar_regions = [i for i in matches if i.distance < 50]
    # for i in matches:
    #     if i.distance < 50:
    #         similar_regions.append(i)

    if len(matches) == 0:
        return 0
    return len(similar_regions) / len(matches)


def structural_sim(img1, img2):
    rsz = (1200, 800)
    resize1 = cv2.resize(img1, rsz, interpolation=cv2.INTER_AREA)
    resize2 = cv2.resize(img2, rsz, interpolation=cv2.INTER_AREA)
    sim, diff = structural_similarity(resize1, resize2, full=True, multichannel=True)
    return sim


orb_similarity = orb_sim(original, second_image)

print('Similarity using ORB is:', int(orb_similarity * 100))

ssim = structural_sim(original, second_image)

print('Similarity using SSIM is:' + str(int(ssim * 100)) + '%')
