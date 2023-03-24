# Jetson-Access-Control
The project uses an Nvidia Jetson Nano with an RFID card reader and camera to grant access based on card authentication and face recognition using the DeepFace library.

# Project Description
The goal of this project is to create a system that allows access to a secure area only to authorized individuals. The system combines RFID card reading with face recognition technology to identify users and grant or deny access based on their identity.
The system is built using a Jetson Nano board, an MFRC522 RFID module, a USB camera, and the DeepFace computer vision library. The Jetson Nano board is a small, powerful computer that can run complex machine learning algorithms, making it an ideal platform for this project. The MFRC522 RFID module is a low-cost device that can read and write RFID cards. The USB camera captures images of users who are attempting to access the secure area, and the DeepFace library is used to perform face recognition.
To set up the system, we first need to install the necessary software libraries. This includes the mfrc522-python library for communicating with the RFID module, the opencv-python library for accessing the USB camera, and the DeepFace library for face recognition. Once the libraries are installed, we can connect the hardware components to the Jetson Nano board.
The MFRC522 module is connected to the Jetson Nano board using SPI pins, and the USB camera is connected to the board's USB port. We also need to create a database to store the authorized users' information. The database contains the users' unique RFID card number and a photo of their face.

The system works as follows:

1. When a user wants to access the secure area, they swipe their RFID card in front of the MFRC522 module. The module reads the card's unique identifier and sends it to the Jetson Nano board.
2. The Jetson Nano board checks if the RFID card number is valid and matches a number in the authorized users' database. If the card is allowed, the system proceeds to the next step. If not, access is denied.
3. The USB camera takes a picture of the user standing in front of it.
4. The DeepFace library is used to detect and extract the user's facial features from the captured image.
5. The system compares the extracted facial features with the features of the user associated with the swiped RFID card in the authorized users' database. If the faces match, access is granted. If not, access is denied.
6. The system displays the access status on a user interface, indicating whether access is allowed or denied.


# Libraries Used
The following libraries were used for this project:
•	OpenCV: used for image processing
•	PIL: used for image manipulation
•	DeepFace: used for face recognition
•	Jetson_MFRC522: used for interacting with the RFID reader
•	os: used for reading the names of files in the database directory
•	time: used for pausing the program for a few seconds before checking for a new card swipe
•	GPIO: used for cleaning up the GPIO pins when the program exits

# Code
The Python code for this project is contained in the file **access_control.py**. Here's a brief overview of the code:
1.	Import the required libraries.
2.	Define a function called **take_photo()** that initializes the camera and takes a photo when called. The function saves the photo with the name "photo.jpg" in the current directory. The function also displays the image on the screen for three seconds before closing the window.
3.	Define a function called **getCardUid()** that interacts with the RFID reader and returns the ID of the card that is swiped.
4.	Define a function called **run()** that initializes the authorized user list by reading the names of the files in the "./database" directory that end with ".jpg". It then enters into an infinite loop where it waits for a card to be swiped. Once a card is swiped, it checks if the card is in the authorized user list. If the card is authorized, it takes a photo using the **take_photo()** function and performs face recognition using DeepFace. If the face in the photo matches the face associated with the card, the user is granted access, and if not, access is denied.
5.	Enclose the code in a try-except block to handle a keyboard interrupt and clean up the GPIO pins before exiting the program.

# Usage
To run this project, follow these steps:
1.	Connect the USB camera and MFRC522 module to the Nvidia Jetson Nano board.
2.	Install the required libraries by running **pip install opencv-python pillow deepface Jetson.GPIO mfrc522** in the terminal.
3.	Create a directory called "database" in the same directory as the **access_control.py** file. In this directory, create a JPG image for each authorized user. The filename of each image should be the UID of the corresponding RFID card.
4.	Run the **access_control.py** file by typing **python access_control.py** in the terminal.
The program will start running and waiting for a card to be swiped. When a card is swiped, the program will take a photo using the USB camera and perform face recognition on the captured image. If the face in the image matches the face associated with the card, the user will be granted access. Otherwise, access will be denied. The program will continue running and waiting for new card swipes until it is interrupted by a keyboard interrupt.
 
