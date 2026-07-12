# ==========================================
# Import Libraries
# ==========================================

import cv2

from config import (
    VIDEO_PATH,
    OUTPUT_FOLDER,
    MIN_AREA,
    SCREENSHOT_FOLDER
)

from src.detector import MotionDetector
from src.recorder import VideoRecorder
from src.screenshot import ScreenshotManager

from utils.logger import logger


# ==========================================
# Main Function
# ==========================================

def main():

    logger.info("Program Started")

    cap = cv2.VideoCapture(VIDEO_PATH)

    if not cap.isOpened():

        logger.error(
            "Cannot Open Video File"
        )

        print("Video error")

        return

    detector = MotionDetector(
        MIN_AREA
    )

    recorder = VideoRecorder(
        OUTPUT_FOLDER
    )

    screenshot_manager = ScreenshotManager(
    SCREENSHOT_FOLDER
    )

    # خواندن اولین فریم
    ret, previous_frame = cap.read()

    if not ret:

        logger.error(
            "Cannot Read First Frame"
        )

        return

    while True:

        ret, current_frame = cap.read()

        if not ret:

            logger.info(
                "Video Finished"
            )

            break

        processed_frame, motion_detected = detector.detect(
            previous_frame,
            current_frame
        )

        if motion_detected:

         if not recorder.recording:

           logger.info(
              "Motion Detected"
           )

           screenshot_manager.save(
               current_frame
           )

           logger.info(
              "Screenshot Saved"
          )

           recorder.start(
              current_frame
          )

           logger.info(
              "Recording Started"
          )

        if recorder.recording:

            recorder.write(
                current_frame
            )

        cv2.imshow(
            "Motion Detection",
            processed_frame
        )

        key = cv2.waitKey(30)

        if key == ord("q"):

            logger.info(
                "Program Closed By User"
            )

            break

        # فریم قبلی برای دور بعد
        previous_frame = current_frame.copy()

    if recorder.recording:

        logger.info(
            "Recording Stopped"
        )

        recorder.stop()

    cap.release()

    cv2.destroyAllWindows()

    logger.info(
        "Program Closed"
    )


# ==========================================
# Program Entry Point
# ==========================================

if __name__ == "__main__":
    main()