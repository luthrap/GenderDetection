# GenderDetection
Supervised learning for gender detection from the given image/webcam using OpenCV API and HAART training model

# What it does
Uses OpenCV library for Python to process images or camera capture to detect the face from the source and estimating that the face belongs to male or female using HAART training model and Fisheface.

# PreRequisites
Python 2.7.12
OpenCV 3.1.0 (Read [installing OpenCV on Ubuntu](https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/). Windows and Mac setups are similar and help available on stackoverflow and other pages)

# Use
Run program from the command. It takes 3 parameters
a) HAAR Case training files location(.xml)
b) Training files location(.jpeg,.png etc). The location should have 2 subdirectories namely : Male and Female. Male directory should have male photgraphs and similary for Female directory. 
c) Location of the input file for which the user is interested to detect the classification. It can be set to 0 to use webcam.
