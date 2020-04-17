from cv2 import cv2
import sys
import os.path

def detect(filename, s, cascade_file = "../lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)
    try:
        print('trying image {}'.format(s))
        cascade = cv2.CascadeClassifier(cascade_file)
        image = cv2.imread(filename, cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        
        faces = cascade.detectMultiScale(gray,
                                        # detector options
                                        scaleFactor = 1.1,
                                        minNeighbors = 5,
                                        minSize = (24, 24))
        for (x, y, w, h) in faces:
            #cv2.rectangle(image, (x-w//4, y-w//4), (x + 5*w//4, y + 5*h//4), (0, 0, 255), 2)
            out = image[y-21:y+107,x-21:x+107]
            #out = image[y-42:y+214,x-42:x+214]
        #cv2.imshow("AnimeFaceDetect", image)
        #cv2.waitKey(0)
        cv2.imwrite("cropped/{}.jpg".format(s), out)
        print('success!')
    except:
        print('one pic error!')

for i in range(1,47050):
    string = str(i).zfill(5)
    detect(filename = '../../illustration2vec/images/{}.jpg'.format(string),s=string)

