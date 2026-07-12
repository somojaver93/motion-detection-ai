# کتابخانه OpenCV برای ساخت و ذخیره ویدئو
import cv2

# کتابخانه زمان برای نام‌گذاری فایل‌ها
import time

# ساخت پوشه‌ها و مدیریت مسیرها
import os


# کلاس ضبط ویدئو
class VideoRecorder:

    # سازنده کلاس
    def __init__(self, output_folder):

        # مسیر ذخیره ویدئوها
        self.output_folder = output_folder

        # اگر پوشه وجود نداشت آن را بساز
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # شیء ذخیره کننده ویدئو
        self.writer = None

        # وضعیت ضبط
        self.recording = False

    # شروع ضبط
    def start(self, frame):

        height, width, _ = frame.shape

        filename = (
            self.output_folder
            + "motion_"
            + str(int(time.time()))
            + ".avi"
        )

        fourcc = cv2.VideoWriter_fourcc(*"XVID")

        self.writer = cv2.VideoWriter(
            filename,
            fourcc,
            20.0,
            (width, height)
        )

        self.recording = True

        print(
            "Recording started:",
            filename
        )

    # نوشتن فریم
    def write(self, frame):

        if self.writer:
            self.writer.write(frame)

    # توقف ضبط
    def stop(self):

        if self.writer:

            self.writer.release()

            self.writer = None

            self.recording = False

            print(
                "Recording stopped"
            )