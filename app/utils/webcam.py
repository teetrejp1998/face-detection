from face_detection_engine import webcam_capture,face_detect,render
import cv2
from PIL.Image import open
from io import BytesIO
async def saveFaceMarking(source):
    cam = cv2.VideoCapture(source)
    frame, gray = webcam_capture(source=source)
    # cv2.imshow('Video', frame)
    # k = cv2.waitKey(0)
    # print(k)
    faces = face_detect(gray)
    render(image=frame,faces=faces,nogui=True)
async def saveFaceMarkingFromRTSP(rtsp):
    cam = cv2.VideoCapture(rtsp)
    frame, gray = webcam_capture(source=rtsp)
    # cv2.imshow('Video', frame)
    # k = cv2.waitKey(0)
    # print(k)
    faces = face_detect(gray)
    render(image=frame,faces=faces,nogui=True)


