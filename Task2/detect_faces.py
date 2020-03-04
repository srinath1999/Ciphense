import os
import numpy as np
import cv2
import json

def detect_faces(img):
	cwd_path = os.getcwd()
	prototxt_path = os.path.join(cwd_path,"Model/deploy_facerec.prototxt.txt")
	caffemodel_path = os.path.join(cwd_path, "Model/res10_300x300_ssd_iter_140000_facerec.caffemodel")
	net = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

	h, w = img.shape[:2]

	blob = cv2.dnn.blobFromImage(cv2.resize(img,(300, 300)), 1.0, (300, 300),(104.0, 177.0, 123.0))
	net.setInput(blob)
	detections = net.forward()

	faces = []
	n_faces = {}
	n_faces['face'] = 0
	for i in range(0, detections.shape[2]):
		confidence = detections[0,0,i,2]
		if confidence>0.5:
			face = {}
			box = detections[0,0,i,3:7]*np.array([w,h,w,h])
			(startX, startY, endX, endY) = box.astype("int")
			face['name'] = "face"
			face['startX'] = int(startX)
			face['startY'] = int(startY)
			face['endX'] = int(endX)
			face['endY'] = int(endY)
			faces.append(face)
			n_faces['face']+=1
			
	return [[n_faces], faces]
