# Attendence-Management-system using face recognition
Attendence Management System using Face Recognition as a part of Collage Mini Project
***********************************************************************************
How to run the project:

•	Download or clone the Repository to your device.

•	Open the command prompt and type "pip install -r requirements.txt" to install the required packages for the project.

•	create folders of named as TrainingImage and Attendence respectively.

•	Open "attendance.py" and "automaticAttendance.py" and change all the path according to your system.

•	Create the folders for subjects we require to take attendance in the "Attendence" folder.

•	Run "attendance.py" file to register your face so that the system can identify you. 

 **************************************************************************************
The project workflow can be described as follows:

•	Click on "Register New Student" and a small window will pop up where you have to enter your ID and name. Then click on the "Take Image" button to capture your face. A camera window will pop up and take up to 100 images (you can change the number of images it can take) and store them in the "TrainingImage" folder.

•	Click on the "Train Image" button to train the model and convert all the images into a numeric format so that the computer can understand them. The system will take some time to complete the training, depending on your system.

•	After training the model, click on "Automatic Attendance". Enter the subject name, and the system will fill in attendance by recognizing your face using the trained model. It will create a separate .csv file for every subject you enter.

•	You can view the attendance record in tabular format by clicking on the "View Attendance" button.

************************************************************************************
Requirements of the system:

•	Python 3.6+

•	Ram minimum : 8gb

•	4gb Graphic Card

•	your Operating System should Support the required modules.

1.	Opencv	(pip install opencv-python)
2.	Tkinter	(Available in python)
3.	PIL 	          (pip install Pillow)
4.	Pandas.      (pip install pandas)
5.	Numpy.      (pip install numpy)
6.	Pillow         (pip install Pillow)

•	haarcascade_frontalface_default.xml
1.	The folder "haarcascades" contains pre-trained classifiers for detecting specific types of objects such as faces (frontal and profile) and pedestrians. Some of the classifiers may have unique licenses that require further investigation.
            https://github.com/opencv/opencv/tree/master/data/haarcascades

•	The quality of images is crucial as it can impact the accuracy of the system by introducing noise.


For any more explaination a pdf of report f my project is attached along with project files(Facerecognitiom_Report.pdf).

Follow and give a Star if you like my project.
*************************************************************************************** 

Basic Layyout or GUI of the project:

<img width="524" alt="image" src="https://user-images.githubusercontent.com/76565982/235320755-90fdb8de-ad67-4de0-af16-941f67837c90.png">

<img width="524" alt="image" src="https://user-images.githubusercontent.com/76565982/235320784-583f51d3-4c05-4aeb-998f-c141867335c9.png">

<img width="523" alt="image" src="https://user-images.githubusercontent.com/76565982/235320807-9f31f8a3-67d5-4220-b13e-9a16527ae365.png">





