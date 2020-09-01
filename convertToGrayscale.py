import cv2

cap = cv2.VideoCapture('D:/Codes/openCV/data_videos/jnc.mp4')
video_name = 'video-jnc.avi'

fps = int(cap.get(cv2.CAP_PROP_FPS))

ret, frame = cap.read()
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
height, width = gray_frame.shape
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'DIVX'), fps, (width, height), False)

i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    video.write(gray_frame)
    i += 1

cap.release()
video.release()
cv2.destroyAllWindows()
