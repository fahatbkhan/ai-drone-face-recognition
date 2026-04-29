# AI-Driven Drone with Robotic Arm

Developed an intelligent UAV system integrating AI-based facial recognition with robotic actuation for targeted payload delivery. The system uses Raspberry Pi for real-time image processing, OpenCV for face detection, Arduino for robotic arm control, and Pixhawk for autonomous flight.

---

## Research Publication

**Integration of AI-Driven Facial Recognition and Robotics in Drone Systems for Critical Operations**

- Published in: IOSR Journal of Electronics and Communication Engineering (IOSR-JECE)
- First Author: Fahat Bar Khan
- DOI: https://doi.org/10.9790/2834-1904010915

---

## Tech Stack
- Python
- OpenCV
- Raspberry Pi 4B
- Arduino (Portenta H7)
- Pixhawk Flight Controller
- PX4 Autopilot

---

## How It Works
1. FPV camera captures real-time video feed  
2. Raspberry Pi processes frames using OpenCV  
3. Face recognition model detects and matches faces  
4. If a match is found, a signal is sent to Arduino  
5. Arduino controls the robotic arm to deliver payload  
6. Pixhawk manages flight control and stability  

---

## Features
- Real-time face detection using OpenCV  
- Autonomous drone navigation using Pixhawk (PX4)  
- Robotic arm for automated payload delivery  
- Integration of AI, embedded systems, and robotics  
- Real-time processing on Raspberry Pi  

---

## Code Structure
- src/face_detection.py → detects faces using OpenCV  
- src/face_recognition.py → identifies known faces  
- src/trigger_action.py → simulates payload delivery  

---

## How to Run
1. Install dependencies  
   pip install -r requirements.txt  

2. Run the program  
   python src/face_detection.py  

---

## Author
Fahat Bar Khan
