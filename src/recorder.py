# کتابخانه OpenCV برای ساخت و ذخیره ویدئو
import cv2

# کتابخانه زمان برای نام‌گذاری فایل‌ها
import time

# ساخت پوشه‌ها و مدیریت مسیرها
import os



# کلاس ضبط ویدئو (Video Recorder)
class VideoRecorder:


    # سازنده کلاس
    def __init__(self, output_folder):

        # مسیر ذخیره ویدئوها
        self.output_folder = output_folder


        # اگر پوشه وجود نداشت، آن را بساز
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)



        # در ابتدا ضبط‌ کننده نداریم
        self.writer = None



    # شروع ضبط ویدئو
    def start(self, frame):


        # گرفتن اندازه فریم
        height, width, _ = frame.shape



        # ساخت نام فایل با زمان فعلی
        filename = (
            self.output_folder
            + "motion_"
            + str(int(time.time()))
            + ".avi"
        )



        # کد فشرده‌سازی ویدئو
        fourcc = cv2.VideoWriter_fourcc(
            *"XVID"
        )



        # ایجاد شیء ذخیره ویدئو
        self.writer = cv2.VideoWriter(
            filename,
            fourcc,
            20.0,
            (width, height)
        )



        print(
            "Recording started:",
            filename
        )



    # اضافه کردن فریم به ویدئو
    def write(self, frame):

        # اگر ضبط فعال بود
        if self.writer:

            self.writer.write(frame)



    # توقف ضبط
    def stop(self):

        # اگر ضبط ‌کننده وجود داشت
        if self.writer:


            # آزاد کردن فایل ویدئو
            self.writer.release()


            # خالی کردن مقدار
            self.writer = None


            print(
                "Recording stopped"
            )