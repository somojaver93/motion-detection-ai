# ==========================================
# Import Libraries
# ==========================================

import cv2

from config import (
    CAMERA_INDEX,
    OUTPUT_FOLDER,
    MIN_AREA
)

from src.detector import MotionDetector
from src.recorder import VideoRecorder

from utils.logger import logger


# ==========================================
# Main Function
# ==========================================

def main():

    logger.info(
        "Camera Mode Started"
    )

    cap = cv2.VideoCapture(
        CAMERA_INDEX
    )

    if not cap.isOpened():

        logger.error(
            "Cannot Open Camera"
        )

        print("Camera error")

        return

    detector = MotionDetector(
        MIN_AREA
    )

    recorder = VideoRecorder(
        OUTPUT_FOLDER
    )

    ret, previous_frame = cap.read()

    if not ret:

        logger.error(
            "Cannot Read First Frame"
        )
        
        print("Camera detected but cannot provide frames")

        return

    while True:

        ret, current_frame = cap.read()

        if not ret:

            logger.error(
                "Cannot Read Camera Frame"
            )

            break

        processed_frame, motion_detected = detector.detect(
            previous_frame,
            current_frame
        )

        if motion_detected:

            logger.info(
                "Motion Detected"
            )

            if not recorder.recording:

                logger.info(
                    "Recording Started"
                )

                recorder.start(
                    current_frame
                )

        if recorder.recording:

            recorder.write(
                current_frame
            )

        cv2.imshow(
            "Motion Detection",
            processed_frame
        )

        key = cv2.waitKey(1)

        if key == ord("q"):

            logger.info(
                "Program Closed By User"
            )

            break

        previous_frame = current_frame.copy()

    if recorder.recording:

        recorder.stop()

    cap.release()

    cv2.destroyAllWindows()

    logger.info(
        "Camera Mode Closed"
    )


if __name__ == "__main__":
    main()