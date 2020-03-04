Folder Overview:
	Model - Contains model information that is needed face recognition
	templates - Contains html files for input and output
	static - contains the collage image in .jpg form
	python files - contains the python code
		app.py - the main code
		detect_faces.py - contains a function that helps us to recognize face

Lib used:
	flask(v1.1.1)
	json
	numpy
	opencv
	os
	imutils


How to use?
	1.Open terminal(Ctrl+Alt+T).
	2.Cd into this directory.
	3.Run command 'flask run'.
	4.Copy the local host address and paste it in the browser.
	5.Enter the path of the directory in which the images are present(full path along of the directory) and press submit.
	6.The collage will be shown at the output
		-If the app is run multiple times, then the output shown might be sometimes the previous output, but on refreshing the page the correct output is shown.