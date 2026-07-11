# ==========================================
# اجرای پروژه با فایل ویدئویی (Video Mode)
# ==========================================


# کتابخانه OpenCV برای پردازش تصویر
import cv2


# فایل تنظیمات پروژه
import config


# کلاس تشخیص حرکت
from src.detector import MotionDetector


# کلاس ضبط ویدئو
from src.recorder import VideoRecorder



# ------------------------------------------
# باز کردن فایل ویدئویی
# ------------------------------------------

video = cv2.VideoCapture(
    config.VIDEO_PATH
)



# بررسی باز شدن فایل
if not video.isOpened():

    print("Video file not found")

    exit()



# ------------------------------------------
# دریافت اولین فریم
# ------------------------------------------

ret, previous_frame = video.read()



# اگر اولین فریم خوانده نشد
if not ret:

    print("Cannot read video")

    video.release()

    exit()



# ------------------------------------------
# تغییر اندازه اولین فریم
# ------------------------------------------

previous_frame = cv2.resize(
    previous_frame,
    (
        config.FRAME_WIDTH,
        config.FRAME_HEIGHT
    )
)



# ------------------------------------------
# ساخت شیء تشخیص حرکت
# ------------------------------------------

detector = MotionDetector(
    config.MIN_AREA
)



# ------------------------------------------
# ساخت شیء ضبط ویدئو
# ------------------------------------------

recorder = VideoRecorder(
    config.OUTPUT_FOLDER
)



# وضعیت ضبط
recording = False



print("Video mode started")
print("Press ESC to exit")



# ==========================================
# حلقه اصلی برنامه
# ==========================================

while True:


    # دریافت فریم جدید
    ret, frame = video.read()



    # اگر ویدئو تمام شد
    if not ret:

        print("Video finished")

        break



    # تغییر اندازه فریم
    frame = cv2.resize(
        frame,
        (
            config.FRAME_WIDTH,
            config.FRAME_HEIGHT
        )
    )



    # تشخیص حرکت
    output, motion = detector.detect(
        previous_frame,
        frame
    )



    # --------------------------------------
    # اگر حرکت تشخیص داده شد
    # --------------------------------------

    if motion:


        # اگر هنوز ضبط شروع نشده
        if not recording:


            # شروع ضبط
            recorder.start(
                output
            )


            recording = True



        # ذخیره فریم
        recorder.write(
            output
        )



        # نمایش متن روی تصویر
        cv2.putText(
            output,
            "Motion Detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )



    # --------------------------------------
    # اگر حرکتی وجود نداشت
    # --------------------------------------

    else:


        # اگر قبلاً ضبط انجام می‌شد
        if recording:


            # پایان ضبط
            recorder.stop()


            recording = False



    # --------------------------------------
    # نمایش تصویر
    # --------------------------------------

    cv2.imshow(
        "Video Surveillance",
        output
    )



    # فریم فعلی برای مقایسه در مرحله بعد
    previous_frame = frame.copy()



    # خروج با کلید ESC
    if cv2.waitKey(25) & 0xFF == 27:

        break



# ==========================================
# آزاد کردن منابع
# ==========================================


# اگر هنوز در حال ضبط بود
if recording:

    recorder.stop()



# آزاد کردن فایل ویدئویی
video.release()



# بستن تمام پنجره‌ها
cv2.destroyAllWindows()



print("Program stopped")