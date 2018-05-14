#horse images from
#https://unsplash.com/search/photos/horses

#dog images from
#https://www.kaggle.com/c/dogs-vs-cats/data

import cv2
import numpy as np
import os
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
def dog_or_horse(folder_mod,k):
    train_targets = []
    test_targets = []
    if folder_mod=='':
        img_file = 'dogs' + folder_mod + '/dog.0'  + '.jpg'
    else:
        img_file = 'dogs' + folder_mod + '/dog.0' + '.png'
    img_in = cv2.imread(img_file, 1)
    img_resized = cv2.resize(img_in, (255, 255))
    img_mat = np.asarray(img_resized)
    img_data_train = img_mat.flatten()
    img_data_test = img_mat.flatten()
    train_targets.append('dog')
    test_targets.append('dog')
    i = 0
    for filename in os.listdir('dogs'):
        img_in = cv2.imread('dogs/' + filename, 1)
        img_resized = cv2.resize(img_in, (255,255))
        img_mat = np.asarray(img_resized)
        img_data_tmp = img_mat.flatten()
        if i%6!=0:
            img_data_train = np.vstack([img_data_train, img_data_tmp])
            train_targets.append('dog')
        else:
            img_data_test = np.vstack([img_data_test, img_data_tmp])
            test_targets.append('dog')
        i = i+1
    for filename in os.listdir('horses'):
        img_in = cv2.imread('horses/' + filename, 1)
        img_resized = cv2.resize(img_in, (255,255))
        img_mat = np.asarray(img_resized)
        img_data_tmp = img_mat.flatten()
        if i%6!=0:
            img_data_train = np.vstack([img_data_train, img_data_tmp])
            train_targets.append('horse')
        else:
            img_data_test = np.vstack([img_data_test, img_data_tmp])
            test_targets.append('horse')
        i = i+1
    #print(np.array(test_targets))
    train = img_mat.flatten()
    tgt = ['dog']
    for j in range(len(train_targets)/2):
        train = np.vstack([train, img_data_train[j,:]])
        tgt.append('dog')
        train = np.vstack([train, img_data_train[len(train_targets)-j-1,:]])
        tgt.append('horse')
    #ml = svm.SVC(gamma=0.001, C=100.)
    ml = KNeighborsClassifier(n_neighbors=k)
    ml.fit(train, np.array(tgt))
    return (ml.predict(img_data_test), test_targets)

def run_ml(k):
    results1, target = dog_or_horse('',k)
    results2, target2 = dog_or_horse('_png_nn1',k)
    results3, target3 = dog_or_horse('_png_nn2',k)
    right = 0
    wrong = 0
    dright = 0
    dwrong = 0
    hright = 0
    hwrong = 0
    #print len(target)
    #print results1.shape
    for i in range(len(target)):
        count = 0
        if results1[i]==target[i]:
            count = count + 1
        if results2[i]==target[i]:
            count = count + 1
        if results3[i]==target[i]:
            count = count + 1
        if count>=2:
            right = right + 1
            if target[i] == 'dog':
                dright = dright + 1
            else:
                hright = hright + 1
        else:
            wrong = wrong + 1
            if target[i] == 'dog':
                dwrong = dwrong + 1
            else:
                hwrong = hwrong + 1
    print 'Accuracy for k=' + str(k) + ': ' + str(right/(1.0 * (wrong + right)))
    print 'Dog accuracy for k=' + str(k) + ': ' + str(dright / (1.0 * (dwrong + dright)))
    print 'Horse accuracy for k=' + str(k) + ': ' + str(hright / (1.0 * (hwrong + hright)))

run_ml(1)
run_ml(5)
run_ml(10)
run_ml(20)


