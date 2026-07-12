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
    # processed_frame : تصویر پردازش شده
    # motion_detected : وضعیت وجود حرکت
    def detect(
        self,
        previous_frame,
        current_frame
    ):

        # محاسبه اختلاف دو فریم
        frame_delta = cv2.absdiff(
            previous_frame,
            current_frame
        )

        # تبدیل به تصویر خاکستری
        gray = cv2.cvtColor(
            frame_delta,
            cv2.COLOR_BGR2GRAY
        )

        # حذف نویز
        blur = cv2.GaussianBlur(
            gray,
            (5, 5),
            0
        )

        # تبدیل به تصویر باینری
        _, thresh = cv2.threshold(
            blur,
            25,
            255,
            cv2.THRESH_BINARY
        )

        # افزایش ضخامت نواحی متحرک
        dilated = cv2.dilate(
            thresh,
            None,
            iterations=3
        )

        # یافتن کانتورهای حرکت
        contours, _ = cv2.findContours(
            dilated,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # فرض می‌کنیم حرکتی وجود ندارد
        motion_detected = False

        # بررسی کانتورها
        for contour in contours:

            # محاسبه مساحت کانتور
            area = cv2.contourArea(
                contour
            )

            # حذف نویزهای کوچک
            if area < self.min_area:
                continue

            # محاسبه مستطیل احاطه کننده
            x, y, w, h = cv2.boundingRect(
                contour
            )

            # رسم کادر سبز
            cv2.rectangle(
                current_frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # نوشتن متن Motion
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
        return (
            current_frame,
            motion_detected
        )