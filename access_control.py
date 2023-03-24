# Importing necessary libraries
import cv2 as cv
from PIL import Image
from deepface import DeepFace
import os
from time import sleep

# Importing libraries for RFID card reader
from Jetson_MFRC522 import SimpleMFRC522
import Jetson.GPIO as GPIO

# Function to take photo using the connected camera and save it as the specified filename
def take_photo(filename='photo.jpg'):
    cam_port = 0
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
        cv.waitKey(3000)
        cv.destroyWindow("ACS")
      
    # If captured image is corrupted, move to else part
    else:
        print("No image detected. Please try again.")

# Function to read the card's unique ID using the RFID reader
def getCardUid():
  reader = SimpleMFRC522()
  id, text = reader.read()
  return id

# Main function to run the project
def run():
  # Creating a list of authorized users based on image files in the 'database' directory
  authorizedUsers = [x.split('.')[0] for x in os.listdir('./database') if x.endswith('.jpg')]
  print('Authorized users:')
  print(authorizedUsers)
  print('----------------')
  init = False
  
  # Loop to continuously monitor for card swipes
  while(True):
    # Read the card's unique ID
    card_uid = str(getCardUid())

    # If a card is detected, check if it is an authorized user
    if card_uid:
      print()
      print(f'Passing with card {card_uid}.')

      if card_uid in authorizedUsers:
        # Take a photo with the connected camera
        take_photo('photo.jpg')
        
        # Use DeepFace library to verify if the captured photo matches the authorized user's face
        result = DeepFace.verify(img1_path = f'./database/{card_uid}.jpg', 
                                 img2_path = 'photo.jpg', 
                                 enforce_detection = False,
                                 prog_bar = False, 
                                 #model_name = 'Facenet512')
                                 model_name = 'VGG-Face')
        print(result)
        print()

        # If this is the first card swipe, print a message and continue monitoring for card swipes
        if not init:
          print('Init finished')
          init = True
          continue

        # If the captured photo matches the authorized user's face, grant access
        if result['verified'] == True:
          print('Authorized ' + card_uid + ' !')
        # If the captured photo does not match the authorized user's face, deny access
        else:
          print('Not authorized face!')
      # If the card is not an authorized user, deny access
      else:
        print('Not authorized card!')
    
    # Pause for 5 seconds before checking for another card swipe
    sleep(5)

# Run the main function
try:
  run()
except KeyboardInterrupt:
  GPIO.cleanup()
  raise
