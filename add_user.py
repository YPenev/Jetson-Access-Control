# Importing necessary libraries
import cv2 as cv
from PIL import Image
from Jetson_MFRC522 import SimpleMFRC522
import sys
import Jetson.GPIO as GPIO

# Function to take photo using OpenCV library and save it
def take_photo(filename='photo.jpg'):
    # Defining the camera port
    cam_port = 0
    
    # Creating a VideoCapture object
    cam = cv.VideoCapture(cam_port)
  
    # Reading the input using the camera
    result, image = cam.read()
      
    # If image is detected without any error, show result
    if result:
        # Showing result, it takes frame name and image output
        cv.imshow("ACS", image)
      
        # Saving image in local storage
        cv.imwrite(filename, image)
      
        # If keyboard interrupt occurs, destroy image window
        cv.waitKey(0)
        cv.destroyWindow("ACS")
      
    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please try again.")

# Creating an instance of SimpleMFRC522
reader = SimpleMFRC522()

try:
    while True:
        # Prompting the user to hold a tag near the reader
        print("Hold a tag near the reader")
        
        # Reading the RFID tag and text associated with it
        id, text = reader.read()
        
        # If an RFID tag is detected
        if id:
            # Take a photo and save it with the tag ID as the filename in the 'database' folder
            filename = take_photo(f'./database/{id}.jpg')
            print("Photo saved successfully.")
            break
        else:
            # Wait for 5 seconds before trying again
            sleep(5)
except KeyboardInterrupt:
    # Clean up the GPIO pins on keyboard interrupt
    #GPIO.cleanup()
    raise
