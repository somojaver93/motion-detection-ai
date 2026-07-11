# ==========================================
# ماژول تشخیص حرکت (Motion Detection)
# ==========================================


# کتابخانه OpenCV برای پردازش تصویر
import cv2



# کلاس تشخیص حرکت
class MotionDetector:


    # سازنده کلاس
    # min_area حداقل اندازه جسم قابل قبول است
    def __init__(self, min_area):

        # ذخیره حداقل مساحت جسم
        self.min_area = min_area



    # تابع اصلی تشخیص حرکت
    # ورودی:
    # previous_frame : فریم قبلی
    # current_frame  : فریم فعلی
    #
    # خروجی:
    # تصویر پردازش شده
    # وضعیت وجود حرکت
    def detect(
            self,
            previous_frame,
            current_frame
    ):


        # محاسبه اختلاف دو فریم
        # قسمت‌های تغییر کرده مشخص می‌شوند
        frame_delta = cv2.absdiff(
            previous_frame,
            current_frame
        )



        # تبدیل تصویر به خاکستری
        # چون تشخیص حرکت به رنگ نیاز ندارد
        gray = cv2.cvtColor(
            frame_delta,
            cv2.COLOR_BGR2GRAY
        )



        # کاهش نویز تصویر
        blur = cv2.GaussianBlur(
            gray,
            (5, 5),
            0
        )



        # تبدیل تصویر به سیاه و سفید
        # تغییرات روشن سفید می‌شوند
        _, thresh = cv2.threshold(
            blur,
            25,
            255,
            cv2.THRESH_BINARY
        )



        # پر کردن قسمت‌های شکسته حرکت
        dilated = cv2.dilate(
            thresh,
            None,
            iterations=3
        )



        # پیدا کردن محدوده‌های تغییر
        contours, _ = cv2.findContours(
            dilated,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )



        # در ابتدا حرکتی نداریم
        motion_detected = False



        # بررسی تمام اجسام پیدا شده
        for contour in contours:


            # محاسبه مساحت جسم
            area = cv2.contourArea(
                contour
            )


            # حذف نویزهای کوچک
            if area < self.min_area:

                continue



            # پیدا کردن مستطیل اطراف جسم
            x, y, w, h = cv2.boundingRect(
                contour
            )



            # محاسبه اندازه واقعی کادر
            object_size = w * h



            # فقط اجسام بزرگ را قبول کن
            if object_size < self.min_area:

                continue



            # رسم کادر سبز دور جسم
            cv2.rectangle(
                current_frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )



            # نمایش مقدار حرکت
            cv2.putText(
                current_frame,
                "Motion",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )



            # حرکت پیدا شد
            motion_detected = True



        # برگرداندن نتیجه
        return current_frame, motion_detected