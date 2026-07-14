# ==========================================
# Statistics Manager
# مدیریت آمار رویدادهای ثبت شده
# ==========================================


# خواندن فایل JSON
import json

# مدیریت فایل‌ها
import os

# کار با تاریخ و زمان
from datetime import datetime


# ==========================================
# کلاس مدیریت آمار
# ==========================================
class StatisticsManager:


    # --------------------------------------
    # سازنده کلاس
    # --------------------------------------
    def __init__(

        self,
        event_file

    ):

        # مسیر فایل رویدادها
        self.event_file = event_file


    # --------------------------------------
    # خواندن همه رویدادها
    # --------------------------------------
    def load_events(self):

        # اگر فایل وجود نداشت
        if not os.path.exists(

            self.event_file

        ):

            return []



        # باز کردن فایل JSON
        with open(

            self.event_file,

            "r",

            encoding="utf-8"

        ) as file:


            # تبدیل JSON به لیست پایتون
            events = json.load(

                file

            )


        return events


    # --------------------------------------
    # تعداد کل رویدادها
    # --------------------------------------
    def total_events(

        self

    ):

        # دریافت رویدادها
        events = self.load_events()


        # تعداد رکوردها
        return len(

            events

        )


    # --------------------------------------
    # آخرین رویداد ثبت شده
    # --------------------------------------
    def last_event(

        self

    ):

        # دریافت رویدادها
        events = self.load_events()


        # اگر هیچ رویدادی وجود نداشت
        if len(

            events

        ) == 0:

            return None


        # آخرین عنصر لیست
        return events[-1]
    
        # --------------------------------------
    # تعداد رویدادهای امروز
    # --------------------------------------
    def today_events(

        self

    ):

        # دریافت همه رویدادها
        events = self.load_events()

        # تاریخ امروز
        today = datetime.now().date()

        count = 0

        # بررسی همه رویدادها
        for event in events:

            event_date = datetime.fromisoformat(

                event["time"]

            ).date()

            if event_date == today:

                count += 1

        return count
    
        # --------------------------------------
    # تعداد رویدادهای هفته جاری
    # --------------------------------------
    def week_events(

        self

    ):

        events = self.load_events()

        today = datetime.now()

        count = 0

        for event in events:

            event_time = datetime.fromisoformat(

                event["time"]

            )

            difference = (

                today - event_time

            ).days

            if difference <= 7:

                count += 1

        return count
    
        # --------------------------------------
    # تعداد رویدادهای ماه جاری
    # --------------------------------------
    def month_events(

        self

    ):

        events = self.load_events()

        current_year = datetime.now().year

        current_month = datetime.now().month

        count = 0

        for event in events:

            event_time = datetime.fromisoformat(

                event["time"]

            )

            if (

                event_time.year == current_year

                and

                event_time.month == current_month

            ):

                count += 1

        return count
    
    