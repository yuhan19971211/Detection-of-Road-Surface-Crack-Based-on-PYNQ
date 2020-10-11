# coding=utf-8
import cv2
import datetime
import numpy as np
import skimage.io as io
from skimage import data_dir
from matplotlib import pyplot as plt
str= '*.jpg'
coll=io.ImageCollection(str)

number=[0]*len(coll)

for i in range(1,len(coll)):
    r1 = cv2.pyrDown(coll[i])
    r2 = cv2.pyrDown(r1)
    r3 = cv2.pyrDown(r2)
    GrayImage = cv2.cvtColor(r3, cv2.COLOR_BGR2GRAY)
    dst = cv2.GaussianBlur(GrayImage, (5, 5), 0, 0)  # 高斯模糊
    img = dst
    cv2.imshow("yuzhichuli", img)

    cv2.waitKey(0)
    ret, thresh5 = cv2.threshold(img, 145, 255, cv2.THRESH_TOZERO_INV)
    # cv2.imshow("yuzhichuli",thresh5)
    # cv2.waitKey(0)
    k = np.ones((4, 4), np.uint8)
    erosion = cv2.morphologyEx(thresh5, cv2.MORPH_OPEN, k)
    k_close = np.ones((4, 4), np.uint8)
    Erosion = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, k_close)
    cv2.imshow("xingtaixueyunsuan",Erosion)
    cv2.waitKey(0)
    #----------------------------------------------------------------------------#
    # brisk = cv2.BRISK_create()
    # keypoints = brisk.detect(Erosion, None)
    # print ("特征值识别第一步进行中")
    # # ------------------------识别步骤2------------------------------#
    # print ("特征值识别第二部进行中")
    # img2 = Erosion
    # img2 = cv2.drawKeypoints(Erosion, keypoints, img2, color=(0, 255, 0))
    # cv2.imshow('Detected BRISK keypoints', img2)
    # cv2.waitKey(0)
    #------------------------------------------------------------------------#
    # starttime = datetime.datetime.now()
    # fast = cv2.FastFeatureDetector_create(50)
    # kp = fast.detect(Erosion,None)
    # img2 = cv2.drawKeypoints(Erosion, kp, (0, 255, 0 ))
    # endtime = datetime.datetime.now()
    # a = endtime - starttime
    # print('number=', len(kp))
    # number[i]=len(kp)
    # ava = np.sum(dst) / np.size(dst)
    # print('average=',ava)
    # cv2.namedWindow('fast', cv2.WINDOW_NORMAL)
    #
    # cv2.imshow('fast', img2)
    # cv2.waitKey(0)
    # if len(kp) >= 45 and len(kp)<=145:
    #     print('have')
    # else:
    #     print('No')
    # print '#----------------------------------------------#'

# print all_number/len(coll)
    fast = cv2.FastFeatureDetector_create(threshold=70,nonmaxSuppression=True,type=cv2.FAST_FEATURE_DETECTOR_TYPE_9_16)
    keypoints = fast.detect(Erosion,None)
    print ("nonmaxSuppression: ", fast.getNonmaxSuppression())
    print('FastFeatureDetector_create')
    # print len(keypoints)
    # if len(keypoints) >= 80:
    #     print('have')
    # else:
    #     print('No')
    # 必须要先初始化img2
    img2 = Erosion
    img2 = cv2.drawKeypoints(img2, keypoints, img2, color=(0, 255, 0))
    cv2.imshow('Detected FAST keypoints', img2)
    cv2.waitKey(0)