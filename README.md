# Smart Study Environment Automation


## Overview

The Smart Study Environment Automation project is a creative solution to automate the transition from recreational activities to focused study sessions. By leveraging computer vision and automation, this project detects the presence of a predefined blue color in the webcam feed, signaling the system to put the computer into sleep mode.

## Features

- **Color-Based Presence Detection:** Utilizes OpenCV and Python to monitor the webcam feed for the presence of a predefined blue color.

- **Automated Computer Sleep Control:** Triggers a sleep command when the blue color is detected, ensuring a seamless transition to a study-ready environment.

## Setup

1. Connect a webcam to your system and position it strategically at the entrance gate.

2. Hang a blue material in the camera's view to serve as the detection trigger.

3. Install the required dependencies using `requirements.txt`.
   
4.opencv-python>=4.5.3
 numpy>=1.21.2
 pyautogui>=0.9.53 

   ```bash
   pip install -r requirements.txt
   pip install opencv
   pip install pyautogui
   pip install numpy
