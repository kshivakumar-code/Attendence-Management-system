import csv
import os
import cv2
import numpy as np
import pandas as pd
import datetime
import time
from PIL import ImageTk, Image

# Train Image
def TrainImage(haarcasecade_path, trainimage_path, trainimagelabel_path, message,text_to_speech):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(haarcasecade_path)
    faces, Id = getImagesAndLables(trainimage_path)
    recognizer.train(faces, np.array(Id))
    recognizer.save(trainimagelabel_path)
    res = "Image Trained successfully" 
    message.configure(text=res)
    text_to_speech(res)

def getImagesAndLables(path):
    faces = []
    Ids = []
    imagePath = []
    for foldername in os.listdir(path):
        #print("*********"+foldername+"************")
        folderpath = os.path.join(path, foldername)
        #print(folderpath)
        if not os.path.isdir(folderpath):
            continue
        for filename in os.listdir(folderpath):
            if filename.endswith('.jpg'):
                filepath = os.path.join(folderpath, filename)
                pilImage = Image.open(filepath).convert("L")
                imageNp = np.array(pilImage, "uint8")
                Id = int(os.path.split(filepath)[-1].split("_")[1])
                imagePath.append(filepath)
                faces.append(imageNp)
                Ids.append(Id)
    return faces, Ids
