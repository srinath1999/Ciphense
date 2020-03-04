from flask import Flask, render_template, redirect, url_for, request, jsonify
from detect_objects import *
from detect_faces import *
import cv2
import numpy as np
import os
import json

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/getImageDetails", methods = ["POST"])
def output():
	img_path = request.form.get("img_path")
	if img_path:
		print(img_path)
		lst1 = detect_objects(cv2.imread(img_path))
		lst2 = detect_faces(cv2.imread(img_path))
		lst1[0][0]['face'] = lst2[0][0]['face']
		for i in lst2[1]:
			lst1[1].append(i)
		print(lst1)


		json_data = json.dumps(lst1)

		return render_template("output.html", json_data = json_data)
	return redirect(url_for("index"))
	