from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import numpy as np

#start import

import tensorflow as tf
from keras import layers, utils

saved_tumodel2 = tf.keras.models.load_model("D:\i3 python\data\deutsch\local1.h5")
import cv2
#
classNames = {0: 'Speed limit (20km/h)',
 1: 'Speed limit (30km/h)',
 2: 'Speed limit (50km/h)',
 3: 'Speed limit (60km/h)',
 4: 'Speed limit (70km/h)',
 5: 'Speed limit (80km/h)',
 6: 'End of speed limit (80km/h)',
 7: 'Speed limit (100km/h)',
 8: 'Speed limit (120km/h)',
 9: 'No passing',
 10: 'No passing for vehicles over 3.5 metric tons',
 11: 'Right-of-way at the next intersection',
 12: 'Priority road',
 13: 'Yield',
 14: 'Stop',
 15: 'No vehicles',
 16: 'Vehicles over 3.5 metric tons prohibited',
 17: 'No entry',
 18: 'General caution',
 19: 'Dangerous curve to the left',
 20: 'Dangerous curve to the right',
 21: 'Double curve',
 22: 'Bumpy road',
 23: 'Slippery road',
 24: 'Road narrows on the right',
 25: 'Road work',
 26: 'Traffic signals',
 27: 'Pedestrians',
 28: 'Children crossing',
 29: 'Bicycles crossing',
 30: 'Beware of ice/snow',
 31: 'Wild animals crossing',
 32: 'End of all speed and passing limits',
 33: 'Turn right ahead',
 34: 'Turn left ahead',
 35: 'Ahead only',
 36: 'Go straight or right',
 37: 'Go straight or left',
 38: 'Keep right',
 39: 'Keep left',
 40: 'Roundabout mandatory',
 41: 'End of no passing',
 42: 'End of no passing by vehicles over 3.5 metric tons'}


#end import

root = Tk()
root.title("Traffic sign detect")
root.geometry('1000x800')

header = Label(root, text='Welcome to Group 9 KITS Data Science Project', bg='blue', fg='white', font=("Helvetica", 32, 'bold'))
header.grid(row=0, columnspan=2)

askToUpload=Label(root, text='Upload a photo to be predicted', fg='#ed6e13', font=("Helvetica", 14, 'italic'))
askToUpload.grid(row=1, column=0)
def uploadPhoto():


    global filename
    filename = filedialog.askopenfilename(initialdir="D:\\i3 python\\test1", title="Select your photo",
                                          filetypes=(("jpg files", "*.jpg"),('png files','*.png'),('jpeg files','*.jpeg'), ("all files", "*.*")))

    WIDTH =120
    HEIGHT =120


    global img
    img= ImageTk.PhotoImage(Image.open(filename).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
    # global uploadedPhoto
    uploadedPhoto= Label(image=img,width=120,height=120)
    uploadedPhoto.grid(row=3,column=0)
    try:
        predictedResult.destroy()
    except:
        print('Label not initialized')

uploadButton =Button(root, text='Upload photo', bg='#87f542', padx=5, pady=5, fg='white', font='25', command=lambda :uploadPhoto())
uploadButton.grid(row=2, column=0)

def predictPhoto():
    testimg = cv2.imread(filename)
    testimg = cv2.resize(testimg, (32, 32))
    testimg = np.array(testimg)
    testArray = np.zeros((1, 32, 32, 3))
    testArray[0] = testimg
    testArray = testArray.astype("float") / 255.0

    result2 = saved_tumodel2.predict(testArray[0:1])
    final2 = np.argmax(result2)
    classname = classNames[final2]


    global  predictedResult

    predictedResult = Label(root, font=("Helvetica", 32, 'bold'), fg='red')
    predictedResult.grid(row=4, column=1)
    predictedResult.config(text=classname)


predictButton = Button(root,text='Predict',bg='#87f542',padx=10,pady=10,fg='white',font='45',command=lambda :predictPhoto())
predictButton.grid(row=2,column=1)
predictLabel =Label(root, text='Predicting Result:', font=("Helvetica", 18, 'italic'), fg='#ed6e13')
predictLabel.grid(row=3, column=1)


# thay1= ImageTk.PhotoImage(Image.open('thay1.jpg'))



root.mainloop()