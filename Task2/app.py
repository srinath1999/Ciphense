from flask import Flask, render_template, redirect, url_for, request, jsonify
import numpy as np
from detect_faces import *
import os
import cv2
from imutils import build_montages


app = Flask(__name__)

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
	dir_path = request.form.get("dir_path")
	if dir_path:
		filePaths = ListAllFiles(myPath = dir_path)
		cwd = os.getcwd()
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
		n_len = int((n_faces**(1/2)) + 1)
		print()
		print(n_faces, "faces detected")
		print()
		montage = build_montages(faces, (int(500/n_len), int(500/n_len)), (int(n_len), int(n_faces/n_len+1)))
		cv2.imwrite(file_name, montage[0])
		return render_template("output.html")
	return redirect(url_for("index"))




