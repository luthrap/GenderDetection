import numpy as np
import cv2 as cv
import sys
import os
import shutil


def detectFaceFromFile(imgLocation,imgName):
    inputImage = cv.imread(imgLocation + '/' + imgName)
    try:
        gray = cv.cvtColor(inputImage,cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            return inputImage[y:y+h,x:x+w]
    except:
        return None

def detectFaceFromArray(img):
    try:
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            return img[y:y+h,x:x+w]
    except:
        return None

def resizeImageFromFile(imgLocation,imgName):
    inputImage = cv.imread(imgLocation + '/' + imgName)
    print 'Exact Location' + imgLocation + "/" + imgName
    try:
        gray = cv.cvtColor(inputImage, cv.COLOR_BGR2GRAY)
        resizedImg = cv.resize(gray,(112,92))
        return resizedImg
    except:
        return None

def resizeImageFromArray(img):
        try:
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            resizedImg = cv.resize(gray,(112,92))
            return resizedImg
        except:
            return None

configPath = sys.argv[1]
face_cascade = cv.CascadeClassifier(configPath + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(configPath + 'haarcascade_eye.xml')
trainingImgPath = sys.argv[2]


print '****----Training Starts----****'
(images, lables, names, id) = ([], [], {}, 0)


try:
    shutil.rmtree(trainingImgPath + "/" + "Output")
except:
    print "No output directory found to delete"
os.mkdir(trainingImgPath + "/" + "Output")

for (root, subdirs, files) in os.walk(trainingImgPath):
    for subdir in subdirs:
        print "Dir : " + subdir
        if(subdir == 'Male' or subdir == 'Female'):
            subjectpath = os.path.join(trainingImgPath, subdir) 
            print "Subject Path : " + subjectpath
            for filename in os.listdir(subjectpath):
                path = subjectpath + '/' + filename
                #normalizedImage = resizeImage(subjectpath,filename)
                normalizedImageTemp = detectFaceFromFile(subjectpath,filename)
                if(normalizedImageTemp is not None):
                    print "Temp File is fine"
                    normalizedImage = resizeImageFromArray(normalizedImageTemp)
                    if(normalizedImage is not None):
                        print "Final File is fine"
                        images.append(normalizedImage)
                        print "Writing to file"
                        cv.imwrite(trainingImgPath + "/Output/" + filename,normalizedImage)
                        if(subdir == 'Male'):
                            lables.append(0)
                        else:
                            lables.append(1)

(images, lables) = [np.array(lis) for lis in [images, lables]]
model = cv.face_FisherFaceRecognizer.create()
model.train(images,lables)

inputSource = sys.argv[3]
img = cv.imread(inputSource)

if(inputSource == '0'):
    c = cv.VideoCapture(0)
    while(1):
        _,f = c.read()
        gray = detectFaceFromArray(f)
        if(gray is None):
            continue
        resizedImage = resizeImageFromArray(gray)
        if(resizedImage is None):
            continue
        prediction,_ = model.predict(resizedImage)
        if(prediction == 0):
            print("The Image is of Male")
        elif(prediction == 1):
            print("The Image is of Female")
        else:
            print("The Image is Undetermined")
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cv.destroyAllWindows()
    c.release()

else:
    gray = detectFaceFromArray(img)
    prediction,_ = model.predict(resizeImageFromArray(gray))
    if(prediction == 0):
        print("The Image is of Male")
    elif(prediction == 1):
        print("The Image is of Female")
    else:
        print("The Image is Undetermined")