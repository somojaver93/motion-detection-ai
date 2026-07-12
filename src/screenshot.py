# ==========================================
# Screenshot Manager
# ==========================================

# کتابخانه OpenCV
import cv2

# کتابخانه زمان
import time

# مدیریت پوشه‌ها
import os


# کلاس ذخیره اسکرین‌شات
class ScreenshotManager:

    # سازنده کلاس
    def __init__(self, output_folder):

        # مسیر ذخیره تصاویر
        self.output_folder = output_folder

        # ساخت پوشه در صورت نبودن
        os.makedirs(
            output_folder,
            exist_ok=True
        )

    # ذخیره تصویر
    def save(self, frame):

        # نام فایل بر اساس زمان
        filename = os.path.join(
            self.output_folder,
            f"motion_{int(time.time())}.jpg"
        )

        # ذخیره تصویر
        cv2.imwrite(
            filename,
            frame
        )

        print(
            "Screenshot saved:",
            filename
        )

        return filename