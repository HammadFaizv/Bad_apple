import cv2 # !pip install opencv-python

# path of video
video = cv2.VideoCapture("Bad_Apple.mp4") # the video is in 144p
# success, image = video.read()
count = 1
while video.isOpened():
    success, image = video.read()
    cv2.imwrite(f"./Frames/frame_{count}.png", image) # imwrite( path, image)
    count += 1