# ==========================================
# Flask Dashboard
# داشبورد تحت وب پروژه
# ==========================================


# فریم‌ورک Flask
from flask import Flask

# فایل تنظیمات پروژه
from config import DATABASE_FILE

# مدیریت آمار
from src.statistics_manager import (
    StatisticsManager
)


# ==========================================
# ساخت برنامه Flask
# ==========================================

app = Flask(

    __name__

)


# ==========================================
# ساخت شیء آمار
# ==========================================

stats = StatisticsManager(

    DATABASE_FILE

)


# ==========================================
# صفحه اصلی
# ==========================================
@app.route("/")
def home():

    # تعداد کل رویدادها
    total_events = stats.total_events()

    # تعداد رویدادهای امروز
    today_events = stats.today_events()

    # تعداد رویدادهای هفته
    week_events = stats.week_events()

    # تعداد رویدادهای ماه
    month_events = stats.month_events()

    # آخرین رویداد
    last_event = stats.last_event()


    # ساخت صفحه HTML
    html = f"""

    <h1>Motion Detection Dashboard</h1>

    <hr>

    <h2>Statistics</h2>

    <p>Total Events: {total_events}</p>

    <p>Today Events: {today_events}</p>

    <p>Week Events: {week_events}</p>

    <p>Month Events: {month_events}</p>

    <hr>

    <h2>Last Event</h2>

    <p>{last_event}</p>

    """

    return html


# ==========================================
# اجرای برنامه
# ==========================================
if __name__ == "__main__":

    app.run(

        debug=True

    )