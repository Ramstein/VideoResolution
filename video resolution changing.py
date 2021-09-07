

import cv2
import numpy as np


video_file = r"C:\Users\user\Documents\course\Downloaded\Introduction_to_video_game_development_with_Unity\02-Module_2_-_Basic_concepts_in_Unity\01-Basic concepts in Unity _ 9_58 _ UPV-eqTNrJg3ZSU.mp4"

cap = cv2.VideoCapture(video_file)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 5, (1920, 1080))

while True:
    ret, frame = cap.read()
    if ret == True:
        b = cv2.resize(frame, (1920, 1080), fx=0, fy=0, interpolation=cv2.INTER_CUBIC)
        out.write(b)
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()