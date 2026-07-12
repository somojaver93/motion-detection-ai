import cv2

cap = cv2.VideoCapture(0)

print("Opened:", cap.isOpened())

for i in range(5):
    ret, frame = cap.read()
    print(f"Try {i}: {ret}")

cap.release()