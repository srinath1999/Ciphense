from flask import Flask, render_template, redirect, url_for, request, jsonify
import numpy as np
from detect_faces import *
import os
import cv2
from imutils import build_montages


app = Flask(__name__)


#This function is used to list all files inside the folder
#The directory should only contain images not any other files
def ListAllFiles ( myPath):

	filePaths = []

	for root, dirs, files in os.walk(myPath) :
		for file in files:
			filePaths.append(os.path.join(root, file))

	return filePaths


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/createCollage", methods = ["POST"])
def output():
	#Taking the directory path as input
	dir_path = request.form.get("dir_path")
	if dir_path:
		filePaths = ListAllFiles(myPath = dir_path)
		cwd = os.getcwd()
		#The collage will be saved in static folder as collage.jpg
		file_name = "static/collage.jpg"
		faces = []
		n_faces = 0
		for image_path in filePaths:
			img = cv2.imread(image_path)
			face_data = detect_faces(img)
			n_faces += face_data[0][0]['face']
			for i in range(0, face_data[0][0]['face']):
				face = img[face_data[1][i]['startY']:face_data[1][i]['endY'], face_data[1][i]['startX']:face_data[1][i]['endX']]
				faces.append(face)
		#number of images in a row
		n_len = int((n_faces**(1/2)) + 1)
		print()
		print(n_faces, "faces detected")
		print()
		#Trying to create a collage of size 500X500 so each face should be resized to 500/n_len
		#Number of images in col = n_len and in row is taken to be int(n_faces/n_len+1), +1 is added to eliminate any corner cases
		#so that all images are present in the collage
		montage = build_montages(faces, (int(500/n_len), int(500/n_len)), (int(n_len), int(n_faces/n_len+1)))
		#Image is stored at static as collage.jpg
		cv2.imwrite(file_name, montage[0])
		return render_template("output.html")
	return redirect(url_for("index"))




