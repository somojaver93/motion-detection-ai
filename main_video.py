# ==========================================
# Import Libraries
# ==========================================

# کتابخانه OpenCV
import cv2

# تنظیمات پروژه
from config import (
    VIDEO_PATH,
    OUTPUT_FOLDER,
    MIN_AREA,
    SCREENSHOT_FOLDER,
    EVENT_FILE,
    DATABASE_FILE
)

# ماژول تشخیص حرکت
from src.detector import MotionDetector

# ماژول ضبط ویدئو
from src.recorder import VideoRecorder

# ماژول ذخیره اسکرین‌شات
from src.screenshot import ScreenshotManager

# ماژول ثبت رویدادها
##from src.event_manager import EventManager

# سیستم لاگ
from utils.logger import logger

from src.database_manager import DatabaseManager


# ==========================================
# Main Function
# ==========================================

def main():

    # ثبت شروع برنامه
    logger.info(
        "Program Started"
    )

    # باز کردن فایل ویدئویی
    cap = cv2.VideoCapture(
        VIDEO_PATH
    )

    # بررسی باز شدن فایل
    if not cap.isOpened():

        logger.error(
            "Cannot Open Video File"
        )

        print(
            "Video error"
        )

        return

    # ساخت شیء تشخیص حرکت
    detector = MotionDetector(
        MIN_AREA
    )

    # ساخت شیء ضبط ویدئو
    recorder = VideoRecorder(
        OUTPUT_FOLDER
    )

    # ساخت شیء اسکرین‌شات
    screenshot_manager = ScreenshotManager(
        SCREENSHOT_FOLDER
    )

    # ساخت شیء دیتابیس
    database = DatabaseManager(
        DATABASE_FILE
    )

    # خواندن اولین فریم
    ret, previous_frame = cap.read()

    if not ret:

        logger.error(
            "Cannot Read First Frame"
        )

        return

    # ==========================================
    # حلقه اصلی برنامه
    # ==========================================

    while True:

        # خواندن فریم جدید
        ret, current_frame = cap.read()

        # پایان ویدئو
        if not ret:

            logger.info(
                "Video Finished"
            )

            break

        # تشخیص حرکت
        processed_frame, motion_detected = detector.detect(
            previous_frame,
            current_frame
        )

        # ==========================================
        # در صورت تشخیص حرکت
        # ==========================================

        if motion_detected:

            # اگر هنوز ضبط شروع نشده
            if not recorder.recording:

                logger.info(
                    "Motion Detected"
                )

                # ذخیره اسکرین‌شات
                screenshot_path = (
                    screenshot_manager.save(
                        current_frame
                    )
                )

                logger.info(
                    "Screenshot Saved"
                )

                # شروع ضبط و دریافت مسیر فایل
                video_path = recorder.start(
                    current_frame
                )

                logger.info(
                    "Recording Started"
                )

                database.insert_event(
                  screenshot_path
                )

                logger.info(
                    "Event Saved"
                )

        # ==========================================
        # ذخیره فریم‌ها هنگام ضبط
        # ==========================================

        if recorder.recording:

            recorder.write(
                current_frame
            )

        # ==========================================
        # نمایش تصویر
        # ==========================================

        cv2.imshow(
            "Motion Detection",
            processed_frame
        )

        # دریافت کلید فشرده شده
        key = cv2.waitKey(
            30
        )

        # خروج با q
        if key == ord("q"):

            logger.info(
                "Program Closed By User"
            )

            break

        # بروزرسانی فریم قبلی
        previous_frame = (
            current_frame.copy()
        )

    # ==========================================
    # پایان برنامه
    # ==========================================

    # توقف ضبط در صورت فعال بودن
    if recorder.recording:

        recorder.stop()

        logger.info(
            "Recording Stopped"
        )

    # آزادسازی منابع
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