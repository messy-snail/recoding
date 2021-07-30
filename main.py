import sys
import cv2


file_name = 1
num = 0
while True:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print('cam error')
        break
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out = cv2.VideoWriter(f'{file_name}.mp4', fourcc, 10,
                          (width,height))
    while (True):
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow('frame', frame)
            key = cv2.waitKey(100)
            if key == 27:
                break
            num+=1
        else:
            break
        if num >=1800:
            break


    cap.release()
    out.release()
    file_name+=1
    key = cv2.waitKey(50)
    if key == 27:
        break

