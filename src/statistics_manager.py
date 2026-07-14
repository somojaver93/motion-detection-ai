# ==========================================
# Statistics Manager
# مدیریت آمار رویدادهای ثبت شده
# ==========================================


# مدیریت دیتابیس
from src.database_manager import (
    DatabaseManager
)

# زمان
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
        database_file

    ):

        # شیء دیتابیس
        self.database = DatabaseManager(

            database_file

        )


    # --------------------------------------
    # دریافت همه رویدادها
    # --------------------------------------
    def load_events(

        self

    ):

        return self.database.get_events()


    # --------------------------------------
    # تعداد کل رویدادها
    # --------------------------------------
    def total_events(

        self

    ):

        return self.database.count_events()


    # --------------------------------------
    # آخرین رویداد ثبت شده
    # --------------------------------------
    def last_event(

        self

    ):

        return self.database.get_last_event()


    # --------------------------------------
    # تعداد رویدادهای امروز
    # --------------------------------------
    def today_events(

        self

    ):

        events = self.load_events()

        today = datetime.now().date()

        count = 0

        for event in events:

            event_date = datetime.fromisoformat(

                event[1]

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

                event[1]

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

                event[1]

            )

            if (

                event_time.year == current_year

                and

                event_time.month == current_month

            ):

                count += 1

        return count