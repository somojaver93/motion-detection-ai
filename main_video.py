# کتابخانه OpenCV
import cv2


import config


from src.detector import MotionDetector

from src.recorder import VideoRecorder



# باز کردن فایل ویدئو
video = cv2.VideoCapture(
    config.VIDEO_PATH
)



detector = MotionDetector(
    config.MIN_AREA
)


recorder = VideoRecorder(
    config.OUTPUT_FOLDER
)



ret, previous_frame = video.read()

# چند فریم اول برای پایدار شدن تصویر رد می‌شوند
for i in range(10):

    video.read()



if not ret:

    print("Video error")

    exit()



previous_frame = cv2.resize(
    previous_frame,
    (
        config.FRAME_WIDTH,
        config.FRAME_HEIGHT
    )
)



recording = False



while True:


    ret, frame = video.read()


    if not ret:
        break



    frame = cv2.resize(
        frame,
        (
            config.FRAME_WIDTH,
            config.FRAME_HEIGHT
        )
    )



    output, motion = detector.detect(
        previous_frame,
        frame
    )



    if motion and output.shape[0] > 0:


        if not recording:

            recorder.start(output)

            recording = True



        recorder.write(output)



    else:


        if recording:

            recorder.stop()

            recording=False



    cv2.imshow(
        "Video Surveillance",
        output
    )



    previous_frame = frame



    if cv2.waitKey(25)==27:
        break



video.release()

cv2.destroyAllWindows()