Folder Overview:
	Model - Contains model information that is needed for object recognition and face recognition
	templates - Contains html files for input and output
	python files - contains the python code
		app.py - the main code
		detect_faces.py - contains a function that helps us to recognize face
		detect_objects.py - contains a function that helps us to recognize objects

Lib used:
	flask(v1.1.1)
	json
	numpy
	opencv
	os


How to use?
	1.Open terminal(Ctrl+Alt+T).
	2.Cd into this directory.
	3.Run command 'flask run'.
	4.Copy the local host address and paste it in the browser.
	5.Enter the path of the image(full path along with extension) and press submit.
	6.The required output is shown in json format.
		-The format of json is [[number of objects/faces/animals], [details regarding each of them]]
		-startX, startY, endX, endY -> starting and ending pixel values of the object in X and Y coordinates
		-name -> The type of object, either face, animal or object
