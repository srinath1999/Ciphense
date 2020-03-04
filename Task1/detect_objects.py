import os
import numpy as np
import cv2
import json

def detect_objects(img):
	cwd_path = os.getcwd()
	prototxt_path = os.path.join(cwd_path, "Model/MobileNetSSD_deploy.prototxt.txt")
	caffemodel_path = os.path.join(cwd_path, "Model/MobileNetSSD_deploy.caffemodel")
	
	objects = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

	box_color = np.random.uniform(0, 255, size=(len(objects), 3))

	net = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)
	h, w = img.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 0.007843, (300, 300), 127.5)

	net.setInput(blob)
	detections = net.forward()

	object_list = []
	n_objects = {}
	for i in objects:
		n_objects[i] = 0

	for i in np.arange(0, detections.shape[2]):

		confidence = detections[0,0,i,2]

		if confidence>0.2:
			obj = {}
			idx = int(detections[0,0,i,1])
			box = detections[0,0,i,3:7]*np.array([w,h,w,h])

			(startX, startY, endX, endY) = box.astype("int")
			obj['name'] = objects[idx]
			obj['startX'] = int(startX)
			obj['startY'] = int(startY)
			obj['endX'] = int(endX)
			obj['endY'] = int(endY)
			object_list.append(obj)

			n_objects[objects[idx]]+=1
	return [[n_objects], object_list]