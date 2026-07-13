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

        # ساخت پوشه در صورت نبودن
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # شیء ذخیره کننده ویدئو
        self.writer = None

        # وضعیت ضبط
        self.recording = False

        # مسیر آخرین ویدئوی ذخیره شده
        self.video_path = None


    # شروع ضبط
    def start(self, frame):

        # ابعاد تصویر
        height, width, _ = frame.shape

        # ساخت نام فایل
        filename = (
            self.output_folder
            + "motion_"
            + str(int(time.time()))
            + ".avi"
        )

        # ذخیره مسیر فایل
        self.video_path = filename

        # کدک ویدئو
        fourcc = cv2.VideoWriter_fourcc(
            *"XVID"
        )

        # ایجاد فایل ویدئو
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

        # برگرداندن مسیر فایل
        return filename


    # ذخیره فریم
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


    # دریافت مسیر آخرین ویدئو
    def get_video_path(self):

        return self.video_path