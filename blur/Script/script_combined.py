import cv2
import os
import random
import math

test_or_train = ['test', 'train']
cat_or_dog = ['CAT', 'DOG']
directory = '../normal/CATS_DOGS'
dump = 'CATS_DOGS_blur_combined'
color = (0, 0, 0)


for t in test_or_train:
    for cd in cat_or_dog:
        num = 1
        for fn in os.listdir(directory+'/'+t+'/'+cd):
            image = cv2.imread(os.path.join(directory+'/'+t+'/'+cd, fn))
            if image is not None:

                h, w = image.shape[0:2]

                sizeH = math.ceil(h / math.sqrt(10))
                sizeW = math.ceil(w / math.sqrt(10))

                rh = random.randint(0, h - sizeH)
                rw = random.randint(0, w - sizeW)

                blurred_part = cv2.blur(image[rh:rh + sizeH, rw:rw + sizeW], ksize=(15, 15), )
                blurred = image.copy()
                blurred[rh:rh + sizeH, rw:rw + sizeW] = blurred_part

                cv2.imwrite(os.path.join(dump+'/'+t+'/'+cd, t+cd+"T"+str(num)+'.jpg'), blurred)
                cv2.imwrite(os.path.join(dump+'/'+t+'/'+cd, t+cd+"N"+str(num)+'.jpg'), image)

                num += 1
