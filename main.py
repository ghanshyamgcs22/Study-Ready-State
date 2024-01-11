import cv2
import numpy as np
import platform
import subprocess

# press q for stop the code or quit from running code 


def sleep_computer():
    # Determine the operating system
    system_platform = platform.system()

    if system_platform == "Windows":
        # Use subprocess to run the Windows command to put the computer to sleep
        subprocess.run(["rundll32.exe", "powrprof.dll,SetSuspendState", "0,1,0"])
    else:
        # Print a message for unsupported operating systems
        print("Unsupported operating system for sleep.")

# Open a connection to the webcam (0 indicates the default camera)
cap = cv2.VideoCapture(0)

# Flag to track if the sleep command has been executed
sleep_flag = False  

while 1:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Get the width and height of the frame
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define a color range for detecting red in the frame
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Create a mask to extract only the red color
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Apply the mask to the original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the resulting frame with the red color highlighted
    cv2.imshow('frame', result)

    # Count the number of non-zero pixels in the mask
    nonzero_count = cv2.countNonZero(mask)

    # If a sufficient amount of red is detected and sleep flag is not set
    if nonzero_count > 1000 and not sleep_flag:
        # Call the sleep_computer function to put the computer to sleep
        sleep_computer()
        # Set the flag to True to avoid sleep command on subsequent iterations
        sleep_flag = True  

    # If 'q' key is pressed, break out of the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
