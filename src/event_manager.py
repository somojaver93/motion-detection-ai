# ==========================================
# Event Manager
# ذخیره رویدادهای تشخیص حرکت
# ==========================================

# کار با فایل JSON
import json

# مدیریت فایل‌ها
import os

# زمان
from datetime import datetime


# کلاس مدیریت رویدادها
class EventManager:


    # سازنده کلاس
    def __init__(self, event_file):

        # مسیر فایل رویدادها
        self.event_file = event_file

        # اگر فایل وجود نداشت
        if not os.path.exists(
            self.event_file
        ):

            with open(
                self.event_file,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )


    # ثبت رویداد جدید
    def save_event(
        self,
        screenshot_path,
        video_path=None
    ):

        # خواندن رویدادهای قبلی
        with open(
            self.event_file,
            "r",
            encoding="utf-8"
        ) as file:

            events = json.load(
                file
            )

        # ساخت شناسه یکتا
        event_id = len(events) + 1

        # ساخت رویداد
        event = {

            "id": event_id,

            "time": str(
                datetime.now()
            ),

            "screenshot": screenshot_path,

            "video": video_path

        }

        # افزودن رویداد
        events.append(
            event
        )

        # ذخیره فایل
        with open(
            self.event_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                events,
                file,
                indent=4,
                ensure_ascii=False
            )